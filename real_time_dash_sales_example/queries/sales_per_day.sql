select
    c.nrcnpj as "cnpj",
    c.dsfantasia as "nome_fantasia",
    c.dsrazaosocial as "razao_social",
    t.dttempo as "data",
    sum(f.vltotalliquido) AS "valor",
    sum(f.qtitem) AS "quantidade"
from
  vendas