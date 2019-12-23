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
from sc4py.env import env
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import User, Application
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help="My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

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

        aa = Application.objects.filter(client_id=env('EGE_ACESSO_JWT_CLIENT_ID'),
                                        secret=env('EGE_ACESSO_JWT_SECRET')).first()

        if aa is not None:
            print("application always exists")
            return

        print("creating app...\n")
        app = Application.objects.create(
            owner=su,
            name='ege_acesso',
            description='some description',
            client_id=env('EGE_ACESSO_JWT_CLIENT_ID'),
            secret=env('EGE_ACESSO_JWT_SECRET'),
            logo=None,
            allowed_callback_urls='http://localhost/ege/perfil/jwt/complete/\nhttp://localhost/ege/processoseletivo/jwt/complete/',
            allowed_web_origins='http://localhost/ege/perfil/jwt/login',
            allowed_logout_urls='http://localhost/ege/perfil/logout',
            expiration=600,
            created_at=datetime.datetime.now(),
            deleted_at=None)
        app.save()

        print("application client_id=%s" % env('EGE_ACESSO_JWT_CLIENT_ID'))
        print("application secret=%s" % env('EGE_ACESSO_JWT_SECRET'))
        print("\nDone.")
