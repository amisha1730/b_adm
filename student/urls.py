from django.urls import include, path
from . import views
from .views import  addStudent , UpdateStudent
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('add',addStudent.as_view()),  
    path('update/<str:id>',UpdateStudent.as_view())
]


