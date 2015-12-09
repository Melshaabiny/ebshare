from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.renderviewbook, name='viewbook'),
    #for passing parameters. Might need dir_name/(...
    url(r'^(?P<book_id>[0-9]+)$', views.renderviewbook, name='viewbook'),
    url(r'^reader/(?P<book_id>[0-9]+)$', views.renderreader, name='reader'),
    url(r'^purchase/(?P<book_id>[0-9]+)/(?P<price>[0-9]+)/(?P<seconds>[0-9]+)$', views.purchasebook, name='purchase'),
]
