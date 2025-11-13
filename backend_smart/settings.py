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
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

def _split_env_list(value: str):
    return [item.strip() for item in value.split(',') if item.strip()]


ALLOWED_HOSTS = _split_env_list(config(
    'ALLOWED_HOSTS',
    default='backend-smartt.onrender.com'
))

# -------------------------------
# API KEYS (variables de entorno)
# -------------------------------
API_KEY_IMGBB = config('API_KEY_IMGBB', default='')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET', default='')

# -------------------------------
# ENDPOINT DE CONFIGURACIÓN (solo despliegues)
# -------------------------------
ENABLE_SETUP_ENDPOINT = config('ENABLE_SETUP_ENDPOINT', default=False, cast=bool)
SETUP_ADMIN_USERNAME = config('SETUP_ADMIN_USERNAME', default='admin')
SETUP_ADMIN_EMAIL = config('SETUP_ADMIN_EMAIL', default='admin@example.com')
SETUP_ADMIN_PASSWORD = config('SETUP_ADMIN_PASSWORD', default='')
SETUP_ADMIN_TOKEN = config('SETUP_ADMIN_TOKEN', default='')

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
    'corsheaders.middleware.CorsMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Debe ir antes del CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# CORS Y CSRF
# -------------------------------
CORS_ALLOWED_ORIGINS = _split_env_list(config(
    'CORS_ALLOWED_ORIGINS',
    default='https://frontend-smartt.onrender.com'
))

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['*']

CSRF_TRUSTED_ORIGINS = _split_env_list(config(
    'CSRF_TRUSTED_ORIGINS',
    default='https://backend-smartt.onrender.com,https://frontend-smartt.onrender.com'
))

# -------------------------------
# DEBUG LOG PARA RENDER (solo temporal)
# -------------------------------
print("🚀 CORS_ALLOWED_ORIGINS:", CORS_ALLOWED_ORIGINS)
print("🚀 CSRF_TRUSTED_ORIGINS:", CSRF_TRUSTED_ORIGINS)
print("🚀 ALLOWED_HOSTS:", ALLOWED_HOSTS)


SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True  # Render usa HTTPS

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
# BASE DE DATOS (Render / local)
# -------------------------------
DATABASE_URL = config('DATABASE_URL')

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=config('DB_CONN_MAX_AGE', default=600, cast=int),
        ssl_require=config('DB_SSL_REQUIRE', default=True, cast=bool)
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
