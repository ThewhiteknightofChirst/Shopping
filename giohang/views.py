from django.shortcuts import render, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from monan.models import Post
from .models import Cart
from django.urls import reverse 
# Create your views here.
@login_required
def index(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "shop/views.html"
    return render(request, template,context)
@login_required
def update_cart(request, id):
    cart = Cart.objects.all()[0]
    try:
        product = Post.objects.get(id=id)
    except:
        pass
    cart.product.add(product)
    new_total = 0.00
    for item in cart.product.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect('/')
@login_required
def delete_cart(request, id):
    cart = Cart.objects.all()[0]
    try:
        product = Post.objects.get(id=id)
    except:
        pass
    cart.product.remove(product)
    new_total = 0.00
    for item in cart.product.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()
    return HttpResponsePermanentRedirect(reverse("giohang"))
