from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Task
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import filters , viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib import messages
from django.contrib.auth import login , logout
# Create your views here.

#Listing
@api_view(['GET'])
def tasklist(request):
    tasks= Task.objects.all()
    serializer = TaskSerializer(tasks, many= True)
    return Response(serializer.data)

#Details
@api_view(['GET'])
def taskdetail(request,pk):
    task= Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many= False)
    
    return Response( serializer.data)

#updation
@api_view(['PUT'])
def taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer= TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#creation 
@api_view(['POST'])
def taskcreate(request):
    serializer= TaskSerializer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#deletetion 
@api_view(['DELETE'])
def taskdelete(request, pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response('Task deleted Successfully')









# =====================


class ToDoViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    search_fields= ['title','desc']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        task=Task.objects.all()
        print(task)
        return task

    def create(self, request, *args, **kwargs):
        # request.data[] = 
        print(request.data)
        ser = self.serializer_class(data=request.data)
        ser.is_valid()
        print(ser.errors)  # force to show errors
        return super().create(request, *args, **kwargs)
    
        


    def update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(["POST"])
def logOutUser(request):
    logout(request)
    return Response({
        "logout": "success"
    })

class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            messages.warning(request,"Invalid username, password")
            return Response({
                "error": "invalid username password"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = serializer.validated_data
            print(user,'==================')
            login(request, user)
            # messages.success(request, "Log in success")
            # _, token = AuthToken.objects.create(user)
            return Response({
                "user" : userSerializer(user, context=self.get_serializer_context()).data,
                # "token":token
            })



class RegisterUserView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def get(self, request, *args, **kwargs):
        return render(request, 'registration.html')

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # _, token = AuthToken.objects.create(user)
        # login(request, user)  # if you readily want to login the user after register
        return redirect('home')



def index(request):
    if(request.user.is_authenticated) :
        task = Task.objects.all()
        return render(request, 'index.html', { 'tasks': task})
    else:
        return render(request, 'user.html')

