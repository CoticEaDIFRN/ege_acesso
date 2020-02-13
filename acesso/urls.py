from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import authorize_view, validate_view, secret_validate_view
from .services import router, UserBiografyService, UserEmailService
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt


app_name = 'acesso'
urlpatterns = [
    # path('', TemplateView.as_view(template_name="acesso/acesso_errado.html",
    #                               extra_context={'perfil_url': settings.LOGIN_REDIRECT_URL})),
    path('', RedirectView.as_view(url="..")),
    path('', RedirectView.as_view(url=settings.URL_PATH_PREFIX)),
    path('api/v1/', include(router.urls)),
    path('api/v1/users/<str:username>/biografy/', csrf_exempt(UserBiografyService.as_view())),
    path('api/v1/users/<str:username>/email/', csrf_exempt(UserEmailService.as_view())),
    path('api/v1/secret/<str:secret>/', secret_validate_view),
    path('jwt/', TemplateView.as_view(template_name="acesso/acesso_errado.html",
                                      extra_context={'perfil_url': settings.LOGIN_REDIRECT_URL})),
    path('jwt/authorize/', authorize_view, name='authorize_view'),
    path('jwt/validate/', validate_view, name='validate_view'),
]
