with sumariza_funcionarios as (
    select f.cpf
        ,  f.nome
        ,  f.cargo
        from funcionarios f
        order by f.nome
)

select p.codigo_ponto as codigo_ponto
    ,  sf.cpf
    ,  sf.nome
    ,  sf.cargo
    ,  TO_CHAR(p.data_hora, 'DD/MM/YYYY HH24:MI') as data_hora
    from ponto p
    inner join sumariza_funcionarios sf
    on p.cpf = sf.cpf
    order by p.codigo_ponto