# coding: UTF-8

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views


from home import views as home_views 

urlpatterns = patterns('',
         # Activation keys get matched by \w+ instead of the more specific
         # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
         # that way it can return a sensible "invalid key" message instead of a confusing 404
					   url(r'^$', home_views.home_view),

        )
