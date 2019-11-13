# encoding: utf-8
"""
@version: 1.0
@author: 
@file: urls
@time: 2019-10-29 22:54
"""

from django.urls import path, re_path
from rest_api.views import LinkView, VisitView

urlpatterns = [
    path('', LinkView.as_view()),
    re_path('(?P<uid>\w+)', VisitView.as_view())
]