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
from django.urls import path
from apps.crud1_using_api_decorator import views as way1
from apps.crud2_using_APIView import views as way2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/", way1.student_api),
    path("studentapi/<int:pk>/", way1.student_api),
    path("apiview_studentapi/", way2.StudentAPI.as_view()),
    path("apiview_studentapi/<int:pk>/", way2.StudentAPI.as_view()),
]
