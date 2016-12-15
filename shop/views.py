from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product
from cart.forms import CartAddProductForm, CartAddOneProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from home.forms import SignUpForm
from django.http import HttpResponseRedirect


class CategoryListView(ListView):
    model = Category


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page')
        context['products'] = Product.objects.all()

        return context

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        products = Product.objects.all()
        page = self.request.GET.get('page')
        paginator = Paginator(products, 3)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            products = paginator.page(paginator.num_pages)
        return qs


def listing(request, category_slug=None):
    template = 'shop/list.html'
    products = Product.objects.filter(available=True)
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    cart_one_product_form = CartAddOneProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = request.GET.get('q')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

    paginator = Paginator(products, 8) # Show 25 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST or None)
        if sign_up_form.is_valid():
            email = sign_up_form.cleaned_data.get('email')
            sign_up_form.save()
            return HttpResponseRedirect('/shop/')
    else:
        sign_up_form = SignUpForm()

    context = {'products': products,
               'categories':categories,
               'sign_up_form': sign_up_form,
               'category':category,
               'cart_product_form': cart_product_form,
               'cart_one_product_form': cart_one_product_form,
                                              }

    return render(request, template, context )


