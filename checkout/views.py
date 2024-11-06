from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/check_out.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QI8onAS7iZraKTaGiCMEPaPNXV8czKkvfNYBb1VYvJnACK1LnTUNMImFuIcJ1GSWhvQ5r5OtCXKusquVaXMerKi00kRLscZzs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)