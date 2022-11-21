from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('response/', views.Response, name="response"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('form/', views.DataPOST, name="form"),
    # Function Based View
    # path('student/', views.StudentList, name="student"),
    # Class Based View
    path('student/', views.StudentList.as_view(), name="student"),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)