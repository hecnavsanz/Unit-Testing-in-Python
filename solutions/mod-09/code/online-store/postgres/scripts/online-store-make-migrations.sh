CWD=$(pwd)

cd /solutions/mod-09/code/online-store/eshop

# create built-in Django models
python manage.py migrate

# create custom models sql
python manage.py makemigrations products

# create custom models in the database
python manage.py migrate products

# insert records into the database
docker cp /solutions/mod-09/code/online-store/postgres/scripts/products-and-product-categories-records-postgres.sql postgres:/tmp/products-and-product-categories-records-postgres.sql
docker exec -it postgres bash -c 'psql --username=postgres --file=/tmp/products-and-product-categories-records-postgres.sql eshop_db'

# create test user
python manage.py shell <<EOF
from django.contrib.auth.models import User

user = User.objects.create_user('test','test@labs.io','Pytest-TDD.Labs_4ALL')
user.save()
EOF

cd $CWD
