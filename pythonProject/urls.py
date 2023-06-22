"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import app.views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', app.views.login, name='login'),
    path('register/', app.views.register, name='register'),
    path('main/', app.views.main, name='main'),
    path('permission/', app.views.getPermisson, name="getPermisson"),
    path('select/name/', app.views.selectName, name='select_name'),
    path('select/address/', app.views.selectAddress, name='select_address'),
    path('select/specialize/', app.views.selectSpecialize, name='select_specialize'),
    path('getSpecialize/', app.views.getSpecialize, name="get_specialize"),
    path('addcontact/', app.views.addContact, name="addcontact"),
    path('updateContact/', app.views.upadteContact, name="updatecontact"),
    path("delcontact/", app.views.delContact, name="delcontact")
]
