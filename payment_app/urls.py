"""
URL configuration for didikala_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from payment_app import views


urlpatterns = [
    path('add-to-basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('cart/', views.view_basket, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update_item_count/<int:item_id>/<str:action>/', views.update_item_count, name='update_item_count'),
    path('shopping-payement/', views.shopping_payement),
    path('shopping-complete-buy/', views.shopping_completed),
    path('shopping-no-complete-buy/', views.shopping_notcompleted),
    path('shopping/', views.shopping),
    path('finalize-order/', views.finalize_order, name='finalize_order'),
    path('', include('payment_app.api.urls')),
]
