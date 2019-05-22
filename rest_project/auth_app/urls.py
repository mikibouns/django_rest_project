from django.urls import path
from . import views

app_name = 'auth_app'


urlpatterns = [
    path('', views.UserViewSet.as_view(), name='users_lc'),
    path('<int:pk>', views.UserViewSet.as_view(), name='users_rud'),

]
