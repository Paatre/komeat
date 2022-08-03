from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views


app_name = 'page'
urlpatterns = [
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
