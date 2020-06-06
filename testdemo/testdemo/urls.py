"""testdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/',admin.site.urls ),
    url(r'^$',views.index,name='index'),
    url(r'^HOME',views.home1,name='home1'),
    url(r'^add_record/$',views.add_record,name='add_record'),
    url(r'^update_record/$',views.update_record,name='update_record'),
    url(r'^update_record_save/$',views.update_record_save,name='update_record_save'),
    url(r'^Search/$',views.search,name="search"),
    # url(r'^search_fetch/$',views.search_fetch,name="search_fetch"),
    url(r'^Delete/$',views.Delete,name='Delete'),

]
