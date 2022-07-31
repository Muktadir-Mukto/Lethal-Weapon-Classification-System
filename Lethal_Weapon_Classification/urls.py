from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from Lethal_Weapon_Classification import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home_menu.urls')),
    path('admin/', admin.site.urls),
    path('SIGNUP_LOGIN/', include('SIGNUP_LOGIN.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('Classification/', include('Classification.urls')),
    path('Weapon/', include('Weapon.urls')),
    path('criminal/', include('Criminal.urls')),
    path('post/', include('post.urls')),





]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


