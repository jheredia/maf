from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.maf, name='maf'),
	url(r'^api/V1/femicidios/$', views.femicidios_list, name='femicidios_list'),
]