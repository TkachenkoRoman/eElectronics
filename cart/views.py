from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect
from coupons.forms import CouponApplyForm
from home.forms import SignUpForm



@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    product_list = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    if query:
        product_list = product_list.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
        return redirect('shop:product_list')

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            sign_up_form.save()
            return HttpResponseRedirect('/cart/')

    else:
        sign_up_form = SignUpForm()

    template = 'cart/detail.html'
    context = {'cart': cart,
               'sign_up_form': sign_up_form
               }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, template, {'cart': cart,
                                      'coupon_apply_form': coupon_apply_form,
                                      'sign_up_form': sign_up_form,
                                      'categories': categories,
                                      })
