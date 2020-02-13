import json
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from sc4net import get_json, post, post_json
from .models import Application, TransactionToken


@login_required
def authorize_view(request):
    print("authorize_view")
    assert 'client_id' in request.GET, "empty client_id on get"
    assert 'state' in request.GET, "state required"
    assert 'redirect_uri' in request.GET

    redirect_uri = request.GET['redirect_uri']

    auth_token = Application.authorize(request.user,
                                       request.GET['client_id'],
                                       request.GET['state'],
                                       redirect_uri,
                                       request.META.get('HTTP_REFERER'))
    return redirect("%s&auth_token=%s" % (redirect_uri, auth_token))


@csrf_exempt
def validate_view(request):
    assert 'client_id' in request.GET, "empty client_id on get"
    assert 'auth_token' in request.GET, "empty auth_token on get"
    return HttpResponse(TransactionToken.validate(request.GET['client_id'], request.GET['auth_token']))


def secret_validate_view(request, secret):
    application = get_object_or_404(Application, owner__deleted__isnull=True, secret=secret)
    return JsonResponse({"result": "OK", "client_id": application.client_id})


@login_required
def perfil_index(request):
    if request.COOKIES.get('hide_config'):
        return render(request, template_name='ege_perfil/index.html', context={'login_url': settings.LOGIN_URL})
    else:
        return HttpResponseRedirect('/ege/perfil/acessibilidade')


class AcessibilidadeService(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='ege_perfil/painel_acessibilidade.html')

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        print("Estou aqui.")
        url = settings.SUAP_EAD_ACESSO_JWT_ROOT + 'api/v1/users/%s/biografy/' % request.user.username
        data = {"biografy": json.loads(request.body)["biografy"]}
        result = post_json(url, data)
        return HttpResponse('{"successs": true}')


class UserBiografyService(View):

    def get(self, request, *args, **kwargs):
        url = settings.SUAP_EAD_ACESSO_JWT_ROOT + 'api/v1/users/%s/biografy/' % request.user.username
        result = get_json(url)
        return HttpResponse('{"biografy": "%s"}' % result.biografy)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        url = settings.SUAP_EAD_ACESSO_JWT_ROOT + 'api/v1/users/%s/biografy/' % request.user.username
        data = {"biografy": json.loads(request.body)["biografy"]}
        result = post_json(url, data)
        return HttpResponse('{"successs": true}')


class UserEmailService(View):

    def get(self, request, *args, **kwargs):
        url = settings.SUAP_EAD_ACESSO_JWT_ROOT + 'api/v1/users/%s/email/' % request.user.username
        result = get_json(url)
        return HttpResponse('{"email": "%s"}' % result.email)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        url = settings.SUAP_EAD_ACESSO_JWT_ROOT + 'api/v1/users/%s/email/' % request.user.username
        data = {"email": json.loads(request.body)["email"]}
        result = post_json(url, data)
        return HttpResponse('{"successs": true}')
