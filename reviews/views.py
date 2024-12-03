from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from products.models import Product
from .forms import ReviewForm

# Create your views here.

# view product reviews
def product_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})

# add product reviews
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.user = request.user
        review.save()
        messages.success(request, "Your review has been submitted!")
        return redirect('product_reviews', product_id=product.id)

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

# update/ edit product reviews
@login_required
def edit_review(request, review_id):
    """Allow a user to edit their review"""
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect('product_reviews', product_id=review.product.id)  # Ensure redirect happens
        else:
            messages.error(request, "Failed to update the review. Please check the form.")
    
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})


# delete product reviews
@login_required
def delete_review(request, review_id):
    print("Delete review view accessed")  # Debugging
    print("Request method:", request.method)  # Debugging

    review = get_object_or_404(Review, id=review_id)
    print("Review to delete:", review)  # Debugging

    if request.method == "POST" and request.user == review.user:
        review.delete()
        messages.success(request, "Your review has been deleted.")
        print("Review deleted successfully")  # Debugging
    else:
        messages.error(request, "You are not authorized to delete this review.")
        print("Authorization failed or wrong method")  # Debugging

    return redirect('product_reviews', product_id=review.product.id)

