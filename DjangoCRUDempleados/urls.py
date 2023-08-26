"""
URL configuration for DjangoCRUDempleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Login/Register
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home_login'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('tasks/', views.tasks_view, name='tasks'),
    # CRUD - Empleados
    path('home_crud', login_required(views.home_crud), name='home_crud'),
    path('registrarEmpleado/', login_required(views.registrarEmpleado), name="registrarEmpleado"),
    path('edicionEmpleado/<codigo>', login_required(views.edicionEmpleado), name="edicionEmpleado"),
    path('editarEmpleado/', login_required(views.editarEmpleado), name="editarEmpleado"),
    path('eliminarEmpleado/<codigo>', login_required(views.eliminarEmpleado), name="eliminarEmpleado")
]
