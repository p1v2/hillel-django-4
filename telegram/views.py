import json

from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from telegram.service import send_telegram_message


# Create your views here.

# Standard view
# @csrf_exempt
# def telegram(request: HttpRequest):
#     # Get JSON from HttpRequest
#     data = json.loads(request.body)
#
#     print(data)
#
#     return HttpResponse('OK!')

# Django REST view

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def telegram(request: Request):
    # Get JSON from HttpRequest
    data = request.data

    print(data)

    chat_id = data['message']['chat']['id']
    text = "Hello, again!"

    send_telegram_message(chat_id, text)

    return Response('OK!')
