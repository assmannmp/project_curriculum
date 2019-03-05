from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
import bcrypt
from .models import Curriculum
from .forms import CurriculumForm

def home(request):
    return render(request,'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('curriculum_list')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'login.html',{})

def register(request):
    if request.method == 'POST':
        if(request.POST['password']== request.POST['password_confirmation']):
            user = User.objects.create_user(username=request.POST['first_name'],email=request.POST['email'],password=request.POST['password'])
            user.save()
            request.session['id'] = user.id
            user = authenticate(username=request.POST['first_name'], password=request.POST['password'])
            login(request, user)
            return redirect('curriculum_new')
        else:
            return HttpResponse("Password and confirmation different password")
    else:
        return render(request,'curriculum_register.html')

@login_required
def curriculum_new(request):
    form = CurriculumForm(request.POST or None,request.FILES or None)
    if(form.is_valid()):
        form.save()
        return redirect('curriculum_list')
    return render(request,'curriculum_new.html',{'form':form})

@login_required
def curriculum_list(request):
    search = request.GET.get('search',None)
    if(search):
        curriculum = Curriculum.objects.filter(presentation_letter__icontains=search)
    else:
        curriculum = Curriculum.objects.all()
    return render(request,'curriculum.html',{'curriculum':curriculum})

@login_required
def curriculum_update(request , id):
    curriculum = get_object_or_404(Curriculum,pk=id)
    form = CurriculumForm(request.POST or None,request.FILES or None, instance=curriculum)
    if (form.is_valid()):
        form.save()
        return redirect('curriculum_list')

    return render(request, 'curriculum_form.html', {'form': form})

@login_required
def curriculum_delete(request, id):
    curriculum = get_object_or_404(Curriculum, pk=id)
    if (request.method == 'POST'):
        curriculum.delete()
        return redirect('curriculum_list')

    return render(request, 'delete_curriculum.html', {'curriculum': curriculum})