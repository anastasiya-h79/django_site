from django.urls import path
from prodapp import views

app_name = 'prodapp'

urlpatterns = [
    path('', views.MainListView.as_view(), name='index'),
    #path('contact/', views.contacts, name='contact'),
    path('card/<int:pk>/', views.CardDetailView.as_view(), name='card'),   #CardDetailView.as_view()
    path('contactform/', views.ContactFormCreateView.as_view(), name='contactform'),
    path('helmets_category/<int:pk>/', views.StandaloneListView.as_view(), name='helmets_category'),
    #path('console/', views.console, name='console')


]