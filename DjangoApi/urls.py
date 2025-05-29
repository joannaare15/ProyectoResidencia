from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static

from api.views import (
    home, profile_view, logout_view, custom_404, registro_custom,
    about_view, about_login, contact, cupon_index, coupon_view,
    login_view, register_view, forgot_password, forgot_coupon,
    blog, blog_details, blog_details_2, blog_grid, blog_list,
    blog_contact, blog_coupon, contact_view, blog_view,
    coupon_contact, coupon_blog, coupon_blog_details, coupon_blog_details_2,
    coupon_blog_grid, coupon_blog_list, coupon_contact_blog_html,
    cart, checkout, compare,
    subir_producto
)

# Página 404 personalizada
handler404 = 'api.views.custom_404'

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Página principal
    path('', home, name='home'),
    path('index/', home, name='home_index'),
    path('index.html', RedirectView.as_view(url='/index/', permanent=True)),

    # Registro personalizado
    path('index/register/', registro_custom, name='registro_custom'),

    # Login, Registro, Olvido contraseña
    path('login/', login_view, name='login_vista'),
    path('login/register/', register_view, name='register_view'),
    path('login/forgot/', forgot_password, name='forgot_login'),
    path('forgot/', forgot_password, name='forgot'),
    path('forgot/coupon/', forgot_coupon, name='forgot_coupon'),
    path('coupon/', cupon_index, name='cupon_index'),


    # Logout
    path('logout/', logout_view, name='logout'),

    # Perfil
    path('profile/', profile_view, name='profile'),
    path('profile/index/', profile_view),
    path('index/profile/', profile_view),
    path('index/profile/index/', profile_view, name='index_profile_index'), 
    path('index/contact', contact_view, name='index_contact'),   
    path('index/blog', blog_view, name='index_blog'), 

    # Acerca de y contacto
    path('about/', about_view, name='about'),
    path('about/login/', about_login, name='about_login'),
    path('about/login/register/', register_view, name='about_login_register'),
    path('contact/', contact, name='contact'),

    # Blog
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog_details'),
    path('blog-details-2/', blog_details_2, name='blog_details_2'),
    path('blog-grid/', blog_grid, name='blog_grid'),
    path('blog-list/', blog_list, name='blog_list'),
    path('blog/contact/', blog_contact, name='blog_contact'),
    path('blog/coupon/', blog_coupon, name='blog_coupon'),
    path('blog-list/blog-details-2/', blog_details_2, name='nested_blog_details_2'),
    path('blog-list/blog-details-2/blog-details/', blog_details_2, name='deep_blog_details_2'),
    path('blog-list/blog-details-2/blog-details/contact/', contact, name='deep_nested_contact'),
    path('blog/coupon/', TemplateView.as_view(template_name='blog/coupon.html')),


    # Cupones
    path('coupon/', TemplateView.as_view(template_name='coupon/index.html'), name='coupon_page'),
    path('coupon/contact/', coupon_contact, name='coupon_contact_view'),
    path('coupon/blog/', coupon_blog, name='coupon_blog'),
    path('coupon/blog-details/', coupon_blog_details, name='coupon_blog_details'),
    path('coupon/blog-details-2/', coupon_blog_details_2, name='coupon_blog_details_2'),
    path('coupon/blog-grid/', coupon_blog_grid, name='coupon_blog_grid'),
    path('coupon/blog-list/', coupon_blog_list, name='coupon_blog_list'),
    path('coupon/contact/blog/', coupon_contact_blog_html, name='coupon_contact_blog_html'),
    path('coupon/contact/', coupon_contact, name='coupon_contact_view'),
    path('index/coupon/', coupon_view, name='coupon_view'),
    path('index/coupon/', TemplateView.as_view(template_name='coupon/index.html'), name='coupon_view'),


    # E-commerce
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('compare/', compare, name='compare'),

    # Subir producto
    path('subir-producto/', subir_producto, name='subir_producto'),

    # Alias .html -> vistas reales
    path('login.html', RedirectView.as_view(pattern_name='login_vista', permanent=True)),
    path('login/register.html', RedirectView.as_view(pattern_name='register_view', permanent=True)),
    path('login/forgot.html', RedirectView.as_view(pattern_name='forgot_login', permanent=True)),
    path('cart.html', RedirectView.as_view(pattern_name='cart', permanent=True)),
    path('checkout.html', RedirectView.as_view(pattern_name='checkout', permanent=True)),
    path('compare.html', RedirectView.as_view(pattern_name='compare', permanent=True)),
    path('blog-grid.html', RedirectView.as_view(pattern_name='blog_grid', permanent=True)),
    path('blog-list.html', RedirectView.as_view(pattern_name='blog_list', permanent=True)),
    path('forgot.html', RedirectView.as_view(pattern_name='forgot', permanent=True)),
    path('coupon/contact/blog.html', RedirectView.as_view(pattern_name='coupon_contact_blog_html', permanent=True)),
    path('index/about.html', RedirectView.as_view(pattern_name='about', permanent=True)),
    path('about/login.html', RedirectView.as_view(pattern_name='about_login', permanent=True)),
    path('profile/index.html', RedirectView.as_view(pattern_name='profile', permanent=True)),

    # Plantillas directas
    path('index/profile.html', TemplateView.as_view(template_name='index/profile.html')),
    path('login/index.html', TemplateView.as_view(template_name='login/index.html')),
    path('404/', TemplateView.as_view(template_name='404.html'), name='error_404'),
    path('404/index.html', RedirectView.as_view(pattern_name='error_404', permanent=True)),
    path('login/forgot/404.html', RedirectView.as_view(pattern_name='error_404', permanent=True)),

    # Redirecciones adicionales limpias
    path('blog/blog/', RedirectView.as_view(pattern_name='blog', permanent=True)),
    path('blog/blog-grid/', RedirectView.as_view(pattern_name='blog_grid', permanent=True)),
    path('blog/blog-list/', RedirectView.as_view(pattern_name='blog_list', permanent=True)),
    path('blog/blog-details/', RedirectView.as_view(pattern_name='blog_details', permanent=True)),
    path('blog/blog-details-2/', RedirectView.as_view(pattern_name='nested_blog_details_2', permanent=True)),
    path('blog-details/blog-details/', RedirectView.as_view(pattern_name='blog_details', permanent=True)),
]

