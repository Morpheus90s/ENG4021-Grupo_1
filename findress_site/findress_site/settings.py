"""
Django settings for findress_site project.
"""

from pathlib import Path

# -----------------------------------------------------------------
# 1. DEFINIÇÃO DO CAMINHO BASE (CRUCIAL - DEVE VIR PRIMEIRO)
# -----------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------
# 2. SEGURANÇA E DEBUG
# -----------------------------------------------------------------
# Mantive a sua chave original que vi nos logs anteriores
SECRET_KEY = 'django-insecure-!m_8vnt0q%1jfl9ggb*mp$^m@thw%xf=978r)q!qc@!di)0co@'

# Mantenha True para desenvolvimento
DEBUG = True

ALLOWED_HOSTS = [
    '.app.github.dev', 
    'localhost', 
    '127.0.0.1'
]

# -----------------------------------------------------------------
# 3. APLICAÇÕES
# -----------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'closet',   # Seu app
    'usuario',  # Seu app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'findress_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Agora BASE_DIR já existe!
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

WSGI_APPLICATION = 'findress_site.wsgi.application'

# -----------------------------------------------------------------
# 4. BANCO DE DADOS
# -----------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # Usa BASE_DIR
    }
}

# -----------------------------------------------------------------
# 5. VALIDAÇÃO DE SENHA
# -----------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------------
# 6. INTERNACIONALIZAÇÃO
# -----------------------------------------------------------------
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------
# 7. ARQUIVOS ESTÁTICOS E MÍDIA
# -----------------------------------------------------------------
STATIC_URL = 'static/'

# O erro acontecia aqui porque BASE_DIR não existia antes
STATICFILES_DIRS = [
    BASE_DIR / 'static', 
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------
# 8. CONFIGURAÇÕES DE LOGIN/LOGOUT E SEGURANÇA (ATIVIDADE 4)
# -----------------------------------------------------------------

# Login/Logout
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# E-mail no console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CSRF (Correção do erro 403)
CSRF_TRUSTED_ORIGINS = [
    'https://studious-chainsaw-6xwv5vq9qw93r757-8000.app.github.dev',
    'https://studious-chainsaw-6xwv5vq9qw93r757-8001.app.github.dev',
    'https://localhost:8000',
    'http://localhost:8000',
    'https://localhost:8001',
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    'https://*.app.github.dev',
]