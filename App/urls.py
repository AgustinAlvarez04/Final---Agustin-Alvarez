from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns= [

    path("", inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('contact/', contact, name="Contact"),
    path('pages/', pages, name="Pages" ),
    path("blogs/", blogs, name="Blogs"),
    
    
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),

    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("crearBlog/", crearBlog, name="crearBlog"),
    path("buscarBlog/", buscarBlog, name="buscarBlog"),
    path("buscar/", buscar, name="buscar"),
    path("resultadosBlog/", resultadosBlog, name="resultadosBlog"),
    path("leerBlog/", leerBlog, name="leerBlog"),
    path("eliminarBlog/<id>", eliminarBlog, name="eliminarBlog"),
    path("editarBlog/<id>", editarBlog, name="editarBlog"),
    
]