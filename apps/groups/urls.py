from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.ListGroups.as_view(), name='all'),
    url(r'^new/$', views.CreateGroup.as_view(), name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(),
        name='single'),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
    url(r"update/(?P<slug>[-\w]+)/$",views.UpdateGroup.as_view(),name="update"),
    url(r"delete/(?P<slug>[-\w]+)/$",views.DeleteGroup.as_view(),name="delete"),

]
