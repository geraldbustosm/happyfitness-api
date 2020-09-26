-- CREATING DATABASE

CREATE TABLE sedes (
    id serial PRIMARY KEY,
    nombre VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE motivos (
    id serial PRIMARY KEY,
    sede_id INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    correlativo INT NOT NULL,
    FOREIGN KEY (sede_id)
        REFERENCES sede(id)
);

CREATE TABLE votaciones (
    id serial PRIMARY KEY,
    motivo_id INT NOT NULL,
    calificacion INT NOT NULL,
    razon TEXT,
    FOREIGN KEY (motivo_id)
        REFERENCES motivo(id)
);

-- INTIALIZICING WITH DATA
INSERT INTO sedes(nombre) VALUES ('Santuario');
INSERT INTO sedes(nombre) VALUES ('El Milagro');
INSERT INTO sedes(nombre) VALUES ('Coquimbo');

INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Baños', 1);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Música', 2);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Ambiente', 3);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Iluminación', 4);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Profesores', 5);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Aseo', 6);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Aroma', 7);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (1, 'Otros', 8);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (2, 'Precios', 1);
INSERT INTO motivos(sede_id, nombre, correlativo) VALUES (2, 'Personal', 2);

INSERT INTO votaciones(motivo_id, calificacion, razon) VALUES (1, 1, 'Mal olor');
INSERT INTO votaciones(motivo_id, calificacion, razon) VALUES (2, 2, 'Música desmotivante');
INSERT INTO votaciones(motivo_id, calificacion, razon) VALUES (6, 3, 'Pasillos sucios');
INSERT INTO votaciones(motivo_id, calificacion) VALUES (9, 4);