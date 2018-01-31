from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$$', views.snippet_detail),
]

urpatterns = format_suffix_patterns(urlpatterns)