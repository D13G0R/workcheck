📌 Sistema de Gestión Colaborativa de Tareas (SGCT)
🧠 Descripción

SGCT es una aplicación web orientada a la gestión de tareas en entornos colaborativos. Permite a múltiples usuarios organizar su trabajo mediante grupos, donde pueden crear, asignar y dar seguimiento a tareas, manteniendo control de acceso basado en roles.

El sistema está diseñado bajo una arquitectura cliente-servidor, separando completamente el frontend y el backend.

🎯 Objetivo

Facilitar la organización y colaboración entre usuarios mediante:

Creación de grupos de trabajo
Gestión de miembros mediante invitaciones
Administración de tareas
Organización por categorías
Asignación de responsabilidades

🏗️ Tecnologías utilizadas
Backend
Django REST Framework
PostgreSQL
Frontend
React

📦 Dependencias principales
Backend
Django
Django REST Framework
PostgreSQL
Gunicorn
Whitenoise

⚙️ Funcionalidades principales
Registro e inicio de sesión de usuarios
Creación y gestión de grupos
Invitación de usuarios por correo electrónico
Sistema de roles (administrador / miembro)
Creación, edición y eliminación de tareas
Asignación de tareas a usuarios
Organización de tareas por categorías
Comentarios en tareas
Registro de actividad dentro del sistema

🔐 Control de acceso

El sistema implementa restricciones basadas en:

Pertenencia

Un usuario solo puede acceder a los grupos a los que pertenece.

Roles
Administrador:
Invitar usuarios
Gestionar miembros
Administrar el grupo
Miembro:
Crear y gestionar tareas
Comentar
🔗 Modelo de datos (visión general)

El sistema está basado en un modelo relacional que incluye:

Usuarios
Grupos
Relación Usuario-Grupo (muchos a muchos con roles)
Tareas
Categorías
Invitaciones
Comentarios
Registro de actividad

🔄 Flujos principales
1. Registro

El usuario crea una cuenta en el sistema.

2. Creación de grupo

Un usuario crea un grupo y se asigna como administrador.

3. Invitación

El administrador invita usuarios al grupo mediante correo.

4. Gestión de tareas

Los usuarios crean, asignan y actualizan tareas dentro del grupo.

5. Colaboración

Los usuarios pueden comentar en tareas.

🌐 Arquitectura

El sistema está dividido en dos repositorios:

Backend

Encargado de:

lógica de negocio
autenticación
validaciones
acceso a datos
Frontend

Encargado de:

interfaz de usuario
consumo de la API

🚀 Instalación y ejecución
Backend
Clonar el repositorio
Crear entorno virtual
Instalar dependencias
Configurar variables de entorno
Ejecutar migraciones
Iniciar servidor
Frontend
Clonar el repositorio
Instalar dependencias
Configurar URL del backend
Ejecutar servidor

🛡️ Seguridad
Autenticación basada en tokens
Validación de permisos en backend
Restricción de acceso por grupo
Protección contra acceso no autorizado
📊 Escalabilidad

El sistema está preparado para:

múltiples usuarios simultáneos
múltiples grupos independientes
separación de responsabilidades entre cliente y servidor
🧠 Decisiones de diseño
Uso de relación muchos a muchos con roles
Separación frontend/backend
Control de acceso basado en pertenencia a grupo
Organización de tareas por categorías
Uso de invitaciones para control de miembros
👤 Autor

Diego Alejandro Rodríguez

📌 Estado del proyecto

En desarrollo / funcional (ajusta esto según tu avance)