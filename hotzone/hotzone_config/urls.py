"""hotzone_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from case_record.views import CaseRecordAPI
from visited_location.views import CreateVisitedLocationAPI, CreateVisitedLocationView
from case_record.views import CreateCaseRecordView, CreateCaseRecordAPI, IndexView
from virus.views import CreateVirusView, CreateVirusAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', include('locations.urls')),
    path('create_caserecord_post/', CaseRecordAPI.as_view(),name='create_caserecord_post'),
    path('create_visitedlocation_post/', CreateVisitedLocationAPI.as_view(),name='create_visitedlocation_post'),
    path('create_caserecord/', CreateCaseRecordView.as_view(), name="create_caserecord"),
    path('post_caserecord/', CreateCaseRecordAPI.as_view(),name="post_caserecord"),
    path('create_virus/', CreateVirusView.as_view(), name='create_virus'),
    path('post_create_virus/', CreateVirusAPI.as_view(), name='post_create_virus'),
    path('', IndexView.as_view(), name='index'),
    path('create_visitedlocation/', CreateVisitedLocationView.as_view(), name='create_visitedlocation')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
