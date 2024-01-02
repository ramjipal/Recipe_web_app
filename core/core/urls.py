"""
URL configuration for core project.

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
from vege.views import *
from django.conf.urls.static import static     #for image
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name = "receipes"),
    path('del-recipe/<id>/', delRecipe, name = "delrecipe"),
    path('up-recipe/<id>', upRecipe, name = "upRecipe"),
    path('user_register/', register_page, name = 'register_page'),
    path('user_login/', login_page, name = 'login_page'),
    path('user_logout/', logout_page, name = 'logout'),
    path('', login_page, name = "login_page")
]

if settings.DEBUG:    #for image
        urlpatterns += static(settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()
