from django.urls import path
from . import views
from django.urls import path,include
from rest_framework import routers
from opuserfileupload.views import OperationUserViewSet

router = routers.DefaultRouter()
router.register("opsuser",OperationUserViewSet)

urlpatterns = [
   path("",include(router.urls)),
   path('upload/', views.upload_file, name='upload_file'),
   path('download/<int:file_id>/', views.download_file, name='download_file'),
]
