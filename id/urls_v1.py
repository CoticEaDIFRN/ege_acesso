from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from rest_framework_swagger.views import get_swagger_view
from .views import authorize_view, validate_view, secret_validate_view
from .views import AcessibilidadeService, UserBiografyService, UserEmailService
from .services import router, UserBiografyService, UserEmailService
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

app_name = 'api_v1'
urlpatterns = [
    path('', include(router.urls)),
    path('sw/', schema_view),
    path('redoc/', TemplateView.as_view(
        template_name='suap_ead/redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    # path('docs/', get_swagger_view(title='Pastebin API')),
    path(
        'me/', 
        include([
            path('acessibilidade', AcessibilidadeService, name='acessibilidade'),
            path('biografy/', csrf_exempt(UserBiografyService.as_view())),
            path('email/', csrf_exempt(UserEmailService.as_view())),
        ])
    ),
    path(
        'users/', 
        include([
            path('<str:username>/biografy/', csrf_exempt(UserBiografyService.as_view())),
            path('<str:username>/email/', csrf_exempt(UserEmailService.as_view())),
        ])
    ),
    path(
        'gateway_api/', 
        include([
            path('secret/<str:secret>/', secret_validate_view),
        ])
    ),
    path('secret/<str:secret>/', secret_validate_view),
]
