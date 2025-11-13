"""
Django settings for backend_smart project.

Generado automáticamente por 'django-admin startproject'.
Adaptado para despliegue en Render con PostgreSQL, React frontend y CORS configurado.
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# -------------------------------
# RUTAS BASE
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# CONFIGURACIONES BÁSICAS
# -------------------------------
SECRET_KEY = config('SECRET_KEY', default='clave_de_prueba_segura')
DEBUG = config('DEBUG', default=False, cast=bool)

# ⚠️ Cambia * por tus dominios definitivos si quieres más seguridad
ALLOWED_HOSTS = [
    'backend-smartt.onrender.com',  # dominio backend
    'localhost',
    '127.0.0.1',
]

# -------------------------------
# API KEYS (seguras en variables de entorno)
# -------------------------------
API_KEY_IMGBB = config('API_KEY_IMGBB', default='')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default='')

# -------------------------------
# APLICACIONES INSTALADAS
# -------------------------------
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'corsheaders',

    # Apps propias
    'autenticacion_usuarios',
    'dashboard_inteligente',
    'productos',
    'reportes_dinamicos',
    'ventas_carrito',
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Debe ir arriba del CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# CORS Y CSRF
# -------------------------------
CORS_ALLOWED_ORIGINS = [
    'https://frontend_smartt.onrender.com',  # tu dominio de frontend
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'https://backend_smartt.onrender.com',
    'https://frontend_smartt.onrender.com',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True  # porque Render usa HTTPS

# -------------------------------
# URLS Y WSGI
# -------------------------------
ROOT_URLCONF = 'backend_smart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_smart.wsgi.application'

# -------------------------------
# BASE DE DATOS (PostgreSQL en Render)
# -------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600,
    )
}

# -------------------------------
# VALIDADORES DE CONTRASEÑA
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# INTERNACIONALIZACIÓN
# -------------------------------
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_TZ = True

# -------------------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# -------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if (BASE_DIR / 'static').exists():
    STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------------
# REST FRAMEWORK
# -------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

# -------------------------------
# AUTO FIELD
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
