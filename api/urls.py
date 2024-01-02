
from django.contrib import admin
from django.urls import path
from .views import CurrenTimeView

urlpatterns = [
    path('time/', CurrenTimeView.as_view()),

]
