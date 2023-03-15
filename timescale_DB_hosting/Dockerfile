FROM timescale/timescaledb:latest-pg14

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB mydb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

