from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.apps import UserConfig
from users.views import LoginView, LogoutView, RegisterUserView, ProfileView

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile_info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)