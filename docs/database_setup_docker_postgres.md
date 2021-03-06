## Docker Postgres Setup

* Install Docker v19.03.1 or later.
* Download a database dump file

1) Use Docker to run a Postgres container:

```
docker run --rm --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:9.6
```

2) Connect to the Docker container using a bash shell:

```
docker exec -it postgres /bin/bash
```

3) In the Docker container, create a "usmai_dw" user:

```
docker> su - postgres
docker> createuser usmai_dw
```

4) In the Docker container, run "psql":

```
docker> psql -U postgres
```

5) In psql, create the "usmai_dw_etl" database, and exit:

```
postgres=# CREATE DATABASE usmai_dw_etl;
postgres=# CREATE ROLE usmai_dw;
postgres=# <Ctrl-D>
```



## Populate database from a dump

6) In a separate (non-Docker) terminal, use "docker cp" to copy the database dump file into the "/tmp" directory of the "postgres" container:

```
docker cp <DATABASE_DUMP_FILENAME> postgres:/tmp
```

where \<DATABASE_DUMP_FILENAME> is the name of the database dump. For example, if the name of the database dump is "dump-usmai_dw_etl9.custom.Tuesday-pm", the command would be:

```
docker cp dump-usmai_dw_etl9.custom.Tuesday-pm postgres:/tmp
```

7) In the Docker container, switch to the "/tmp" directory and and restore the dump:

```
docker> cd /tmp
docker> pg_restore -d usmai_dw_etl -U postgres <DATABASE_DUMP_FILENAME>
```

where \<DATABASE_DUMP_FILENAME> is the name of the database dump. For example, if the  database dump file was named "dump-usmai_dw_etl9.custom.Tuesday-pm", the command would be:

```
docker> pg_restore -d usmai_dw_etl -U postgres dump-usmai_dw_etl9.custom.Tuesday-pm
```

8) In the ".env" file the following properties can be used:

```
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'usmai_dw_etl'
DB_HOST_NAME= '127.0.0.1'
DB_PORT= '5432'
```
