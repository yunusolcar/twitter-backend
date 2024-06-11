from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.account.models import UserProfile
from apps.account.serializers import UserSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = UserProfile.objects.filter(pk=pk).first()
        if user is None:
            return Response({'error': 'User not found'}, status=404)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = UserProfile.objects.filter(pk=pk).first()
        if user is None:
            return Response({'error': 'User not found'}, status=404)

        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = UserProfile.objects.filter(pk=pk).first()
        if user is None:
            return Response({'error': 'User not found'}, status=404)

        user.delete()
        return Response(status=204)
