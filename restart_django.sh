#!/bin/bash

echo "🚫 Zastavuji kontejnery..."
sudo docker compose down

echo "🧹 Mazání starých obrazů (volitelné)..."
# sudo docker image prune -f  # Odkomentuj, pokud chceš čistit i staré image

echo "🔨 Překompiluji docker kontejnery..."
sudo docker compose build

echo "🚀 Spouštím kontejnery..."
sudo docker compose up -d

echo "⌛ Čekám 5 sekund, než se kontejnery nahodí..."
sleep 5

echo "🛠️ Provádím migrace..."
sudo docker compose exec web python manage.py makemigrations
sudo docker compose exec web python manage.py migrate

echo "📦 Načítám statické soubory..."
# sudo docker compose exec web python manage.py collectstatic --noinput  # volitelné

echo "👑 Vytvářím superuživatele admin/admin@admin.com (pokud neexistuje)..."
sudo docker compose exec web python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@admin.com').exists():
    User.objects.create_superuser(
        email='admin@admin.com',
        password='admin',
        first_name='Admin',
        last_name='User'
    )
    print('✅ Superuživatel admin@admin.com/admin vytvořen.')
else:
    print('ℹ️ Superuživatel admin@admin.com již existuje.')
"


echo "✅ Hotovo! Přístup na: http://localhost:8000"
