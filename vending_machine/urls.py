"""
URL configuration for vending_machine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from apps.health.views import healthcheck
import apps.vending.views as vending_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthcheck/", healthcheck),
    path('login/', vending_views.LoginView.as_view()),
    path("user/", include([
        path("<str:username>/balance/", vending_views.UserBalanceView.as_view()),
        path("<str:username>/refund/", vending_views.UserBalanceRefundView.as_view()),
        path("<str:username>/", vending_views.UserView.as_view()),
    ])),
    path("products/", include([
        path("", vending_views.ProductsView.as_view()),
    ])),
    path("products/", include([
        path("", vending_views.ProductsView.as_view()),
        path("buy/<str:id>/", vending_views.BuyProductView.as_view()),
    ])),
]
