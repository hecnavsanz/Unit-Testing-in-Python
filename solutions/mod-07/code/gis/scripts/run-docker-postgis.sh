
sudo mkdir -p $HOME/postgis

docker pull postgis/postgis

docker run -d --name postgis \
    -e POSTGRES_PASSWORD=Pytest-TDD.Labs_4ALL \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /home/labs/postgis:/var/lib/postgresql/data \
	-p 8080:5432 \
    postgis/postgis

