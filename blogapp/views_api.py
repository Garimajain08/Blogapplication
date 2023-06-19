from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Profile,BlogComment
from.utlis import *


class Loginview(APIView):
    def post(self, request):
        response={}
        response['message']="something went wrong"
        response['status'] = "500"
        try:
            data = request.data
            if data.get('username') is None:
                 response['message'] = "User name not found "
                 raise Exception('Username not found')
            if data.get('email') is None:
                 response['message'] = "User name not found "
                 raise Exception('Username not found')
            if data.get('password') is None:
                response['message'] = 'Password is wrong'
                raise Exception('User name not found')

            obj = User.objects.filter(email = data.get('email') , username = data.get('username')).first()
            if obj is None:
                response['message'] = 'User doesnt exist'
                raise Exception ( 'No user with this id' )
            pro_obj = Profile.objects.get(user = obj)
            if  not pro_obj.verified:
                response['message'] = "Your account is not verified"
                raise Exception ('First verify your account')
            print("Verifieed")
            user_obj = authenticate(username = data.get('username'),email = data.get('email'),password = data.get('password'))
            if user_obj  is  None:
                response['message'] = 'Invalid password'
                raise Exception ( 'No user with this id' )
                response['message'] = 'Invalid password'
            else:

               # login(request,user_obj)
               response['message'] = f"Welcome  {data.get('username') }"
               response['status'] = "200"
            return  Response (response)


        except Exception as e:
            print("exception",e)
            return Response(response)


class Register(APIView):
    def post(self, request):
        response = {}
        response['message']="something went wrong"
        response['status'] = "500"
        try:
            print("TRy")
            data = request.data
            print(data)
            if data.get('username') is None:
                 response['message'] = "User name not found"
                 raise Exception('Username not found')
            if data.get('password') is None:
                response['message'] = 'Password is wrong'
            if data.get('email') is None:
                response['message'] = "Enter valid email"
                raise Exception('User name not found')
            obj = User.objects.filter(email = data.get('email')).first()
            if obj :
                response['message'] = 'Already exists user'
                raise Exception ( 'Already exist user' )

            else:
                newuser = User(username =  data.get('username') , email = data.get('email'))
                newuser.set_password(data.get('password'))
                newuser.save ()
                print("yha tak aaay new user")
                token = random_string_generator ( size=20 )
                print(token,"token")
                p = Profile(user=newuser,token = token)
                send_email_to(token,data.get('email'))
                p.save()
                response['message'] = f"Welcome{data.get('username')}"
                response['status'] = " 200 "
            return  Response (response)

        except Exception as e:
            print("exception",e)
            return Response(response)












Loginview = Loginview.as_view()
Register  = Register.as_view()
# Comment = Comment.as_view()