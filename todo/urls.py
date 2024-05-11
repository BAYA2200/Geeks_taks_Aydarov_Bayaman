from django.urls import path

from . import views
urlpatterns = [
    path('task/create/', views.TaskAPIView.as_view({'post': 'create'})),
    path('task/list/', views.TaskAPIView.as_view({'get': 'list'})),
    path('task/<int:pk>/detail/', views.TaskAPIView.as_view({'get': 'retrieve'})),
    path('task/<int:pk>/update/', views.TaskAPIView.as_view({'put': 'update'})),
    path('task/<int:pk>/delete/', views.TaskAPIView.as_view({'delete': 'destroy'})),
]
