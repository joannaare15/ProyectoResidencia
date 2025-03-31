from django.shortcuts import render

# Define your view function for handling login requests
def login_view(request):
    # Specify the template file that will render the login page
    template_view = "login.html"

    # Render the login template and return the response
    return render(request, template_name=template_view)