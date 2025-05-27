from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view

from gp.forms import CommerceForm, SubscribeForm, MpesaForm
from gp.models import Commerce
from gp.serializers import CommerceSerializer
import json



# Create your views here.
def index(request):

    if request.method == "POST":
        form=CommerceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CommerceForm()
        return render(request,'index.html',{'form':form})


    return render(request, 'index.html')
def service(request):
    return render(request,'service.html')
# def starterpage(request):
    # return render(request,'starterpage.html')
def portfolio(request):
    return render(request,'portfolio.html')
def commercelist(request):
    commerce=Commerce.objects.all()
    return render(request, 'commercelist.html',{'commerce':commerce})

def updatecommerce(request,id):
    commerce=get_object_or_404(Commerce,id=id)
    if request.method == "POST":
        form=CommerceForm(request.POST,instance=commerce)
        if form.is_valid():
            form.save()
            return redirect('commercelist')
    else:
        form=CommerceForm(instance=commerce)
    return render(request, 'updatecommerce.html',{'form':form,'commerce':commerce})

def deletecommerce(request,id):
    commerce=get_object_or_404(Commerce,id=id)
    try:
        commerce.delete()
    except Exception as e:
        messages.error(request,'Error deleting commerce')
    return redirect('commercelist')
@api_view(['GET','POST'])
def commerceapi(request):
    if request.method == "GET":
        commerce=Commerce.objects.all()
        serializer=CommerceSerializer(commerce,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer=CommerceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login


# from django.contrib.auth import login
# from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

# Signup View with Email Verification
# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect after successful signup
            return redirect('login')  # Change 'login' to your preferred URL name
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to index page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have subscribed successfully!")
            return redirect("subscribe")
    else:
        form = SubscribeForm()

    return render(request, "subscribe.html", {"form": form})

  # Django Daraja import


def mpesa_payment(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        if not phone_number or not amount:
            return render(request, 'mpesa_form.html', {'error': 'All fields are required.'})

        try:
            amount = int(amount)
        except ValueError:
            return render(request, 'mpesa_form.html', {'error': 'Please enter a valid amount.'})

        # Instantiate the MPesa client
        client = MpesaClient()

        # Define your parameters (update these as needed)
        account_reference = "DigitalMarketing"  # Customize your account reference
        transaction_desc = "Payment for Digital Marketing Services"
        callback_url = 'https://darajambili.heroku.com/express-payment';

        # Initiate the STK Push payment
        response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        print("STK Push Response:", response)  # Log the response

        # Render a success page with the API response
        return render(request, 'mpesa_success.html', {'response': response})

    # For GET requests, simply display the form
    return render(request, 'mpesa_form.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        # Process the callback payload here
        callback_data = request.body.decode('utf-8')
        # Log or process the callback_data as needed
        print("Callback received:", callback_data)
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
    return JsonResponse({"error": "Invalid request method"}, status=400)


#
#
# def mfrom django.shortcuts import render
# from .forms import MpesaForm
# from django.http import HttpResponse
# from mpesa_api.mpesa_client import MpesaClient

# from django.shortcuts import render
# from .forms import MpesaForm
# from django.http import JsonResponse
# from mpesa_api.mpesa_client import MpesaClient

