from django.views.generic import TemplateView

# Create your views here.

class LoginView(TemplateView):
	tempate_name = 'authauth/login.html'

