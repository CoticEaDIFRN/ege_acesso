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
import datetime
import jwt
from urllib.parse import urlparse, unquote_plus
import uuid
import hashlib
from django.utils.translation import gettext_lazy as _
from django.db.models import Model, ForeignKey, ManyToManyField, CASCADE
from django.db.models import CharField, DateTimeField, BooleanField, TextField, PositiveIntegerField, \
                             SmallIntegerField, FileField, NullBooleanField
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import make_aware
from python_brfied import to_choice
import ege_theme


def _cast_timestamp(old):
    if old is None or not isinstance(old, str):
        return old
    try:
        return make_aware(datetime.datetime.strptime(old, '%Y%m%d%H%M%S.0Z'))
    except ValueError as e:
        try:
            return make_aware(datetime.datetime.strptime(old, '%d/%m/%Y %H:%M'))
        except ValueError as e:
            return None


def url_only(full_url):
    return full_url.replace('?%s' % urlparse(full_url).query, '')


def validate_url(url, urls_string):
    urls = [url_only(x)
            for x in urls_string.replace('\r', '').split('\n')
            if x.strip()]
    return url_only(url) in urls


class SpecialNeed(Model):
    VISION = _('Visão')
    AUDITION = _('Audição')
    OTHERS = _('Outras')
    CHOICES = to_choice(VISION, AUDITION, OTHERS)

    name = CharField(_('name'), max_length=250, blank=False, null=False)
    category = CharField(_('category'), max_length=250, choices=CHOICES, blank=False, null=False)

    class Meta:
        verbose_name = _('special need')
        verbose_name_plural = _('special needs')

    def __str__(self):
        return "%s (%s)" % (self.name, self.category)


class User(AbstractUser):
    username = CharField(_('username'), max_length=150, primary_key=True)
    cpf = CharField(_('cpf'), max_length=255, null=True, blank=True)

    is_active = BooleanField(_('is active'), default=True)
    is_staff = BooleanField(_('staff status'), default=False)
    is_superuser = BooleanField(_('superuser status'), default=False)
    active = CharField(_('active'), max_length=255, null=True, blank=True)

    presentation_name = CharField(_('presentation name'), max_length=255, null=True, blank=True)
    civil_name = CharField(_('civil name'), max_length=255, null=True, blank=True)
    social_name = CharField(_('social name'), max_length=255, null=True, blank=True)
    first_name = CharField(_('first name'), max_length=255, null=True, blank=True)
    last_name = CharField(_('last name'), max_length=255, null=True, blank=True)

    campus = CharField(_('campus'), max_length=255, null=True, blank=True)
    campus_code = CharField(_('campus code'), max_length=255, null=True, blank=True)
    department = CharField(_('department'), max_length=255, null=True, blank=True)
    title = CharField(_('title'), max_length=255, null=True, blank=True)
    carrer = CharField(_('carrer'), max_length=255, null=True, blank=True)
    job = CharField(_('job'), max_length=255, null=True, blank=True)
    polo = CharField(_('polo'), max_length=255, null=True, blank=True, default=_('unknown'))
    polo_code = CharField(_('polo code'), max_length=255, null=True, blank=True)

    course = CharField(_('course'), max_length=255, null=True, blank=True)
    course_code = CharField(_('course code'), max_length=255, null=True, blank=True)

    email = CharField(_('personal mail'), max_length=250, null=True, blank=True)
    enterprise_email = CharField(_('enterprise email'), max_length=250, null=True, blank=True)
    academic_email = CharField(_('academic email'), max_length=250, null=True, blank=True)
    scholar_email = CharField(_('scholar email'), max_length=250, null=True, blank=True)

    first_access = DateTimeField(_('date joined'), auto_now_add=True)
    last_access = DateTimeField(_('last access'), auto_now=True)
    deleted = DateTimeField(_('deleted at'), null=True, blank=True)

    created_at = DateTimeField(_('created at'), null=True, blank=True)
    changed_at = DateTimeField(_('changed at'), null=True, blank=True)
    password_set_at = DateTimeField(_('password set at'), null=True, blank=True)
    last_access_at = DateTimeField(_('last ad access'), null=True, blank=True)

    photo_url = CharField(_('photo'), max_length=250, null=True, blank=True)

    biografy = TextField(_('biografy'), blank=True, null=True)
    is_biografy_public = TextField(_('show to all'), blank=True, null=True)

    valid_photo = FileField(_('valid photo'), null=True, blank=True)
    pending_photo = FileField(_('pending photo'), null=True, blank=True)
    photo_solicitation_at = DateTimeField(_('photo_solicitation_at'), blank=True, null=True)
    photo_approved_at = DateTimeField(_('photo_approved at'), blank=True, null=True)
    photo_approved_by = CharField(_('photo_approved by'), max_length=250, blank=True, null=True)

    font_size = SmallIntegerField(_('font size'), blank=True, null=True)
    theme_skin = CharField(_('theme skin'), choices=ege_theme.skins, max_length=250, blank=True, null=True)
    legends = NullBooleanField(_('legends'), blank=True, null=True)
    sign_language = NullBooleanField(_('sign language'), blank=True, null=True)
    screen_reader = NullBooleanField(_('screen reader'), blank=True, null=True)

    special_needs = ManyToManyField(SpecialNeed, verbose_name=_('special needs'))
    is_special_needs_public = NullBooleanField(_('show to all'))

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['first_name']

    def __str__(self):
        return self.printing_name

    def save(self, *args, **kwargs):
        self.is_active = 'Ativo' == self.active

        self.created_at = _cast_timestamp(self.created_at)
        self.changed_at = _cast_timestamp(self.changed_at)
        self.password_set_at = _cast_timestamp(self.password_set_at)
        self.last_access_at = _cast_timestamp(self.last_access_at)

        self.email = self.email or self.enterprise_email or self.academic_email or self.scholar_email

        self.civil_name = "%s %s" % (self.first_name, self.last_name)
        self.presentation_name = self.social_name or self.civil_name

        super().save(*args, **kwargs)

    @property
    def printing_name(self):
        if self.social_name and self.social_name != self.civil_name:
            return "%s (%s)" % (self.social_name, self.civil_name)
        return self.civil_name

    @property
    def status(self):
        result = ""
        result += "%s " % (_("active") if self.is_active else _("inactive"))
        if self.is_superuser:
            result += "(%s" % _("superuser")
            if not self.is_staff:
                result += " %s" % _("but not a staff")
            result += ")"
        elif self.is_staff:
            result += "(%s)" % _("staff")
        else:
            result += "(%s)" % _("user")
        return result


class Application(Model):
    owner = ForeignKey(verbose_name=_('owner'), to=User, on_delete=CASCADE)
    name = CharField(_('name'), max_length=150)
    description = TextField(_('description'), null=True, blank=True)
    client_id = CharField(_('client_id'), max_length=150)
    secret = CharField(_('client_secret'), max_length=150)
    logo = FileField(_('application_logo'), null=True, blank=True)
    allowed_callback_urls = TextField(_('allowed_callback_urls'), null=True, blank=True)
    allowed_web_origins = TextField(_('allowed_web_origins'), null=True, blank=True)
    allowed_logout_urls = TextField(_('allowed_logout_urls'), null=True, blank=True)
    expiration = PositiveIntegerField(_('expiration_in_seconds'), default=300)
    created_at = DateTimeField(_('when_created'), auto_now_add=True)
    deleted_at = DateTimeField(_('deleted_at'), null=True, blank=True)

    class Meta:
        verbose_name = _('Aplicação')
        verbose_name_plural = _('Aplicações')

    def __str__(self):
        return "%s [%s]" % (self.name, self.owner)

    def save(self, *args, **kwargs):
        if self.client_id is None or self.client_id == '' or self.secret is None or self.secret == '':
            self.client_id = hashlib.sha1(("%s" % uuid.uuid1()).encode('utf-8')).hexdigest()
            self.secret = hashlib.sha3_512(("%s" % uuid.uuid1()).encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

    @staticmethod
    def authorize(user, client_id, state, redirect_uri, referer):
        app = Application.validate_client_id(client_id)

        try:
            state = jwt.decode(state, app.secret, algorithm='HS512')
        except Exception as e:
            raise Exception("Invalid 'state'")
        assert 'client_id' in state, "state invalid encoded, client_id not present"
        assert 'uuid' in state, "state invalid encoded, uuid not present"

        # if referer is not None:
        #     referer = referer
        #     assert app.allowed_web_origins is None and validate_url(referer.split("?")[0], app.allowed_web_origins), \
        #         "'referer (%s)' not present on '%s (%s)'" % (referer.split("?")[0],
        #                                                     _('allowed_web_origins'),
        #                                                      app.allowed_web_origins)

        redirect_uri = unquote_plus(redirect_uri)

        assert validate_url(redirect_uri, app.allowed_callback_urls), \
            "'redirect_uri' not present on '%s' - %s" % (_('allowed_callback_urls'), url_only(redirect_uri))

        expire_at = make_aware(datetime.datetime.now() + datetime.timedelta(minutes=10))

        hashcode = "%s" % uuid.uuid1()
        TransactionToken.objects.create(application=app,
                                        user=user,
                                        hashcode=hashcode,
                                        state=state,
                                        redirect_uri=redirect_uri,
                                        referer=referer,
                                        expire_at=expire_at)
        return hashcode

    @staticmethod
    def validate_client_id(client_id):
        try:
            return Application.objects.get(client_id=client_id, deleted_at__isnull=True)
        except Exception as e:
            raise Exception("Invalid 'client_id'")


class TransactionToken(Model):
    application = ForeignKey(verbose_name=_('application'), to=Application, on_delete=CASCADE)
    user = ForeignKey(verbose_name=_('user'), to=User, on_delete=CASCADE)
    hashcode = TextField(_('hash'))
    state = TextField(_('state'))
    redirect_uri = TextField(_('redirect_uri'))
    referer = TextField(_('referer'), null=True, blank=True)
    expire_at = DateTimeField(_('expireAt'))

    class Meta:
        verbose_name = _('Token de transação')
        verbose_name_plural = _('Tokens de transações')

    def __str__(self):
        return "%s - %s - %s" % (self.hashcode, self.application, self.expire_at)

    def generate_jwt(self):
        data = {
            'username': self.user.username,
            'cpf': self.user.cpf,

            'is_active': self.user.is_active,
            'active': self.user.active,
            'status': self.user.status,

            'presentation_name': self.user.presentation_name,
            'civil_name': self.user.civil_name,
            'social_name': self.user.social_name,

            'campus': self.user.campus,
            'department': self.user.department,
            'title': self.user.title,
            'carrer': self.user.carrer,
            'job': self.user.job,
            'polo': self.user.polo,

            'course': self.user.course,
            'course_code': self.user.course_code,

            'personal_email': self.user.email,
            'enterprise_email': self.user.enterprise_email,
            'academic_email': self.user.academic_email,
            'scholar_email': self.user.scholar_email,

            'first_access': "%s" % self.user.first_access,
            'last_access': "%s" % self.user.last_access,
            'deleted': "%s" % self.user.deleted,

            'created_at': "%s" % self.user.created_at,
            'changed_at': "%s" % self.user.changed_at,
            'password_set_at': "%s" % self.user.password_set_at,
            'last_access_at': "%s" % self.user.last_access_at,

            'photo_url': self.user.photo_url,

            'biografy': self.user.biografy,
            'is_biografy_public': self.user.is_biografy_public,

            # 'valid_photo': self.user.valid_photo,
            # 'pending_photo': self.user.pending_photo,
            'photo_solicitation_at': self.user.photo_solicitation_at,
            'photo_approved_at': self.user.photo_approved_at,
            'photo_approved_by': self.user.photo_approved_by,

            'font_size': self.user.font_size,
            'theme_skin': self.user.theme_skin,
            'legends': self.user.legends,
            'sign_language': self.user.sign_language,
            'screen_reader': self.user.screen_reader,

            'special_needs': [x for x in self.user.special_needs.all()],
            'is_special_needs_public': self.user.is_special_needs_public,
        }
        return jwt.encode(data, self.application.secret, algorithm='HS512')

    @staticmethod
    def validate(client_id, auth_token):
        application = Application.validate_client_id(client_id)
        transaction_token = TransactionToken.objects.select_related('application').\
            get(application=application, hashcode=auth_token, expire_at__gt=make_aware(datetime.datetime.now()))
        # transaction_token.delete()
        return transaction_token.generate_jwt()
