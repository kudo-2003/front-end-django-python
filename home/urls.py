from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]
