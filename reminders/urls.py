from django.urls import path
from . import views

urlpatterns = [
    path('get_all/', views.ReminderListCreateAPIView.as_view(), name='get_all'),
    path('create/', views.ReminderListCreateAPIView.as_view(), name='create_reminder'),
    path('delete/<int:pk>/', views.ReminderListCreateAPIView.as_view(), name='delete_reminder'),
    path('update/<int:pk>/', views.ReminderListCreateAPIView.as_view(), name='update_reminder'),
    path('reminder_detail/<int:pk>/', views.ReminderDetailAPIView.as_view(), name='reminder-detail'),
    
    
    
]

