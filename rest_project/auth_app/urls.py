from django.urls import path
from . import views

app_name = 'auth_app'




urlpatterns = [
    path('', users_lc, name='users_lc'),
    path('<int>', users_rud, name='users_rud'),

]
