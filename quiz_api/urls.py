from django.urls import path, include

from .views import *
from . import routers

urlpatterns = [
    path('answer/', AnswerOnTestProcedureAPIView.as_view(), name='answer'),
] + routers.urlpatterns

