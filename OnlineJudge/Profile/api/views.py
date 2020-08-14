from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from Profile.models import Profile
from .serializers import ProfileSerializer


class ProfileListSearchAPIView(APIView):
    permission_classes          =[]
    authentication_classes      =[]

    def get(self, request, format=None):
        qs= Profile.objects.all()
        serializer=ProfileSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs= Profile.objects.all()
        serializer=ProfileSerializer(qs, many=True)
        return Response(serializer.data)

class ProfileAPIView(generics.ListAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    serializer_class            =ProfileSerializer

    def get_queryset(self):
        qs= Profile.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(content_iscontains=query)
        return qs

class ProfileCreateAPIView(generics.CreateAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    queryset                    =Profile.objects.all()
    serializer_class            =ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    queryset                    =Profile.objects.all()
    serializer_class            =ProfileSerializer
    lookup_field                ='id'

class ProfileUpdateAPIView(generics.UpdateAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    queryset                    =Profile.objects.all()
    serializer_class            =ProfileSerializer
    lookup_field                ='id'

class ProfileDeleteAPIView(generics.DestroyAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    queryset                    =Profile.objects.all()
    serializer_class            =ProfileSerializer
    lookup_field                ='id'