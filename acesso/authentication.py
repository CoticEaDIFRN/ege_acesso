from django.utils.translation import ugettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .models import Application


class ApplicationSecretAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Secret ".  For example:

        Authorization: Secret 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Secret'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].decode() != self.keyword:
            return None

        if len(auth) == 1:
            msg = _('Invalid secret header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid secret header. Secret string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Secret string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, secret):
        try:
            application = Application.objects.select_related('owner').get(secret=secret)
        except Application.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid secret.'))

        if application.deleted_at is not None:
            raise exceptions.AuthenticationFailed(_('Application not exists'))

        if not application.owner.is_active or application.owner.deleted is not None:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return application.owner, application

    def authenticate_header(self, request):
        return self.keyword
