from django.shortcuts import render

def login_view(request):
    template_view = "login.html"
    return render(request, template_name=template_view)

# View for Register
def register_view(request):
    template_view = "register.html"
    return render(request, template_name=template_view)

# View forget
def forget(request):
    template_view = "forget.html"
    return render(request, template_name=template_view)


