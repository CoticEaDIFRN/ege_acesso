from django.contrib.auth.backends import ModelBackend
from django_python3_ldap import ldap


class LDAPBackend(ModelBackend):
    supports_inactive_user = False

    def authenticate(self, *args, **kwargs):
        result = ldap.authenticate(*args, **kwargs)
        return result
