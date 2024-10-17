from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from login_app.forms import SignupForm , Additional_info , UserUpdateForm
from .models import profile
from django.core.exceptions import ObjectDoesNotExist



def test_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        
        return redirect('home')
    return render(request,'login.html')

def test_logout(request):
    logout(request)
    return redirect('login')

def test_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render('index.html')
    else:
        form = SignupForm()
    return render(request , 'register.html' , {'form':form})

def test_wellcom(request):
    return render(request,'welcome.html')

def additional_info_profile(request):
    context = {}
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    national_id = request.POST.get('national_id')
    card_no = request.POST.get('card_no')
    
    post = request.POST.copy() 
    if request.POST.get('is_Subscription') is not None:
        post['is_Subscription'] = True
        request.POST = post


    try:
        Additional_info(request.user.profile)
    except ObjectDoesNotExist:
        profile.objects.create(user = request.user)

    user_profile = profile.objects.get(user = request.user)
    context['profile'] = profile

    if request.method == 'POST':
        form = UserUpdateForm(request.POST , instance=request.user)
        if first_name != None and last_name != None and email != None:
            form.save()
            form = Additional_info(data = request.POST , instance=request.user.userprofile , files= request.FILES)
            if phone_number != None and national_id != None and card_no != None :
                form.save()
                return redirect('store_app.views.index.html')
        
    return render(request , 'profile-additional-info.html' , context)

