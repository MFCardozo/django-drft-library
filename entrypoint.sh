#!/usr/bin/env bash
set -e

 # Load env
if [ -f ".env" ]; then
    # Exporta todas las variables de .env de manera segura
    set -a
    source .env
    set +a
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput
# crea admin
python manage.py create_admin
# crear datos de prueba
python manage.py seed

exec "$@"