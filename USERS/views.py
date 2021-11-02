from rest_framework.generics import GenericAPIView
from ADMIN.models import m
from .models import Users
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response 
from ADMIN.models import Advisor
from rest_framework import status
from ADMIN.serializers import AdvisorSerializer,AdvisorBookingSerializer,AdvisorBookedSerializer

class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_400_BAD_REQUEST)



class AdvisorList(APIView):
    def get(self, request, user_id):
        user = Users.objects.filter(id = user_id).exists()
        if  not user:
            return Response({"message":"User not Found!"},status=status.HTTP_400_BAD_REQUEST)
        tasks = Advisor.objects.all()
        serializer = AdvisorSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class AdvisorBooking(GenericAPIView):
    serializer_class = AdvisorBookingSerializer
    def post(self, request, user_id, advisor_id):
        user = Users.objects.filter(id = user_id).exists()
        if  not user:
            return Response({"message":"User not Found!"},status=status.HTTP_400_BAD_REQUEST)
        advisor = Advisor.objects.filter(id = advisor_id).exists()
        if not advisor:
            return Response({"message":"Advisor not Found!"},status=status.HTTP_400_BAD_REQUEST)
        name = Advisor.objects.filter(id = advisor_id).first()
        client = {'Advisor_client': request.user.username}
        serializer = AdvisorBookingSerializer(instance = name, data = request.data)
        if serializer.is_valid():
            serializer.update(instance = name, validated_data = client)
        return Response(status=status.HTTP_200_OK)
        

class AdvisorBooked(APIView):
    def get(self, request, user_id):
        user = Users.objects.filter(id = user_id).exists()
        if  not user:
            return Response({"message":"User not Found!"},status=status.HTTP_400_BAD_REQUEST)
        task = Advisor.objects.filter(Advisor_client = request.user.username)
        serializer = AdvisorBookedSerializer(task , many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)