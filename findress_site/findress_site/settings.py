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
SECRET_KEY = "django-insecure-!m_8vnt0q%1jfl9ggb*mp$^m@thw%xf=978r)q!qc@!di)0co@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# --- CONFIGURAÇÃO DE ACESSO (PARA O CODESPACE FUNCIONAR) ---
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
        "DIRS": [], # O Django vai procurar na pasta 'templates' de cada app
        "APP_DIRS": True, # Esta linha é a mais importante
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
# ... (deixe como está no seu arquivo) ...
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# --- Internacionalização ---
LANGUAGE_CODE = "pt-br" # Mudado para Português
TIME_ZONE = "America/Sao_Paulo" # Mudado para Fuso Horário de São Paulo
USE_I18N = True
USE_TZ = True


# --- CORREÇÃO 1: CONFIGURAÇÃO DE ESTILO (CSS) ---
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = "static/"

# 
# ESTA LINHA ESTAVA FALTANDO. 
# Ela diz ao Django para também procurar arquivos CSS na pasta 'static'
# que fica na raiz do seu projeto (findress_site/static/css/style.css)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# --- CONFIGURAÇÃO DE IMAGENS (Uploads) ---
MEDIA_URL = '/media/'
# Diz ao Django para salvar os uploads de imagem na pasta 'media'
MEDIA_ROOT = BASE_DIR / 'media' 


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- CORREÇÃO 2: CORREÇÃO DO ERRO 403 (CSRF) ---
# A sua versão tinha um link em Markdown. Esta é a versão correta em Python.
CSRF_TRUSTED_ORIGINS = [
    'https://studious-chainsaw-6xwv5vq9qw93r757-8000.app.github.dev',
    'https://localhost:8000', # Necessário por causa do erro 403
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://*.app.github.dev' # Curinga para todos os Codespaces
]

