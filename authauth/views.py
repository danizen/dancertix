from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class MyLoginView(TemplateView):
	template_name = 'authauth/login.html'


class MyLogoutView(LogoutView):
	pass


@method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):
	template_name = 'authauth/profile.html'
