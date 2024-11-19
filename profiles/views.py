from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist

# view wishlist
def wishlist(request):
    """ view to show the user's wishlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)
