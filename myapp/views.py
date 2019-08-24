from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from .tasks import print_lot_of_times


def do_a_celery_task(request):
    print_lot_of_times.delay("test text", 10)
    