from django.urls import path,include
from .views import createAdmDetail,getAdmDetail,getAdmDetailById,deleteAdmDetail,updateAdmDetail


urlpatterns = [

    path('create',  createAdmDetail.as_view()),
    path('get', getAdmDetail.as_view()),
    path('get/<str:id>', getAdmDetailById.as_view()),
    path('update/<str:id>', updateAdmDetail.as_view()),
    path('delete/<str:id>', deleteAdmDetail.as_view()),
    #path('applyleave/<str:id>',Applyleave.as_view())
]

