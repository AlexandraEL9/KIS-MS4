from django.shortcuts import render, redirect, reverse, HttpResponse

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity  # Add quantity to existing item
    else:
        bag[item_id] = quantity  # Initialize item with quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity  # Set to new quantity
    else:
        bag.pop(item_id, None)  # Remove item if quantity is zero

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    bag = request.session.get('bag', {})
    bag.pop(item_id, None)  # Remove item

    request.session['bag'] = bag
    return HttpResponse(status=200)
