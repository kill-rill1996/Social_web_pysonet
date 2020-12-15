from django.urls import path

from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.GetUserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserNetPublicView.as_view({'get': 'retrieve'})),

]