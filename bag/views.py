from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

# view bag
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


# add to bag
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    options = None
    if 'product_options' in request.POST:
        options = request.POST['product_options']
    bag = request.session.get('bag', {})

    if options:
        if item_id in list(bag.keys()):
            if options in bag[item_id]['items_by_options'].keys():
                bag[item_id]['items_by_options'][options] += quantity
                messages.success(request, f'Updated option {options.upper()} {product.name} quantity to {bag[item_id]["items_by_option"][option]}')
                
            else:
                bag[item_id]['items_by_options'][options] = quantity
                messages.success(request, f'Added  option {options.upper()} to your bag')
                
        else:
            bag[item_id] = {'items_by_options': {options: quantity}}
            messages.success(request, f'Added  option {options.upper()} to your bag')
           
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
           
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


#adjust bag
def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    options = None
    if 'product_options' in request.POST:
        options = request.POST['product_options']
    bag = request.session.get('bag', {})

    if options:
        if quantity > 0:
            bag[item_id]['items_by_options'][options] = quantity
            messages.success(request, f'Updated option {options.upper()} {product.name} quantity to {bag[item_id]["items_by_option"][option]}')
            
        else:
            del bag[item_id]['items_by_options'][options]
            if not bag[item_id]['items_by_options']:
                bag.pop(item_id)
                messages.success(request, f'Removed options {options.upper()} {product.name} from your bag')

               
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
            
        else:
            bag.pop(item_id)
            message.success(request, f'Removed {product.name} from your bag')
           

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

# remove from bag
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        options = None
        if 'product_options' in request.POST:
            options = request.POST['product_options']
        bag = request.session.get('bag', {})

        if options:
            del bag[item_id]['items_by_options'][options]
            if not bag[item_id]['items_by_options']:
                bag.pop(item_id)
            messages.success(request, f'Removed options {options.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
