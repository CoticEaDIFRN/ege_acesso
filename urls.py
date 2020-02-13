from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import urls


urlpatterns = [
    path(
        settings.URL_PATH_PREFIX,
        include(
            [
                path('admin/', admin.site.urls),
                path('', include('django.contrib.auth.urls')),
                path('', include('acesso.urls', namespace='api_v1')),
                # path('api-auth/', include('rest_framework.urls')),
                # path('logout/', jwt_logout, name='logout'),
                # path('', include('suap_ead.urls', namespace='suap_ead')),
            ]
        )
    ),
    path('', RedirectView.as_view(url=settings.LOGIN_REDIRECT_URL)),
    # path('', RedirectView.as_view(url=settings.URL_PATH_PREFIX)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('%s__debug__/' % settings.URL_PATH_PREFIX, include(debug_toolbar.urls)))
