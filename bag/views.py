from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    # Ensure bag[item_id] is always a dictionary structure
    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}, 'quantity': 0}

    if size:
        # Handle items with sizes
        if size in bag[item_id]['items_by_size']:
            bag[item_id]['items_by_size'][size] += quantity
        else:
            bag[item_id]['items_by_size'][size] = quantity
    else:
        # Handle items without sizes
        bag[item_id]['quantity'] += quantity

    # Update the session
    request.session['bag'] = bag
    return redirect(redirect_url)
