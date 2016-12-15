from django.conf.urls import url
from . import views
from .views import ProductListView, ProductDetailView
from .views import listing


urlpatterns = [
    url(r'^$', views.listing, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.listing, name='product_list_by_category'),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
]