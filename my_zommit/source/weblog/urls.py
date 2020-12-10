"""weblog URL Configuration

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
    2. Add a URL to urlpatterns:  path('weblog/', include('weblog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from author.views import signup, login_view
from post.views import post_list, home, post_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',post_list),
    path('home/',home,name='home'),
    path('post/<int:pk>',post_details,name="post_detail"),
    path('register/',signup,name='signup'),
    path('login/',login_view,name='login')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
