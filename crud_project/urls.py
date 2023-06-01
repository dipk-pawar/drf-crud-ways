"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.crud1_using_api_decorator import views as way1
from apps.crud2_using_APIView import views as way2
from apps.crud3_using_genetic_api_vew_and_mixins import views as way3
from apps.crud4_using_concrete_views import views as way4
from apps.crud5_using_viewsets import views as way5
from apps.crud6_using_model_viewsets import views as way6
from apps.crud7_using_serializers import views as way7

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register("way5_studentapi", way5.StudentViewSet, basename="student_way5")
router.register("way6_studentapi", way6.StudentModelViewSet, basename="student_way6")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("way1_studentapi/", way1.student_api),
    path("way1_studentapi/<int:pk>/", way1.student_api),
    path("way2_studentapi/", way2.StudentAPI.as_view()),
    path("way2_studentapi/<int:pk>/", way2.StudentAPI.as_view()),
    path("way3_studentapi/", way3.ListandCreateStudentAPI.as_view()),
    path("way3_studentapi/<int:pk>/", way3.ReadUpdateDeleteStudentAPI.as_view()),
    path("way4_studentapi/", way4.StudentListCreate.as_view()),
    path("way4_studentapi/<int:pk>/", way4.StudentRetrieveUpdateDestroy.as_view()),
    path("way7_studentapi/", way7.StudentAPI.as_view()),
    path("", include(router.urls)),
]
