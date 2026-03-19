from django.urls import include, path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register_view,name='register_view'),
    path('logout/',views.login_view,name='logout_view'),
]