"""
project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from online_grocery import views
from django.contrib.auth import views as g

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="hm"),
    path('',views.showslides),
    path('abt/',views.about,name="ab"),
    path('vege/',views.vegetables,name="veg"),
    path('fru/',views.fruits,name="fit"),
    path('da/',views.dairy,name="day"),
    path('pu/',views.pulses,name="pul"),
    path('ho/',views.house,name="hom"),
    path('po/',views.care,name="car"),
    path('ca/',views.cart,name="cat"),
    path('cnt/',views.contact,name="ct"),
    path('rg/',views.register,name="reg"),
    path('pf/',views.prfle,name="pfe"),
    path('upf/',views.updf,name="upfe"),
    path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
    path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]
