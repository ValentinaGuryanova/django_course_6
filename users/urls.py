from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.apps import UsersConfig
from users.services import generate_new_password, verify_view
from users.views import LoginView, LogoutView, RegisterView, ProfileView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('verifying/', verify_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


