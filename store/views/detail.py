from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from store.models.product import Product
from store.models.category import Category
from django.views import View

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'detail.html', context)
