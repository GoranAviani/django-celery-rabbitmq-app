import string
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

#asincro task
@shared_task
def print_lot_of_times(someData, someData1):
    f= open("testfile.txt","w+")
    for i in range(someData1):
        f.write("This is text111111 ")
       

#periodic function that is beating
@shared_task
def this_is_periodic_task_function(a, b):
    f= open("testfile11.txt","a")
    for i in range(5):
        f.write(a)
        f.write(b)

import time    
@shared_task
def this_is_periodic_task_function_no_args():
    f= open("testfile22.txt","a")
    for i in range(5):
        f.write(str(time.ctime()))
        
    