from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Usuario, Producto
from .forms import UsuarioForm, ProductoForm

# ====================
# ERROR 404 PERSONALIZADO
# ====================

def custom_404(request, exception):
    return render(request, '404.html', status=404)


# ====================
# PÁGINAS ESTÁTICAS
# ====================

def home(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def about_view(request):
    return render(request, 'about.html')

def about_login(request):
    return render(request, 'login.html')  # O cambia por otra plantilla si tienes una diferente

def contact(request):
    return render(request, 'contact.html')


# ====================
# AUTENTICACIÓN
# ====================

def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        try:
            usuario = Usuario.objects.get(correo=correo, contraseña=contraseña)
            request.session['usuario_id'] = usuario.id
            return redirect('profile')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('login_vista')

    return render(request, 'register.html')


def forgot_password(request):
    return render(request, 'forgot.html')

def forgot_coupon(request):
    return render(request, 'forgot/coupon.html')


# ====================
# PERFIL
# ====================

def profile_view(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login_vista')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, 'El usuario no existe.')
        return redirect('login_vista')

    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.correo = request.POST.get('correo')
        usuario.telefono = request.POST.get('telefono')
        usuario.sexo = request.POST.get('sexo')
        usuario.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('profile')

    return render(request, 'profile.html', {'usuario': usuario})


def logout_view(request):
    request.session.flush()
    return redirect('home')


# ====================
# BLOG
# ====================

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog_details_2(request):
    return render(request, 'blog-details-2.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

def blog_list(request):
    return render(request, 'blog-list.html')

def blog_coupon(request):
    return render(request, 'blog/coupon.html')

def blog_contact(request):
    return render(request, 'contact.html')  # Si usas una plantilla distinta, cámbiala


# ====================
# CUPONES
# ====================

def coupon_contact(request):
    return render(request, 'coupon/contact.html')

def coupon_blog(request):
    return render(request, 'coupon/blog.html')

def coupon_blog_details(request):
    return render(request, 'coupon/blog_details.html')

def coupon_blog_details_2(request):
    return render(request, 'coupon/blog_details_2.html')

def coupon_blog_grid(request):
    return render(request, 'coupon/blog_grid.html')

def coupon_blog_list(request):
    return render(request, 'coupon/blog_list.html')

def coupon_contact_blog_html(request):
    return render(request, 'coupon/contact/blog.html')

def coupon_view(request):
    return render(request, 'index/coupon.html')

def cupon_index(request):
    return render(request, 'coupon/index.html')



# ====================
# E-COMMERCE
# ====================

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def compare(request):
    return render(request, 'compare.html')

def contact_view(request):
    return render(request, 'contact.html')

def blog_view(request):
    return render(request, 'blog.html')  # o la plantilla que corresponda

def register_view(request):
    return render(request, 'login/register.html')  # O el nombre correcto de tu plantilla







# ====================
# PRODUCTOS
# ====================

def subir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto subido correctamente.')
            return redirect('home')
    else:
        form = ProductoForm()

    return render(request, 'subir_producto.html', {'form': form})


# ====================
# REGISTRO CUSTOM
# ====================

def registro_custom(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro completado.')
            return redirect('login_vista')
    else:
        form = UsuarioForm()

    return render(request, 'register.html', {'form': form})


