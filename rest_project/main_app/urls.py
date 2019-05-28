from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.APIRootView.as_view(), name='main_app'),
    # path('api_doc', )
]
