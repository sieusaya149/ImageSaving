from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.core.files.storage import FileSystemStorage
from django.conf import settings 
import json
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from post.models import *
import os.path
import uuid
# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        print("user is authenthicated")
        return render(request,'post/post.html')
    else:
        print("user is not authenthicated")
        return render(request,'authenthicating/login.html')

@api_view(['GET'])
def getPostInfor(request,postId):
    postList = Post.objects.filter(userId=request.user).filter(postId__lt=postId).order_by('-postId')[0:3]
    print('postInfor')
    postInforSerial=  PostInformationSerializer(postList,many=True)
    return Response(postInforSerial.data)

@api_view(['GET'])
def getImageInfor(request,postId):
    imageInfor=Image.objects.filter(postId=postId)
    print('postInfor')
    imageInforSerial=  ImageInformationSerializer(imageInfor,many=True)
    return Response(imageInforSerial.data)

@api_view(['GET'])
def getHeartInfor(request,postId):
    heartList=UserHeart.objects.filter(postId=postId)
    print('listHeart')
    HeartListSerial=  HeartInformationSerializer(heartList,many=True)
    return Response(HeartListSerial.data)

@api_view(['GET'])
def getCommentInfor(request,postId):
    commentList=UserComment.objects.filter(postId=postId)
    print('listHeart')
    commentListSerial=  CommentInformationSerializer(commentList,many=True)
    return Response(commentListSerial.data)

def get_name_uid(filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

def CreateNewPost(request):
    try:
        if request.method == 'POST':
            caption = request.POST.get('caption')
            print('caption:', caption)
            description = request.POST.get('description')
            print('description:', description)
            listImages = request.FILES.getlist('fileList')
            if (len(listImages)<1):
                print('Do not have any images in this post')
                return render(request , 'post/post.html')
            # get user now
            currentUser = request.user
            if not request.user.is_authenticated:
                print('not allow to use this resource')
                return render(request , 'post/post.html')
            print('user now ', currentUser)
            # create new post
            newPost= Post.objects.create(userId=currentUser, caption=caption, 
                                        description=description)
            print('create new post success')
            # get Images
            for file in listImages:
                unitName=get_name_uid(file.name)
                print(unitName)
                fs = FileSystemStorage()
                fs.save(unitName, file)
                newImage = Image.objects.create(postId=newPost,
                                                name=file.name,
                                                path=unitName)
            print('create new images success')
    except Exception as e:
            print(e)
    return redirect('/')
