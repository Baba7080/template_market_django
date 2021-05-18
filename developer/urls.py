from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('',devloper_home_view,name=''),
    path('detail/<int:pk>/',detail_view.as_view(),name='detail'),# detailveiws
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
