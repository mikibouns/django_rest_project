from django.urls import path
from . import views

app_name = 'auth_app'


urlpatterns = [
    path('', views.UserListViewSet.as_view()),
    path('<int:pk>/', views.UserDetailViewSet.as_view()),

]
