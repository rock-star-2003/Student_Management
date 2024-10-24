from django.urls import path
from .views import *
urlpatterns = [


    path('login/', login_user, name='login'),
    path('', index, name='index'),
    path('edit_profile/<int:id>/', edit_profile, name='edit_profile'),
    path("fee_payment/<int:id>/", fee_payment, name="fee_payment"),
    path('leave_letter/<int:id>/', leave_letter, name='leave_letter'),
    path('view_student/<int:id>/',view_student,name="view_student"),
    path('update_attendance/',update_attendance,name="update_attendance"),
    path('update_attendance_status/', update_attendance_status, name='update_attendance_status'),

]