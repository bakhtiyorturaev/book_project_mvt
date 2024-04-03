from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, CustomUserCreationForm, CustomerUserUpdateForm, CustomerUser
from django.views import View
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home page
def index(request):
    return render(request, 'index.html')


# Signup page
def user_signup(request):
    context = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        for i in form:
            if i.label == "Password":
                i.label = "Parol"
            elif i.label == "Password confirmation":
                i.label = "Parolni tasdiqlang"
        if form.is_valid():
            form.save(commit=False)
            form.instance.username = form.cleaned_data['username'].lower()
            form.save()
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'ttingiz ")
            User = get_user_model()
            registered_user = User.objects.filter(email=form.cleaned_data['email']).first()
            if registered_user:
                return redirect('user:login')
        else:
            messages.error(request, "Ro'yxatdan o'tolmadingiz")
    else:
        form = CustomUserCreationForm()
        context['form'] = form
    return render(request, 'registration/signup.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                messages.success(request, 'Tizimga xush kelibsiz')
                return redirect('home')
            else:
                messages.error(request, 'Bunday login yoki parol mavjud emas')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


# Logout page
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'Tizimdan chiqdingiz')
    return redirect('user:login')


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        update_form = CustomerUserUpdateForm(instance=request.user)
        context = {'update_form': update_form}
        return render(request, 'registration/profile_update.html', context=context)

    def post(self, request):
        update_form = CustomerUserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Ma'lumotlar muvaffaqiyatli yangilandi")
            return redirect('user:profile')
        else:
            messages.error(request, "Yangilanish muvaffaqqiyatsiz tugadi")
            context = {'update_form': update_form}
            return render(request, 'registration/profile_update.html', context=context)


@login_required(login_url='login')
def profile_view(request):
    return render(request, 'registration/profile.html')

