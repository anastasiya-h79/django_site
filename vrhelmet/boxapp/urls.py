from django.urls import path
from boxapp import views

app_name = 'boxapp'

urlpatterns = [
    #path('checkout/', views.OrderListView.as_view(), name='order'),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    #url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),
    path('thanks/', views.checkout, name='thanks'),
    ##path('contact/', views.contacts, name='contact'),



]

# urlpatterns = [
#     path(r'^$', views.cart_detail, name='cart_detail'),
#     path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
#     path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
# ]