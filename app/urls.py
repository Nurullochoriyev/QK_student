
from django.urls import path

from .views import *

urlpatterns = [

    path('index/',index ,name='home'),
    path('add_student/',add_student ,name='add_student'),
    path('add_fan/',add_fan ,name='add_fan'),
    path('generate_pdf/<int:student_id>/', generate_pdf, name='generate_pdf'),
]





