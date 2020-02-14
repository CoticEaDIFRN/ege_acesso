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
