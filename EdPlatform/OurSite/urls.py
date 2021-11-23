from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from .views import HomePageView
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.post_list, name='post_list'),
     # path('add/', views.add_list, name='add_list'),
    path('add/', views.HomePageView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', RedirectView.as_view(pattern_name="index")),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)