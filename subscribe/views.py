from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed to our newsletter!")
            return redirect('subscribe')  # Stay on the same page
    else:
        form = SubscribeForm()

    context = {
        'subscribe_form': form,
    }
    return render(request, 'subscribe/subscribe.html', context)
