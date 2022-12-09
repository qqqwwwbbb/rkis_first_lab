from django.contrib import admin
from django.urls import include, path

from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/polls/', permanent=True)),
    path('polls/', include('polls.urls'), name='polls'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]