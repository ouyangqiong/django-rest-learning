from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$$', views.SnippetDetail.as_view()),
]

urpatterns = format_suffix_patterns(urlpatterns)
