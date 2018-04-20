"""First URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from First.QWEQWEQWEQ.NoSeQuePedo import views
from First.QWEQWEQWEQ.NoSeQuePedo.views import publicaciones, profileInfo


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('First.QWEQWEQWEQ.NoSeQuePedo.urls')),
    url(r'^inicio', include('First.QWEQWEQWEQ.NoSeQuePedo.urls')),
    url(r'^nuevo/$',views.añadirUsers, name="registrar"),
    url('^login/$',views.login, name='login'),
    url('^buscar/$', views.buscar, name='buscar'),
    url('^publicar/$', views.publicar, name='publicar'),
    url(r'^welcome$',publicaciones.as_view(), name='welcome'),
    url('^messages/$', views.mensajes, name='messages'),
    url('^send/$', views.enviar, name='send'),
    url('^profile/$', profileInfo.as_view(), name='profile'),
    url('^profile/subirImagen/$', views.subirImagen, name='imagen'),
    url('^solicitudes/$', views.solicitudes),
    url('^logout/$', views.logout),
    url('^profile/EditProfile/$', views.editprofile),
    url('^profile/EditProfile/Confirm$', views.confirmEdit, name="ConfirmEdit"),
    url('^delete/$', views.eliminarPublicacion, name='delete'),
]
