from django.shortcuts import render
# rest_framework
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# for return
from rest_framework.response import Response
# token
from rest_framework.authtoken.models import Token
# authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# jwt authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Generic feature for easy curd operation
from rest_framework import generics

# custom
from .models import *
from .serializers import *
from .serverDemo import *


class ServerView(ServerD, APIView):
    def post(self, request):
        data = request.data
        print(data)
        try:
            name = data.get('name')
            age = data.get('age')

            if name is None or age is None:
                print("*"*20)
                return Response({'status': 403, 'error': "wrong field name given", "field name error": 'required fields : name , age'})

            self.changeClient(name=name, age=age)

            return Response({'status': 200,
                             "clients": ServerD.client,
                            "payload": request.data,
                             "message": 'client added'})
        except Exception as e:
            return Response({'status': 403, 'error': e, 'message': 'required fields : name , age'})


class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # generics.ListAPIView for GET method
    # generics.CreateAPIView for POST method


class StudentGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    # generics.UpdateAPIView for put or patch method
    # generics.DestroyAPIView for delete method


# Create your views here.
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)  # jwt auth

        # Token_obj,_ =  Token.objects.get_or_create(user=user) # basic auth
        # return Response({'status':200,"payload":serializer.data,'token':str(Token_obj),"message":'data saved'})

        return Response({'status': 200,
                         "payload": serializer.data,
                         'refresh': str(refresh),
                         'access': str(refresh.access_token),
                         "message": 'data saved'})


class StudentAPI(APIView):

    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Student_obj = Student.objects.all()
        serializer = StudentSerializer(Student_obj, many=True)
        return Response({'status': 200, "message": serializer.data})

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

        serializer.save()
        return Response({'status': 200, "payload": serializer.data,"request":data, "message": 'data saved'})

    def put(self, request):
        try:
            Student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(Student_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

            serializer.save()
            return Response({'status': 200, "payload": serializer.data, "message": 'data updated'})

        except Exception as e:
            return Response({'status': 403, 'error': e, 'message': 'invalid ID'})

    def patch(self, request):
        try:
            Student_obj = Student.objects.get(id=request.data['id'])
            # partial use to preform patch operation
            serializer = StudentSerializer(
                Student_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'something went wrong'})

            serializer.save()
            return Response({'status': 200, "payload": serializer.data, "message": 'data updated'})

        except Exception as e:
            return Response({'status': 403, 'error': e, 'message': 'invalid ID'})

    def delete(self, request):
        print(request.data)
        try:
            id = request.data.get('id')
            if id is None:
                raise serializers.ErrorDetail({'error': "id feild missing"})
            
            Student_obj = Student.objects.get(id=id)
            Student_obj.delete()
            return Response({'status': 200, "message": 'data deleted'})
        except Exception as e:
            return Response({'status': 403, 'error': e, 'message': 'invalid ID'})


# @api_view(['GET'])
# def get_book(request):
#     book_obj = Book.objects.all()
#     serializer = BookSerializer(book_obj,many=True)
#     return Response({'status':200,"payload":serializer.data})

# @api_view(['GET'])
# def home(request):
#     Student_obj = Student.objects.all()
#     serializer = StudentSerializer(Student_obj, many=True)
#     return Response({'status':200,"message": serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})

#     serializer.save()
#     return Response({'status':200,"payload":serializer.data,"message":'data saved'})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         Student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(Student_obj,data=request.data ,partial = True) # partial use to preform patch operation

#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})

#         serializer.save()
#         return Response({'status':200,"payload":serializer.data,"message":'data saved'})

#     except Exception as e:
#         return Response({'status':403,'error':e,'message':'invalid ID'})

# @api_view(["DELETE"])
# def delete_student(request,id):
#     try:
#         Student_obj = Student.objects.get(id=id)
#         Student_obj.delete()
#         return Response({'status':200,"message":'data deleted'})
#     except Exception as e:
#         return Response({'status':403,'error':e,'message':'invalid ID'})
