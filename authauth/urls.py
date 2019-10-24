from django.urls import path

from .views import MyLoginView, MyLogoutView, MyProfileView

app_name = 'authauth'

urlpatterns = [
	path('login/', MyLoginView.as_view(), name='login'),
	path('profile/', MyProfileView.as_view(), name='profile'),
	path('logout/', MyLogoutView.as_view(), name='logout'),
]