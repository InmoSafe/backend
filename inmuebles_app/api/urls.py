from django.urls import path
from inmuebles_app.api.views import ApCreate, ApUpdate, ApDelete, ApList, ApDetail

urlpatterns = [
    path('create/', ApCreate.as_view()),
    path('<int:pk>/update/', ApUpdate.as_view()),
    path('<int:pk>/delete/', ApDelete.as_view()),
    path('', ApList.as_view()),
    path('<int:pk>/', ApDetail.as_view()),
]
