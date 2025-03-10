"""
URL configuration for ges_project project.

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

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from ges_project import settings
from main.views import IndexHandler

urlpatterns = [
    path('admin/', admin.site.urls),


    url(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }),

    path('',IndexHandler)

]
"""

"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from ges_project import settings
from django.shortcuts import redirect
from django.urls import path

urlpatterns = [
    path('', lambda request: redirect('admin/')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),
]
"""


from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from ges_project import settings
from main.views import IndexHandler  # İndexHandler'ın doğru import edilmesi

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin paneli yolu

    # Medya dosyalarını sunmak için doğru URL yapısını kullanın
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    # Anasayfa URL'si, IndexHandler sınıfını fonksiyon tabanlı view olarak kullanıyorsanız:
    path('', IndexHandler),  # IndexHandler burada fonksiyon tabanlı view olarak kullanılırsa
]