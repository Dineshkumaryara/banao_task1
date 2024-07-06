from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    return render(request, 'home.html')


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Patient'})


def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignUpForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Doctor'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_patient:
                return redirect('patient_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})


@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})


# blog
@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('doctor_dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


@login_required
def doctor_dashboard(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'doctor_dashboard.html', {'posts': posts})


@login_required
def patient_dashboard(request):
    posts = BlogPost.objects.filter(draft=False)
    for post in posts:
        post.summary = ' '.join(post.summary.split()[:15]) + '...'
    return render(request, 'patient_dashboard.html', {'posts': posts})


# edit blog
@login_required
def edit_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('doctor_dashboard')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': form, 'blog_post': blog_post})
