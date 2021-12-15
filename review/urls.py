from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('review/add/', ReviewCreateView.as_view(), name='review-add'),
    path('review/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
