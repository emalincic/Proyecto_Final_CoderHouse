from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm, PasswordEditForm
from accounts.models import Avatar


# from accounts.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)

        return redirect('/app/show/')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            data = form.cleaned_data
            avatar = Avatar(user=user, imagen=data['avatar'])
            avatar.save()

            return redirect("/accounts/login/")

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required(login_url='Login')
def editar_request(request):
    user = request.user
    if request.method == "POST":

        form1 = UserUpdateForm(request.POST)
        form2 = PasswordEditForm(request.user, request.POST)

        if 'submit1' in request.POST:
            if form1.is_valid():
                data = form1.cleaned_data
                user.email = data['email']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.username = data['username']
                user.save()

                return redirect('home')

        if 'submit2' in request.POST:
            if form2.is_valid():
                contra = form2.cleaned_data['new_password1']

                if contra:
                    user.set_password(contra)
                    user.save()

                    return redirect('home')
    else:
        form1 = UserUpdateForm()
        form2 = PasswordEditForm(request.user)

    return render(request, "accounts/editar_usuario.html", {'form1': form1, 'form2': form2})


@login_required(login_url='Login')
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            avatar = user.avatar
            avatar.imagen = data["imagen"]
            avatar.save()

            return redirect("/app/show/")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)
