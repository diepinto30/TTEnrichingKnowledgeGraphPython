from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from portal import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    path('portal/', include('portal.urls')),
    url(r'^admin/', admin.site.urls),
]
