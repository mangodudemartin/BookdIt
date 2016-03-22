from django.conf.urls import url
from bookdit.controllers import homeController, authController

app_name = 'bookdit'
urlpatterns = [
    # /
    url(r'^$', homeController.index, name='index'),
    
    
    #-------------------------------------------------------------------------------------------------------------
    # AUTHENTICATION URLS
    #-------------------------------------------------------------------------------------------------------------
    url(r'^login/$', authController.vlogin, name='vlogin' ),
    # login/
    url(r'^login_request/$', authController.login_request, name='login_request'),
    # logout_view/
    url(r'^logout_request/$', authController.logout_request, name='logout_request'),
]
