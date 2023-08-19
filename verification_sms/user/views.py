from .serializers import PhoneSerializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Phone
import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from utils import send_message
from .serializers import generate_invite_code
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

class PhoneView(generics.CreateAPIView):
    queryset = Phone.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PhoneSerializers


def generate_code():
    number_list = [x for x in range(10)]
    code_items = []

    for i in range(4):
        num = random.choice(number_list)
        code_items.append(num)
    
    code_string = ''.join(str(item) for item in code_items)
    return code_string


@api_view(['POST'])
def verify_view(request):
    phone_number = request.data.get('phone_number')
    code = generate_code()
    send_message(code, phone_number=phone_number)
    try:
        phone = Phone.objects.get(phone_number=phone_number)
        phone.login_code = code
        phone.save()
    except ObjectDoesNotExist:
        Phone.objects.create(phone_number=phone_number, generated_code=generate_invite_code(6), login_code=code)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_code_view(request):
    phone_number = request.data.get('phone_number')
    verification_code = request.data.get('verification_code')

    if phone_number and verification_code:
        phone = Phone.objects.get(phone_number=phone_number)
        
        if phone.login_code == verification_code:
            return Response({'phone_number': phone.phone_number, 
                             'generated_code': phone.generated_code, 
                             'invitation_code': phone.invitation_code,
                             'friends_number': phone.friends_number.all().values_list('phone_number', flat=True)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing phone number or verification code'}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def add_invitation_view(request):
    invitation_code = request.data.get('invitation_code')
    phone_number = request.data.get('phone_number')

    if invitation_code and phone_number:
        try: 
             to_phone = Phone.objects.get(phone_number=phone_number)
        except:
            return Response({'message': "This phone number is not saved in our database"}, status=status.HTTP_400_BAD_REQUEST)
        
        if to_phone.invitation_code == "":
            try:
                from_phone = Phone.objects.get(generated_code=invitation_code)         
                phone_number += f"{phone_number}" if from_phone.friends_number == "" else f", {phone_number}"
                from_phone.save()
                to_phone.invitation_code = invitation_code
                to_phone.save()
                return Response(status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "This phone number is connected to an invitation code before."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': "Write invitation_code"}, status=status.HTTP_400_BAD_REQUEST)

        

@api_view(['GET'])
def profile_view(request):
    phone_number = request.data.get('phone_number')
    login_code = request.data.get('login_code')
    try:
        phone = Phone.objects.get(phone_number=phone_number)
        if login_code == phone.login_code:
            return Response({'phone_number': phone.phone_number, 
                                'generated_code': phone.generated_code, 
                                'invitation_code': phone.invitation_code,
                                'friends_number': phone.friends_number.all().values_list('phone_number', flat=True)}, status=status.HTTP_200_OK)
        else:
            return Response({'message:': "Your login code is not correct."})
             
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def verification_page(request):
    return render(request, 'index.html')
