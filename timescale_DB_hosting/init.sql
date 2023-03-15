GRANT ALL PRIVILEGES ON DATABASE mydb TO postgres;


CREATE TABLE Bengaluru_temperature (
    timestamp TIMESTAMPTZ NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    temperature_feels DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    wind_speed DOUBLE PRECISION,
    wind_direction DOUBLE PRECISION,
    visibility DOUBLE PRECISION,
    cloudiness DOUBLE PRECISION
);
CREATE TABLE Delhi_temperature (
    timestamp TIMESTAMPTZ NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    temperature_feels DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    wind_speed DOUBLE PRECISION,
    wind_direction DOUBLE PRECISION,
    visibility DOUBLE PRECISION,
    cloudiness DOUBLE PRECISION
);

SELECT create_hypertable('Bengaluru_temperature', 'timestamp');
SELECT create_hypertable('Delhi_temperature', 'timestamp');


