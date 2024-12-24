from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import Favourite
from products.models import Product

# Create your views here.


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

    if created:
        messages.success(
            request,
            (
                f"Added {product.name} to your favourites. "
                "<a href='/favourites/' class='alert-link'>"
                "View Favourites</a>"
            )
        )
    else:
        messages.info(
            request,
            (
                f"{product.name} is already in your favourites. "
                "<a href='/favourites/' class='alert-link'>"
                "View Favourites</a>"
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
            f"Removed {product.name} from your favourites."
        )
    except Favourite.DoesNotExist:
        messages.error(
            request,
            f"{product.name} was not found in your favourites."
        )

    favourites = Favourite.objects.filter(user=request.user)

    return render(
        request,
        'favourites/favourites.html',
        {'favourites': favourites}
    )
