from django.conf.urls import patterns, include, url
from django.contrib import admin

from quickbooks_web_connector.views import QWCDownloadView

urlpatterns = patterns('',
    # Examples:
    url(r'^qwc/', QWCDownloadView.as_view(), name='qwc'),
)
