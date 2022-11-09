from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView

from accounts.decorators import required_access
from mbb_sacco import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', required_access(function=TemplateView.as_view(template_name="index.html"), login_url=reverse_lazy('accounts:login'), user_type="CM"), name="index"),
    path('', include('accounts.urls')),
    path('', include('store.urls')),
    path('', include('loans.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
