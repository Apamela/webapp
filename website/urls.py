from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.home_projects,name = 'homepage'),
    url(r'^profile$',views.profile, name='profile'),
    url(r'^search/',views.search_projects,name='search_projects'),
    url(r'^project$',views.project_list,name= 'project_list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

