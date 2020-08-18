import json
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins, permissions
from django.shortcuts import get_object_or_404

from .models import Profile
from .serializers import ProfileSerializer



def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid=True
    except ValueError:
        is_valid=False
    return is_valid

class ProfileAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView,
    ):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class            = ProfileSerializer
    queryset                    = Profile.objects.all()
    lookup_field                = 'user'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

 #   def perform_update(self, serializer):
 #       serializer.save(updated_by_user=self.request.user)

#    def perform_destroy(self, instance):
#        if instance is not None:
#            return instance.delete();
#        return None

class ProfileAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView,
    ):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    #queryset                   = Profile.objects.all()
    serializer_class            = ProfileSerializer
    passed_id                   = None

    def get_queryset(self):
        request = self.request
        #print(request.user)
        qs              = Profile.objects.all()
        query           = request.GET.get('q')
        if query is not None:
            qs          = qs.filter(about__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

