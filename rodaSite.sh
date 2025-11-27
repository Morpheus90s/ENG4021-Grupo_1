#Rodei isso para abrir o site:
# bash rodaSite.sh

set -e

cd findress_site

echo "Limpando ambiente antigo..."
rm -rf venv

echo "Criando novo ambiente virtual..."
python3 -m venv venv

echo "Ativando ambiente..."
source venv/bin/activate

echo "Instalando Django e Pillow..."
pip install django pillow

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Iniciando servidor..."
python manage.py runserver 0.0.0.0:8001