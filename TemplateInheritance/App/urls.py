from django.conf.urls import url
from App import views

#Template Tagging
app_name = 'App'

urlpatterns = [
    url(r'^base/$',views.base,name='base'),
    url(r'^other/$',views.other,name='other'),
]
