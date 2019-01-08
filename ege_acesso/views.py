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
