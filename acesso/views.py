suap_ead_
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
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
