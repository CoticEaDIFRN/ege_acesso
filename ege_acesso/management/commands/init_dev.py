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
from python_brfied import env
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import User, Application


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        if not settings.DEBUG:
            print("init_dev are project to dev environment")
            return

        su = User.objects.filter(is_superuser=True).first()
        if su is None:
            yn = input('do you wanna create a admin:admin superuser (y/N)?')
            if yn in ['Y', 'y']:
                su = User()
                su.username = 'admin'
                su.set_password('admin')
                su.first_name = 'First name'
                su.last_name = 'Last name'
                su.social_name = 'Social name'
                su.department = 'Department'
                su.campus = 'Campus'
                su.campus = 'Campus'
                su.active = 'Ativo'
                su.is_staff = True
                su.is_superuser = True
                su.carrer = 'Carrer'
                su.job = 'Job'
                su.cpf = 'CPF'
                su.academic_email = 'academic@email.edu'
                su.enterprise_email = 'enterprise@email.edu'
                su.email = 'personal@email.com'
                su.title = 'Officer'
                su.created_at = datetime.datetime.now()
                su.changed_at = datetime.datetime.now()
                su.password_set_at = datetime.datetime.now()
                su.last_access = datetime.datetime.now()
                su.last_ad_access_at = datetime.datetime.now()
                su.date_joined = datetime.datetime.now()
                su.first_access_at = None
                su.deleted_at = None
                su.photo_blob = 'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAKtklEQVR42u1dC4hcVxne2Uf2NSSrtSabzj3ve' \
                                '+exm91mlyapWZvVlhKIz6iNr5SGarRpoi0IKlWwRaTatNhafFBRUUHTChXFqlRBqA+0giAqTQpqrG1EKbaK2p' \
                                'hk9T93Z7Yn05mdOzt37pxz8l/4yWN3v3P2//655/znfOc/fX344NPJc9VVizmwfsNyiOcPXqvGBuoN8fzBaxV' \
                                'lg2BDhg2uNdoQzy68JI3pBtYZNtRh5xHPErwkjQ2DjRg23GHnEc8SvCSN6QZGDRvpsPOIZwleq8b0bHIMbNww' \
                                '/e9+xHMfL0ljuoG8YeMddh7xLMFL2th6w/Iddj7fK7zKxZW8JGReULpXMPYu+PMmRenN1b/vlURu277lsk2+/' \
                                'L5pjPljRoMbqn920vkazoYs8JRSw5yQPZKwT3PKfispOwf2v2YWcqHtnGLisUjIzxdVdM309NSoK7/vWjhuNc' \
                                'EYr4s4J8jnnEeCsntlwP6+GuENyD/P4q8BhsZijBV9Ib/K70DDnzdSi9G6scZ68jVJ8Co/BsQtJSV+VfLPtyX' \
                                'Avl8HlwfkDzYMAGNRYcQIgHHbyVdKjktKP8ED8t92iG+D/BVbboN+vFAojDpKfm2lsGEADFZXkmoBMGY9+Yxe' \
                                'BoScaJf4tZB/nhFyHGzOMfKHjZXCgfPmANX/GDICYMR68ik/CJ/I05mT//zb4DlFyPUOkN9vcLoSAI0mBbUA6' \
                                'GR5MqNPPrtjLcSnRb5pkDHcaTn5Y8ZKoeZ3sNE3DRjjg7XkLy4ubACnf9YW8ldwhLzPUvJr87haALyQXyMABm' \
                                '3/5IPT77KO/JUgEHdbRr65Ujja9M1uBIDl5PP3Wkt+FQ9SxXdb5L/1RgCMrLrw0+FycRZj/pXg4LM2k19LEwU' \
                                'hOy3xXy0Axrq5S9h18stB+aUyYKdsJ38lCCh9ghDyIgv8t77bG0WZpD7wWn3AFfIN+6oF/ss7Tz4n/FUOkh8b' \
                                'DFtXu7pRZAX5lUplHbxOH3eR/HhCGLDf7erbNYjkrxFPUXrIVfJX3gKEXI/krwFvfn5+SE+mXCZ/OS1kv4dfZ' \
                                'wDJbxOPE/I218l//i3A97lOfj7rzoPjfuwD+XEAcPaIy+SPN8gtu0t+QSpfyK9hzFbKs66R3zNNoCDswz6Rr6' \
                                '0o5a2oCUzYeXDeL30iX5ti4heoCUzQ+WgyekkrTZ9r5FfxzlFKJ1AT2KLzsT7fP/KXJ4MBfzVqAlvgSUpv95H' \
                                '8eE2AsI+iJrDFIwP2kI/kLxv9NmoCWzx65cxP8uNt4sdRE7j60w9OOuMj+VWxyGn4HXOoCWzycM43+kr+ioIY' \
                                'shzUBDZ5IE0q+Ux+/BZocLQMNYG1CSAh8z6TH6eClG5FTWCTJ+L8cp/Jr74BtqEmsAleJYqu8Jn86pnCOdQEN' \
                                'sHbUi5u95p8MD3PQXFIE7wtW6aKPpMfzwGUmkTym+BduX3xInDuWV/J14dGFhZ2TCD5q+BxQv7kI/kxHhUnkf' \
                                'wWeJLSh70kX2sCuHwYNYEtOi8CdtRH8quqoE+iJrBF5yVj+3wkPw4ApfajJrBF5wkhkz6SD7a0deusQE1ggs5' \
                                'zyn7joSbw16gJTCoLI+xjvsnCFGO3WUS+3XUCGWOzvsnCFCEVS8h3o04gZAO/8kcZRB+1hHx36gTqCt6+iEME' \
                                'pQcsWHdxq06gLsXKKf2b8/qAgJ3SdQ56TL6bdQIlYx90XgpO6U09Jt/dOoEv2zqzSXFxytkt4oCcpJSO9JB89' \
                                '+sEllV00Nkt4oBd02P/+VEnMBTiRw6S/5AF/vOjTqAQgsPr9BmHdgmfLgbBZgv850edQP11RfgbHSF/CT79r7' \
                                'HEf3lvagbFWcEqB0ftWTSit9nqP6fJrz45TsjXbSUfUr6v9K1y9AvJTwEvLh9HyDctJP+B+qKQSH6X8HQQ6Fq' \
                                '81rz2CfkSkp89Xg7G24/Uysn0asInCPvQhTDm523tvGRsT0jZX7PP88lfmhWD9o38zOsEtos3Pz0nIiGPZUU+' \
                                'jPdfLm3efJHv5Dt3d3A5LF3dToXR9smnjyS9DQTvDu7lohFju4Cwb9RXG1kL+fEVMDDD5wF/ueNzpkbb/37dH' \
                                'Vz/vXHNQcLfwQl7UC/PJiVfcvG0DNiDutR7oVB4sQcT5np+/bo7OCFeTgWB1LX6ICgOw+v8VphAHtVXvRWlvL' \
                                '0oxfuKYbRvplya8eT3bUa+X3cHI15b5Ptzd/Dc3KUbFRVHWl3n3s3+xTWNCLlR316OdwdnRL4+Ql6U6giM3U9' \
                                'Va++dAfscY4xm1b+IEA4Tw/tW7jHk4smylId13/Du4C6Rv7i4MFEK1dtDyppdFX92eaOILsKP9nehf/2QAr4S' \
                                'iL9fF35uNIFUTDxWisI3z85OD1jkP/fvDp4qFveEnD+aeJEnYH8Aou7Q6WBNkbuW/imlhnVACcLu1Pq+xKkjZ' \
                                'T8RgViwwH9uawIrlfLOiMnvd7jC92+9gBMJ8ZmikjeXi9Hecrm0c2qqPK3LtejilDCWs5DSS+H7dsNwcgPYPf' \
                                'pnIJD+0+GK4bdkEEz18MPjpiZwaqoypYT4mj5R60HNoHOSsC9IKYMezJnc0gTqO4JDIe8Fp532rkJoQJ7Tw5K' \
                                '5sISawOozs3HjOIzXt4Cj/uF9ncCAPCMC9v6MUke7NYFaRAGvx4M6pfO9QugLDFLHkgyP2Jg6ZtGY1va9QRJy' \
                                '3PfawC3xmDgO6e1bbEkdu95YvFNHyM99rwre/q4j+2k7O47OkQ/p1gykVd/x/T6ANK6VEQUx7Q35OsfWCpr6q' \
                                '+CQ/FXxlmBu9EUhBLGF/LY1gXovXhB2l74mxXOyups6BuyoKT+zXhOoUzp4jd0CnX/2QiKr66kjpR/gnOWt1Q' \
                                'RqrX5c1iVgpy5osrp6C7l4qiTVe9JIHdPUBOaWD27SE0hWVqkjO1EM1Vs7SB3T0QTqnTIzpUOyssWD+cHPIBi' \
                                'uyFwTqJS6WKtukSw78GB+cCzhOYXONYGxDKrB3jiS1WM8rYG4RIRd1QSGhcIlgrInkSw78fRlG/AB3dQtTWAO' \
                                'GvkBkmU3niDke31GjYLUNIGSsdciWa7g0d2pawIB+IfoXDfwOGHfTVUTCOPKhKmERbIsv52M0jM7ZrdNpqYJ1' \
                                'HJodK5beOWwtDs1TSCkGNeic93CK0XhgdQ0gfqELTrXuQuqDqWmCWwUAEiW3XiRkjektktYHwBIlgN4jB1IbW' \
                                'vYDAB0riMbRZRel3oAoHOduqYmvQBQVLwTnevcTSXpBICeSBRFeCM617kt4utSIV/nkUUZHkbnuoXXcQCYmkA' \
                                'zANC5buAlCYDEmkDIKQ+hcx3DI2x/aprAUhS+Dp3rGh59RWqawFKpOKEPKaBzncH71+Tk5FiqmkBdiQud6wYe' \
                                'jP+fSl0TqI96ccr+jGRZjheQk/XlbVOrE6ivQIc3wRNIlrXk/1GrtrtaJ1BHF0ww7oZA+CeSZYkaOCDP6oO4W' \
                                'rmVWZ1AfScuBMLlMN7s1UfDQireVFbRfrBrDduv/19/vV1DvNZ44PvXK0p36HqGNtQJNM8Qrk+hxDzipYOXSZ' \
                                '1A8wxhPoUS84iXLl5X6wSOGePMeAol5hHPErwkewW19YJRY5KRQzz38ZI0NmzkliMdlphHPIvwkh4xXmfYUIe' \
                                'dRzxL8JIWFxgybLDDziOeJXhJGhyoN8TzBy9JtPUblkM89/H+D/AdE3+KpeL3AAAAAElFTkSuQmCC'
                # su.photo_blob = 'data:image/png;base64'
                su.save()
                print("User created")

        if su is None:
            print("superuser dont exists")
            return

        expire_at = datetime.datetime.now() + datetime.timedelta(days=365)

        aa = Application.objects.filter(client_id=env('EGE_ACESSO_JWT_CLIENT_ID'),
                                        secret=env('EGE_ACESSO_JWT_SECRET')).first()

        if aa is not None:
            print("application always exists")
            return

        print("creating app...\n")
        app = Application()
        app.owner = su
        app.name = 'ege_acesso'
        app.description = 'some description'
        app.client_id = env('EGE_ACESSO_JWT_CLIENT_ID')
        app.secret = env('EGE_ACESSO_JWT_SECRET')
        app.logo = None
        app.allowed_callback_urls = 'http://localhost/ege/perfil/jwt/complete/?original_next=/ege/perfil/'
        app.allowed_web_origins = 'http://localhost/ege/perfil/jwt/login'
        app.allowed_logout_urls = 'http://localhost/ege/perfil/logout'
        app.expiration = 600
        app.created_at = datetime.datetime.now()
        app.deleted_at = None
        app.save()

        print("application client_id=%s" % env('EGE_ACESSO_JWT_CLIENT_ID'))
        print("application secret=%s" % env('EGE_ACESSO_JWT_SECRET'))
        print("\nDone.")
