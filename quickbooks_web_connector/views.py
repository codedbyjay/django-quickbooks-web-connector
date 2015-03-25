from django.shortcuts import render, HttpResponse
from django.core.files.base import ContentFile
from django.template.loader import render_to_string
from django.conf import settings

from django_downloadview import VirtualDownloadView

class QWCDownloadView(VirtualDownloadView):

    def get_file(self):
        context = {
            "SITE_URL" : settings.SITE_URL,
            "QWC_APPLICATION_NAME" : settings.QWC_APPLICATION_NAME,
            "minutes" : 30
        }
        content = render_to_string("qwc.xml", context)
        return ContentFile(content, name='application.qwc')
    