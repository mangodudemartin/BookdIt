from django.conf.urls import url

from . import views
from bookdit.controllers import homeController

app_name = 'bookdit'
urlpatterns = [
    # /
    url(r'^$', homeController.index, name='index'),
    
    # login/
    url(r'^login_request/$', homeController.login_request, name='login_request'),
    # logout_view/
    url(r'^logout_view/$', homeController.logout_view, name='logout_view'),
]
