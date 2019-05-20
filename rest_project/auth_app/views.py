from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model


def auth():
    return None