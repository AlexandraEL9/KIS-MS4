from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.html import format_html

from .models import Favourite
from products.models import Product


@login_required
def favourites(request):
    """
    View the user's favourites list
    """
    favourites = Favourite.objects.filter(user=request.user)
    return render(
        request,
        'favourites/favourites.html',
        {'favourites': favourites}
    )


@login_required
def add_to_favourites(request, product_id):
    """
    Add a product to the favourites list
    """
    product = get_object_or_404(Product, pk=product_id)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user,
        product=product
    )

    favourites_url = reverse('favourites')  # Dynamically get the favourites URL

    if created:
        messages.success(
            request,
            format_html(
                "Added {} to your favourites. <a href='{}' class='alert-link'>View Favourites</a>",
                product.name,
                favourites_url
            )
        )
    else:
        messages.info(
            request,
            format_html(
                "{} is already in your favourites. <a href='{}' class='alert-link'>View Favourites</a>",
                product.name,
                favourites_url
            )
        )

    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_favourites(request, product_id):
    """
    Remove a product from the favourites list
    """
    product = get_object_or_404(Product, pk=product_id)

    try:
        favourite = Favourite.objects.get(user=request.user, product=product)
        favourite.delete()
        messages.success(
            request,
            format_html(
                "Removed {} from your favourites. <a href='{}' class='alert-link'>View Favourites</a>",
                product.name,
                reverse('favourites')
            )
        )
    except Favourite.DoesNotExist:
        messages.error(
            request,
            format_html(
                "{} was not found in your favourites. <a href='{}' class='alert-link'>View Favourites</a>",
                product.name,
                reverse('favourites')
            )
        )

    favourites = Favourite.objects.filter(user=request.user)

    return render(
        request,
        'favourites/favourites.html',
        {'favourites': favourites}
    )
