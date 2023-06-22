from django.urls import path
from . import views

app_name = 'boutique'
urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:category_id>/', views.product_list, name='product_list'),
]