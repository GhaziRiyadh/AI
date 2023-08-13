from django.shortcuts import render
from UserApp.models import CatDog, User, FinancialAccount as FinancialAccountModel
from django.contrib.auth import login, logout
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings


from rest_framework import viewsets, response,  permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

# AI
from keras.utils import load_img, img_to_array
from tensorflow import nn, expand_dims
# from keras import models
# from UserApp.apps import class_names, UserappConfig, img_height, img_width
# import numpy as np


from UserApp.serializers import AuthSerializer, CatDogSerializer, FinancialAccountSerializer, UserSerializer
# Create your views here.


class UserViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (TokenAuthentication)

    def list(self, request):
        users = User.objects.all()
        serials = UserSerializer(users, many=True)
        return response.Response(serials.data)

    @action(methods=['post'], detail=False, url_path=r'login', url_name='login')
    def login(self, request, pk=None):
        user = User.objects.filter(email=request.data['email'])

        # validation data
        users = AuthSerializer(data=request.data)
        users.is_valid(raise_exception=True)

        # genrate token
        token, created = Token.objects.get_or_create(user=user)  # get token

        return response.Response(
            data={
                'token': token.key,
                'user': UserSerializer(user).data
            }
        )

    @action(methods=['POST'], detail=False, url_path=r'register', url_name='register')
    def register(self, request):
        print(request.user)
        # validation and cteate user
        users = UserSerializer(data=request.data)
        users.is_valid(raise_exception=True)
        user = users.save()

        # genrate token
        token, created = Token.objects.get_or_create(user=user)  # get token

        return response.Response(
            data={
                'token': token.key,
                # 'user': user
            }
        )
        pass

    @action(methods=['get'], detail=False, url_name='logout')
    def logout(self, request, pk=None):
        user = authentication.get_user_model()
        token = Token.objects.get(user=user)
        token.delete()
        return response.Response(data='done')

    # video stream function
    @action(methods=['POST'], url_path='video-streem', detail=False)
    def videoStreem(self, request):
        return response.Response(request.data['video'])

    # django login function

    # @action(methods=['POST'], detail=False, url_name='image-test', url_path='image-test')
    # def clfImage(self, request):
    #     f = request.FILES['image']  # here you get the files needed
    #     responses = {}
    #     file_name = "pic.jpg"
    #     file_name_2 = default_storage.save(file_name, f)
    #     file_url = default_storage.url(file_name_2)
    #     original = load_img('media/' + file_name_2,
    #                         target_size=(img_height, img_width))
    #     numpy_image = img_to_array(original)
    #     img_array = expand_dims(numpy_image, 0)  # Create a batch

    #     # model = UserappConfig.model.load_model('cats_and_dogs_small_1.h5')

    #     predictions = UserappConfig.model.predict(img_array)
    #     score = nn.softmax(predictions[0])
    #     # type = class_name[np.argmax(score)]
    #     print(
    #         "This image most likely belongs to {} with a {:.2f} percent confidence."
    #         .format(class_names[np.argmax(score)], 100 * np.max(score))
    #     )
    #     type = class_names[np.argmax(score)]
    #     responses['type'] = type
    #     print(
    #         f"This image most likely belongs to {type} with a {100 * np.max(score):.2f} percent confidence.")
    #     CatDog.objects.create(image=f,type=type);
    #     return response.Response(data=responses)

    @action(methods=['GET'], detail=False, url_path='get-history')
    def getHistory(self, request):
        history = CatDogSerializer(CatDog.objects.all(), many=True)
        return response.Response(data=history.data)


class FinancialAccount(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated)
    authentication_classes = (TokenAuthentication)

    # @action(url_name='getAll', detail=False, methods='get')
    def list(self, request):
        ser = FinancialAccountSerializer(
            FinancialAccountModel.objects.all(), many=True)
        return response.Response(ser.data)

    @action(detail=True, url_name='payment', methods='post')
    def payment(self, request, pk):
        ser = FinancialAccountSerializer(
            FinancialAccountModel.objects.all(), many=True)
        return response.Response(ser.data)
        pass
    pass
