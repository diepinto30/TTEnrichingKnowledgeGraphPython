from django.conf.urls import url
from . import views

urlpatterns = [

    # url del manejo de roles
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout_view/$', views.logout_view, name="logout_view"),

    # url api data rdf/mxl

    url(r'^api/$', views.api, name="api"),
    url(r'^apiDataSemantic/$', views.apiDataSemantic, name="apiDataSemantic"),

    # url de registro de datos solo admin
    url(r'^registerData/$', views.registerData, name="registerData"),
    url(r'^registerDataSemantic/$', views.registerDataSemantic, name="registerDataSemantic"),

    # url de ner entitys (spacy traing)
    url(r'^ner_entity/$', views.ner_entity, name="ner_entity"),

]
