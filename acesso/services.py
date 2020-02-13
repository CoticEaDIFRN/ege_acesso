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
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class BaseModelService(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )


class UserService(BaseModelService):
    queryset = User.objects.filter(deleted__isnull=True)
    serializer_class = UserSerializer


# Trocar isso para APIView
class UserBiografyService(View):

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        return HttpResponse(json.dump({"biografy": user.biografy}))

    @method_decorator(csrf_exempt)
    def post(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        user.biografy = request.POST['biografy']
        user.save()
        return HttpResponse('{"success": true}')


class UserEmailService(View):

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        return HttpResponse(json.dump({"email": user.email}))

    @method_decorator(csrf_exempt)
    def post(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        user.email = request.POST['email']
        user.save()
        return HttpResponse('{"success": true}')

router = DefaultRouter()
router.register('users', UserService)
