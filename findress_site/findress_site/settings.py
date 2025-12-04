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
# ... (Mantenha todo o código anterior até chegar na parte 8)

# -----------------------------------------------------------------
# 8. CONFIGURAÇÕES DE LOGIN/LOGOUT E SEGURANÇA (CORRIGIDO)
# -----------------------------------------------------------------

# Login/Logout
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# E-mail no console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- CORREÇÃO DO CSRF (403 Forbidden) ---

# Confia em qualquer subdomínio do GitHub Codespaces e Localhost (HTTP e HTTPS)
CSRF_TRUSTED_ORIGINS = [
    'https://*.app.github.dev',
    'https://*.github.dev',
    'http://localhost:8000',
    'http://localhost:8001',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8001',
    # Adicionando versões HTTPS para localhost (Resolve o seu erro específico)
    'https://localhost:8000',
    'https://localhost:8001',
    'https://127.0.0.1:8000',
    'https://127.0.0.1:8001',
]

# Essas configurações ajudam quando o site roda atrás de um proxy (como o Codespace)
# (Corrigido erro de digitação de SSE para USE)
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Esta linha é CRUCIAL para o Django saber que o Codespaces é seguro (estava comentada/quebrada antes)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Opcional: Se continuar dando erro, descomente a linha abaixo TEMPORARIAMENTE para testar
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True