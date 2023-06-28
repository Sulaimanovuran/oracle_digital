from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Student
from .serializers import StudentSerializer, SpamSerializer
from .signals import send_spam_mail



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['id', 'full_name', 'email', 'group']
    ordering_fields = ['full_name', 'email', 'group', 'date_of_brith']
    search_fields = ['full_name', 'email',]



class SpamAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = SpamSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        students = Student.objects.all()
        for student in students:
            send_spam_mail(student.email, student.full_name, data['text'])
        return Response('Письма успешно отправлены всем учашимся')

