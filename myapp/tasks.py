import string
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def print_lot_of_times(someData, someData1):
    f= open("testfile.txt","w+")
    for i in range(someData1):
        f.write("This is text111111 ")
       

@shared_task
def add(a, b):
    f= open("testfile11.txt","a")
    for i in range(5):
        f.write("This is tex3 ")
    