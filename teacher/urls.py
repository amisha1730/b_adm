from django.urls import include, path
from . import views
from .views import AddTeacher,UpdateTeacher
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register',  AddTeacher.as_view()),
    path('update/<str:id>', UpdateTeacher.as_view()),
]

