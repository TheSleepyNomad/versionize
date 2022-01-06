from django.shortcuts import render

def index(request): return render(request, 'user/base.html')


def login(request):
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = auth.authenticate(username=username, password=password)
    #         if user and user.is_active:
    #             auth.login(request, user)
    #             return HttpResponseRedirect(reverse('index'))
    # else:
    #     form = UserLoginForm()
    # context = {'title': 'Login',
    #            'form': form}
    return render(request, 'user/login.html')
    # , context)


def lk(request):
    return render(request, 'user/lk.html')
