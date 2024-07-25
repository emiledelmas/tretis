from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserUpdateForm,ProfileUpdateForm
from django.db.models import Q
from .models import Profiles_Picture, Profile, User, Historique
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import math

def tretis(request):
    #send_mail('subject', 'body of the message', 'tretis89@gmail.com', ['emile.delmas@gmail.com', 'emile.delmas@yahoo.fr'])
    return render(request,'home.html',)


def tretisPR(request):
    if request.method == "POST":
        username = request.POST['username_field']
        score = request.POST['score_field']
        rank = request.POST['rank_field']
        user = User.objects.get(username=username)
        userProfile = Profile.objects.get(user=user)
        level = userProfile.level
        userProfile.score += int(score) 
        RequiredXP = 5 * level * level - 5 * level+50
        if userProfile.level<100:
            while userProfile.score>=RequiredXP and userProfile.level<100:
                userProfile.score -= RequiredXP
                userProfile.level += 1
        elif userProfile.score >= RequiredXP:
            userProfile.score = RequiredXP
        userProfile.save()

        historique = Historique(username=username,rank=rank,level=userProfile.level,score=userProfile.score,game_score=score)
        historique.save()

        return redirect('pr') 
    else:
        return render(request,'pr.html', )

def tretisBR(request):
    return render(request,'br.html', )

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            form.active=True
            user = authenticate(request, username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.info(request,f'Account created for {username}! (+20 XP)')
            return redirect('home')
        else:
            return render(request,'registration/register.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request,'registration/register.html',{'form':form})


def email_already_exist(request):
    messages.warning(request,f'Account already created for this email address please login')
    return redirect('login')

@login_required
def profile_page(request):
    if request.method == "POST":
        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request,f'Your account has been updated')
        else:
            messages.warning(request,f'Username aleady taken or unvalid (This value may contain only letters, numbers, and @/./+/-/_ characters.)')
        return redirect('profile_page')
    else:
        profile_pics = Profiles_Picture.objects.all().order_by('required_level')
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    return render(request, 'profile.html',{'u_form':u_form,"p_form":p_form,"profile_pics":profile_pics})


def new_home(request):
    return render(request, 'new_home.html')

def history(request, username):
    historique = Historique.objects.filter(username=username).order_by('-created')
    game_count = historique.count()
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'history.html',{'historique':historique, 'game_count':game_count, 'profile':profile})


def global_leaderboard(request):
    players = Profile.objects.all().order_by('-level','-score')
    players_count = players.count()
    return render(request, 'global_board.html',{'players':players,'players_count':players_count})