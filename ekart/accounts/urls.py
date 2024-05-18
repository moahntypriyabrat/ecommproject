"""ekart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("", views.dashboard, name='dashboard'),
    path("forgotpassword/", views.forgotpassword, name='forgotpassword'),
    path("resetPassword/", views.resetPassword, name='resetPassword'),

    path("activate/<uidb64>/<token>/", views.activate, name='activate'),
    path("resetpassword_validate/<uidb64>/<token>/", views.resetpassword_validate, name='resetpassword_validate'),
    path("my_orders/", views.my_orders, name='my_orders'),
    path("edit_profile/", views.edit_profile, name='edit_profile'),
    path("changepassword/", views.changepassword, name='changepassword'),
    path("order_details/<int:order_id>/", views.order_details, name='order_details'),

]
