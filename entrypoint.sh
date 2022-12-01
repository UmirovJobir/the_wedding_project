
#!/bin/bash


if [ "$DATABASE" = "wedding_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

sleep 10

echo "Chmod entrypoint.sh"
chmod +x entrypoint.sh

echo "Apply database migrations"
python3 manage.py migrate

# echo "collectstatic"
python3 manage.py collectstatic

echo "initadmin"
python3 manage.py initadmin

echo "Starting server"
python3 manage.py runserver --insecure 0.0.0.0:8000

exec "$@"

