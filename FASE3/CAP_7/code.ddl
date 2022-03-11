-- Gerado por Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   em:        2021-11-18 22:56:03 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_reg_alim (
    id_reg_alim          RAW(16) NOT NULL,
    nm_registro          VARCHAR2(30) NOT NULL,
    vl_calorias          VARCHAR2(8) NOT NULL,
    vl_descricao         VARCHAR2(120),
    dt_registro          DATE NOT NULL,
    t_usuario_id_usuario RAW(16) NOT NULL
);

ALTER TABLE t_reg_alim ADD CONSTRAINT t_registro_alimentacao_pk PRIMARY KEY ( id_reg_alim );

CREATE TABLE t_reg_ativ (
    id_reg_ativ          RAW(16) NOT NULL,
    nm_atividade         VARCHAR2(30) NOT NULL,
    vl_calorias          VARCHAR2(8) NOT NULL,
    vl_tempo             VARCHAR2(8) NOT NULL,
    vl_descricao         VARCHAR2(120),
    dt_registro          DATE NOT NULL,
    t_usuario_id_usuario RAW(16) NOT NULL
);

ALTER TABLE t_reg_ativ ADD CONSTRAINT t_registro_atividade_pk PRIMARY KEY ( id_reg_ativ );

CREATE TABLE t_sessao (
    id_sessao            RAW(16) NOT NULL,
    dt_ultimasessao      DATE NOT NULL,
    t_usuario_id_usuario RAW(16) NOT NULL
);

ALTER TABLE t_sessao ADD CONSTRAINT t_sessao_pk PRIMARY KEY ( id_sessao );

CREATE TABLE t_usuario (
    id_usuario     RAW(16) NOT NULL,
    nm_funcionario VARCHAR2(80) NOT NULL,
    dt_nascimento  DATE NOT NULL,
    vl_altura      VARCHAR2(4) NOT NULL,
    vl_peso        VARCHAR2(4) NOT NULL,
    vl_imc         VARCHAR2(3) NOT NULL,
    vl_username    VARCHAR2(40) NOT NULL,
    vl_hashedpass  RAW(50) NOT NULL
);

ALTER TABLE t_usuario ADD CONSTRAINT t_usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE t_reg_alim
    ADD CONSTRAINT t_reg_alim_t_usuario_fk FOREIGN KEY ( t_usuario_id_usuario )
        REFERENCES t_usuario ( id_usuario );

ALTER TABLE t_reg_ativ
    ADD CONSTRAINT t_reg_ativ_t_usuario_fk FOREIGN KEY ( t_usuario_id_usuario )
        REFERENCES t_usuario ( id_usuario );

ALTER TABLE t_sessao
    ADD CONSTRAINT t_sessao_t_usuario_fk FOREIGN KEY ( t_usuario_id_usuario )
        REFERENCES t_usuario ( id_usuario );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
