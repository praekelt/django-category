from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^tree/$', 'category.admin_views.tree'),
)
