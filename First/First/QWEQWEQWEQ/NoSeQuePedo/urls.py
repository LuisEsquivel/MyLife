from django.conf.urls import url
from First.QWEQWEQWEQ.NoSeQuePedo import views
from First.QWEQWEQWEQ.NoSeQuePedo.views import profileInfo

urlpatterns = [
    url(r'^$', views.home, name='inicio'),
    url(r'^$', views.welcome, name='welcome'),
    url('login/(?P<email>\d+)/(?P<pswd>\.+)/$', views.login),
    url('^buscar/$', views.buscar, name='buscar'),
    url('^messages/$', views.mensajes, name='messages'),
    url('^send/$', views.enviar, name='send'),
    url('^profile/$', profileInfo.as_view(), name='profile'),
    url('^delete/$', views.eliminarPublicacion, name='delete'),

]
