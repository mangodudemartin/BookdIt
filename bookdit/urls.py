from django.conf.urls import url
from django.contrib import admin
from bookdit.controllers import homeController, authController

app_name = 'bookdit'
urlpatterns = [
    # /
    url(r'^$', homeController.index, name='index'),
    url(r'^home/', homeController.home, name='home'),
    url(r'^admin/', admin.site.urls),
    
    
    #-------------------------------------------------------------------------------------------------------------
    # AUTHENTICATION URLS
    #-------------------------------------------------------------------------------------------------------------
    url(r'^register/$', authController.register, name='register'),
    url(r'^login/$', authController.vlogin, name='vlogin' ),
    # login/
    url(r'^login_request/$', authController.login_request, name='login_request'),
    # logout_view/
    url(r'^logout_request/$', authController.logout_request, name='logout_request'),
]
