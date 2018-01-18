from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.ServiceProviderCreateView.as_view(), name='serviceprovider_create'),
    url(r'^(?P<pk>\d+)/$', views.ServiceProviderDetailView.as_view(), name='serviceprovider_detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ServiceProviderUpdateView.as_view(), name='serviceprovider_update'),
]