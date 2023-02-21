from django.urls import path,include
from .views import createApplyleave,getApplyleave,getApplyleaveById,deleteApplyleave,updateApplyleave


urlpatterns = [

    path('create',  createApplyleave.as_view()),
    path('get', getApplyleave.as_view()),
    path('get/<str:id>', getApplyleaveById.as_view()),
    path('update/<str:id>', updateApplyleave.as_view()),
    path('delete/<str:id>', deleteApplyleave.as_view()),
    
]