#
# from django.urls import path
#
# from .views import *
#
# urlpatterns = [
#
#     path('index/',index ,name='home'),
#     path('add_student/',add_student ,name='add_student'),
#     path('add_fan/',add_fan ,name='add_fan'),
#     path('generate_pdf/<int:student_id>/', generate_pdf, name='generate_pdf'),
# ]
#
#


from django.urls import path
from .views import (
    FanListView, FanDetailView, FanCreateView, FanUpdateView, FanDeleteView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    GeneratePDFView, index
)

urlpatterns = [
    # Bosh sahifa
    path('index/', index, name='home'),

    # Fan uchun URLlar
    path('fan/', FanListView.as_view(), name='fan_list'),
    path('fan/<int:pk>/', FanDetailView.as_view(), name='fan_detail'),
    path('add_fan/', FanCreateView.as_view(), name='add_fan'),
    path('fan/<int:pk>/update/', FanUpdateView.as_view(), name='fan_update'),
    path('fan/<int:pk>/delete/', FanDeleteView.as_view(), name='fan_delete'),

    # Student uchun URLlar
    path('student/', StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('add_student/', StudentCreateView.as_view(), name='add_student'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    # PDF generatsiya qilish uchun URL
    path('generate_pdf/<int:student_id>/', GeneratePDFView.as_view(), name='generate_pdf'),
]
