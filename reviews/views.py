from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissionClass

class ReviewCreateListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermissionClass,)
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer