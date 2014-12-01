from django.conf.urls import patterns
from tastytools.views import doc, howto

urlpatterns = patterns('',
    (r'^doc', doc),
    (r'^howto', howto),
)
