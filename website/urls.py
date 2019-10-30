from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home_projects, name='homePage'),
    url(r'^search/', views.search_projects, name='search_projects'),
    url(r'^image(\d+)', views.project, name='project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^profile$', views.edit_profile, name='edit_profile'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^project$', views.project_list, name='project_list'),
    url(r'^profile/(?P<username>[0-9]+)$',views.profile, name='profile'),
        
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)