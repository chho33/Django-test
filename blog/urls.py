from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^(?P<key>\d+)',views.post_record, name='post_record'),
    url(r'^add_record', views.add_record, name="add_record"),
    url(r'^delete/(\d+)', views.delete_record, name="delete_record"),

]
