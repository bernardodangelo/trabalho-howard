select p.codigo_ponto
    ,  TO_CHAR(p.data_hora, 'DD/MM/YYYY HH24:MI') as data_hora
    ,  f.nome as funcionarios
    from ponto p
    inner join funcionarios f
    on p.cpf = f.cpf
    order by p.codigo_ponto
