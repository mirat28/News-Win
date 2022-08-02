from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        redirect('/login')
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request)
    context = {"form":form}
    return render(request, "accounts/login.html", context)

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # print(username, password)
#         user = authenticate(request, username=username, password=password)
#
#         if user is None:
#             context = {"error": "invalid username or password. "}
#             return render(request, "accounts/login.html", context)
#         login(request, user)
#         return redirect("/admin")
#     return render(request, "login.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")

    return render(request, "accounts/logout.html", {})


def SignUp(request):
    return render(request, 'SignUp.html', {})


# def forms(request):
#     submitbutton = request.POST.get("submit")
#
#     firstname = ''
#     lastname = ''
#     emailvalue = ''
#
#     form = UserForm(request.POST)
#     if form.is_valid():
#         firstname = form.cleaned_data.get("first_name")
#         lastname = form.cleaned_data.get("last_name")
#         emailvalue = form.cleaned_data.get("email")
#
#     context = {'form': form, 'firstname': firstname,
#                'lastname': lastname, 'submitbutton': submitbutton,
#                'emailvalue': emailvalue}
#
#     return render(request, 'forms.html', context)



