"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import authorize_view, validate_view, secret_validate_view
from .services import router


app_name='ege_acesso'
urlpatterns = [
    path('', TemplateView.as_view(template_name="ege_acesso/acesso_errado.html",
                                  extra_context={'perfil_url': settings.LOGIN_REDIRECT_URL})),
    path('api/v1/', include(router.urls)),
    path('api/v1/secret/<str:secret>/', secret_validate_view),
    path('jwt/', TemplateView.as_view(template_name="ege_acesso/acesso_errado.html",
                                      extra_context={'perfil_url': settings.LOGIN_REDIRECT_URL}),
            ),
    path('jwt/authorize/', authorize_view, name='authorize_view'),
    path('jwt/validate/', validate_view, name='validate_view'),
]
