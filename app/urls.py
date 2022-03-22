from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/jobs', views.NewsList.as_view()),
    path('api/jobs/<id>', views.NewsDescription.as_view()),
    path('api/auth', obtain_auth_token)
]
