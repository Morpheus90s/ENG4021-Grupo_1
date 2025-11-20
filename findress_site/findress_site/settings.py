"""
Django settings for findress_site project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! IMPORTANTE: MANTENHA A SUA SECRET_KEY ORIGINAL !!!
# !!! COLE A SUA CHAVE QUE JÁ ESTÁ NO SEU ARQUIVO AQUI !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
SECRET_KEY = 'django-insecure-!m_8vnt0q%1jfl9ggb*mp$^m@thw%xf=978r)q!qc@!di)0co@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# --- CONFIGURAÇÃO DE ACESSO (ALLOWED_HOSTS) ---
ALLOWED_HOSTS = [
    '.app.github.dev', # Permite qualquer link do Codespace
    'localhost',
    '127.0.0.1',
]


# --- APLICAÇÕES INSTALADAS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'closet',   # Nosso app de roupas
    'usuario',  # Nosso app de usuários
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "findress_site.urls"

# --- CONFIGURAÇÃO DOS TEMPLATES (HTML) ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [], 
        "APP_DIRS": True, 
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "findress_site.wsgi.application"


# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# --- Internacionalização ---
LANGUAGE_CODE = "pt-br" 
TIME_ZONE = "America/Sao_Paulo" 
USE_I18N = True
USE_TZ = True


# --- CONFIGURAÇÃO DE ESTILO (CSS) ---
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# --- CONFIGURAÇÃO DE IMAGENS (Uploads) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- CORREÇÃO DO ERRO 403 (CSRF) ---
# Adicionamos explicitamente a porta 8001 aqui
CSRF_TRUSTED_ORIGINS = [
    'https://studious-chainsaw-6xwv5vq9qw93r757-8000.app.github.dev',
    'https://studious-chainsaw-6xwv5vq9qw93r757-8001.app.github.dev', # Link externo porta 8001
    'https://localhost:8000',
    'http://localhost:8000',
    # --- AQUI ESTÃO AS LINHAS QUE CORRIGEM O SEU ERRO ATUAL ---
    'https://localhost:8001', 
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    # ----------------------------------------------------------
    'https://*.app.github.dev',
]