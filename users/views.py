from users.forms import UserLoginForm, UserRegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
