import datetime
from sc4py.env import env
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import User, Application
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help="My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('myip', nargs='+')

    def handle(self, *args, **options):
        if not settings.DEBUG:
            print("init_dev are project to dev environment")
            return

        su=User.objects.filter(is_superuser=True).first()
        if su is None:
            yn=input('do you wanna create a admin:admin superuser (y/N)?')
            if yn in ['Y', 'y']:
                su = User.objects.create(
                    username='admin',
                    cpf='12345678901',

                    active='Ativo',
                    is_staff=True,
                    is_superuser=True,

                    social_name='Social name',
                    first_name='First name',
                    last_name='Last name',

                    campus='Campus',
                    department='Department',
                    title='Officer',
                    carrer='Carrer',
                    job='Job',
                    polo='Polo',

                    course='Course name',
                    course_code='0000',

                    email='personal@email.com',
                    enterprise_email='enterprise@email.edu',
                    academic_email='academic@email.edu',
                    scholar_email='scholar@email.edu',

                    first_access=make_aware(datetime.datetime.now()),
                    last_access=make_aware(datetime.datetime.now()),
                    deleted=None,

                    created_at=make_aware(datetime.datetime.now()),
                    changed_at=make_aware(datetime.datetime.now()),
                    password_set_at=make_aware(datetime.datetime.now()),
                    last_access_at=make_aware(datetime.datetime.now()),

                    photo_url='https://suap.ifrn.edu.br/media/alunos/150x200/170685.jpg')
                su.set_password('admin')
                su.save()
                print("User created")

        if su is None:
            print("superuser dont exists")
            return

        allowed_callback_urls = ''
        allowed_web_origins = ''
        allowed_logout_urls = ''
        for host in ['sead', 'localhost'] + options['myip']:
            for service in ['acesso', 'dashboard', 'perfil']:
                allowed_callback_urls += 'http://%s/sead/%s/jwt/complete/\n' % (host, service)
                allowed_web_origins += 'http://%s/sead/%s/jwt/login/\n' % (host, service)
                allowed_logout_urls += 'http://%s/sead/%s/jwt/logout/\n' % (host, service)

        app = Application.objects.filter(client_id=env('SUAP_EAD_ACESSO_JWT_CLIENT_ID'),
                                         secret=env('SUAP_EAD_ACESSO_JWT_SECRET')).first()
        if app is None:
            print("creating app...\n")
            app = Application()
        else:
            print("application always exists\n")

        app.owner = su
        app.name = 'SUAP_EAD_acesso'
        app.description = 'some description'
        app.client_id = env('SUAP_EAD_ACESSO_JWT_CLIENT_ID')
        app.secret = env('SUAP_EAD_ACESSO_JWT_SECRET')
        app.logo = None
        app.allowed_callback_urls = allowed_callback_urls
        app.allowed_web_origins = allowed_web_origins
        app.allowed_logout_urls = allowed_logout_urls
        app.expiration = 600
        app.created_at = datetime.datetime.now()
        app.deleted_at = None
        app.save()

        print("application client_id=%s" % env('SUAP_EAD_ACESSO_JWT_CLIENT_ID'))
        print("application secret=%s" % env('SUAP_EAD_ACESSO_JWT_SECRET'))
        print("\nDone.")
