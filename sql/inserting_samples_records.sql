INSERT INTO FUNCIONARIOS VALUES('00000000000', 'Alisson', 'Artista');
INSERT INTO FUNCIONARIOS VALUES('00000000001', 'João', 'Uber');

INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('20/10/2024 12:02', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('20/10/2024 20:30', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('21/10/2024 12:16', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('21/10/2024 20:18', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('22/10/2024 12:08', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('22/10/2024 20:12', 'DD/MM/YYYY HH24:MI'), '00000000000');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('21/10/2024 14:32', 'DD/MM/YYYY HH24:MI'), '00000000001');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('21/10/2024 22:49', 'DD/MM/YYYY HH24:MI'), '00000000001');
INSERT INTO PONTO VALUES(CODIGO_PONTO_SEQ.NEXTVAL, TO_DATE('22/10/2024 14:21', 'DD/MM/YYYY HH24:MI'), '00000000001');

COMMIT;