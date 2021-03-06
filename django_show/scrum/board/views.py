# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions, filters
from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model
import django_filters

User = get_user_model()


# Create your views here.

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ('sprint', 'status', 'assigned')


class DefaultsMixin(object):
    authentication_classes = (authentication.BasicAuthentication,
                              authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 25
    paginate_by_parm = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        # filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    search_fields = ('name',)
    ordering_fields = ('end', 'name',)


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'order', 'start', 'due', 'completed',)
    filter_class = TaskFilter


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
