from django.urls import path
import app.views
urlpatterns = [
               path('students/', app.views.student_collection),
               path('students/<int:pk>/', app.views.student_record),
               ]

