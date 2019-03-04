# docker build -t todo-db .
# docker run -d --rm -e POSTGRES_PASSWORD=Password1! -p 5432:5432 todo-db
FROM postgres:11.2

EXPOSE 5432
COPY init.sh /docker-entrypoint-initdb.d/init.sh
