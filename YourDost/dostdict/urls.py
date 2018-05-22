from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.word_list, name='word_list'),
    url(r'^startswith/(?P<pk>[a-zA-Z]+)/$', views.starts_with, name='starting_with'),
    url(r'^addword/new/$',views.add_word,name='add_word'),
    url(r'^word/(?P<pk>\d+)/delete/$',views.word_delete,name='word_delete')

]
