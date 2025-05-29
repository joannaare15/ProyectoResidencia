from django.shortcuts import render

# Define your view function for handling login requests
def home_views(request):
    # Specify the template file that will render the home page
    template_view = "index.html"

    # Render the home template and return the response
    return render(request, template_view)


