from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

