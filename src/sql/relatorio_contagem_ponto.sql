WITH sumariza_funcionarios AS (
    SELECT p.codigo_ponto,
           TO_CHAR(p.data_hora, 'DD/MM/YYYY HH24:MI') AS data_hora,
           f.cpf
    FROM ponto p
    INNER JOIN funcionarios f ON p.cpf = f.cpf
    ORDER BY p.codigo_ponto
)

SELECT f.nome AS funcionarios,
       COUNT(1) AS contagem,
       f.cargo AS cargo
FROM funcionarios f
INNER JOIN sumariza_funcionarios sp ON f.cpf = sp.cpf
GROUP BY f.nome, f.cargo
ORDER BY f.nome