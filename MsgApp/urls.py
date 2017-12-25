
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.users, name='users'),

    url(r'^(?P<user_id>[0-9]+)/$', views.message, name='message'),

    url(r'^(?P<user_id>[0-9]+)/send/$', views.send, name='send'),

    url(r'^(?P<user_id>[0-9]+)/logout/$', views.logout_view, name='logout_view'),

    url(r'^', include('django.contrib.auth.urls')),

]

# URL -> FUNCTION -> TEMPLATE (HTML)
