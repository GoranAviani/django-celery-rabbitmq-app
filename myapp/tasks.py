import string
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def print_lot_of_times(someData, someData1):
    for i in range(someData1):
        print(someData)
    return HttpResponse('do_a_celery_task')