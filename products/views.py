from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Fetch all categories for display purposes
    all_categories = Category.objects.all()  # This gets all categories

    # Initialize current_categories as a queryset or list
    current_categories = all_categories  # Set to all categories or filter based on user selection

    # Process GET requests for filtering
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            current_categories = Category.objects.filter(name__in=categories)  # Update current categories

        # ... additional filtering logic ...

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,  # Ensure this is a list of categories
        'all_categories': all_categories,  # All categories for badges
        'current_sorting': f'{sort}_{direction}',
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)