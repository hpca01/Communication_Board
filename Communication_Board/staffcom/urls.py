"""Communication_Board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views as staff_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$', exp_view.home, name = 'home'),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^logout/$', auth_views.logout, name = 'logout'),
    url(r'^admin/', admin.site.urls),
    # basic default views first
    url(r'^inventory/$', staff_view.Inventory_View.as_view(), name = 'inventory'),
    url(r'^chemo/$', staff_view.View_with_PHI.as_view(commtype = 'Chemo'), name = 'chemo'),
    url(r'^ops/$', staff_view.View_with_PHI.as_view(commtype = 'Operation') , name = 'ops'),
    url(r'^homeiv/$', staff_view.View_with_PHI.as_view(commtype = 'HomeIV') , name = 'homeiv'),
    # methods to access details of a post
    url(r'^detail/(?P<pk>\d+)/$', staff_view.DetailPostView.as_view(), name = 'details'),
    # methods to deal with CRUD with objects for posts(communication) and comments
    url(r'^new_comm/$', staff_view.form_view, name ='add_communication'),
    url(r'^detail/(?P<pk>\d+)/comment$', staff_view.comment_view, name='comment_new'),
    url(r'^detail/(?P<pk>\d+)/update$', staff_view.UpdatePostView.as_view(), name='update_communication'),
    url(r'^detail/(?P<pk>\d+)/delete$', staff_view.DeletePostView.as_view(), name='delete_communication'),
    url(r'^search/$', staff_view.search_posts, name='search_view'),
]

