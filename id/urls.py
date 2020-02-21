from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from .views import authorize_view, validate_view, secret_validate_view
from .views import index, acessibilidade, UserBiografyService, UserEmailService
from .services import router, UserBiografyService, UserEmailService

app_name = 'id'
urlpatterns = [
    path('', index, name='index'),
    path('acessibilidade/', acessibilidade, name='acessibilidade'),
    path(
        'jwt/', 
        include([
            path('authorize/', authorize_view, name='authorize_view'),
            path('validate/', validate_view, name='validate_view'),
        ])
    ),
    path('api/docs/', TemplateView.as_view(
        template_name='suap_ead/swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('api/v1/', include('id.urls_v1', namespace='api_v1'))
]
