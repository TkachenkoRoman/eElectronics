from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
#from .tasks import order_created
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from home.forms import SignUpForm
from django.http import HttpResponseRedirect
from shop.models import Category


def order_create(request):
    categories = Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        sign_up_form = SignUpForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            sign_up_form.save()
            return HttpResponseRedirect('/home/')
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
            order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         sell_price=item['sell_price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
        sign_up_form = SignUpForm(request.POST or None)

    context = {'cart': cart,
               'form': form,
               'sign_up_form':sign_up_form,
               'categories': categories,
               }
    return render(request, 'orders/order/create.html', context)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

