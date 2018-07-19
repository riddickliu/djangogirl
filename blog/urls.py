from django.conf.urls import url
from .views import post_list

urlpatterns = [
    url(r'^$', post_list, name='post_list'),#去掉views.post_list
]