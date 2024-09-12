from time import sleep

from django.http import HttpResponse
from random import random


def hello_world(request):
    # random_time = random() * 10  # 0-10 seconds
    #
    # sleep(random_time)

    return HttpResponse('Hello, World!')
