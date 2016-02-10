from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Portraits, UserProfile, Commentaire
from .forms import PortraitsForm, CommentaireForm, UserProfileForm, UserForm, LoginForm
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

def portraits_list(request):
    portraits = Portraits.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'roots/portraits_list.html', {'portraits': portraits})

def portraits_detail(request, pk):
    portraits = get_object_or_404(Portraits, pk=pk)
    return render(request, 'roots/portraits_detail.html', {'portraits': portraits})

@login_required
def portraits_new(request):
    if request.method == "POST":
        form = PortraitsForm(request.POST)
        if form.is_valid():
            portraits = form.save(commit=False)
            portraits.ajouteePar = request.user
            portraits.date_publication = timezone.now()
            portraits.save()
            return redirect('roots.views.portraits_detail', pk=portraits.pk)
    else:
        form = PortraitsForm()
    return render(request, 'roots/portraits_edit.html', {'form': form})

@login_required
def add_commentaire_to_portraits(request, pk):
    portraits = get_object_or_404(Portraits, pk=pk)
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.portraits = portraits
            commentaire.save()
            return redirect('roots.views.portraits_detail', pk=portraits.pk)
    else:
        form = CommentaireForm()
    return render(request, 'roots/add_commentaire_to_portraits.html', {'form': form})

def user_detail(request):
    user_profile = get_object_or_404(UserProfile)
    return render(request, 'roots/user_detail.html', {'user_profile': user_profile})

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #Saving the user in user_profile
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('roots/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'roots/base.html')
                else:
                    return redirect('roots/error.html')
    else:
        form = LoginForm()
    return render(request, 'roots/login.html', {'form': form,})

def error(request):
    return render(request, 'roots/error.html')

def user_logout(request):
    logout(request)
    return render(request, 'roots/base.html')

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('roots.views.post_detail', pk=comment.post.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('roots.views.post_detail', pk=post_pk)

def search(request):
    context = RequestContext(request)
    try:
        q = request.GET['q']
        posts = Portraits.objects.filter(nom__search=q) | \
                Portraits.objects.filter(prenom__search=q) | \
                Portraits.objects.filter(citations__search=q) | \
                Portraits.objects.filter(oeuvres__search=q)
        return render_to_response('roots/results.html', {'posts':posts, 'q':q}, context)
    except KeyError:
        return render_to_response('roots/results.html')