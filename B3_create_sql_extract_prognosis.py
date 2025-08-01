# Generate sql script to extract patient followup for each condition
# Requires tables containing patients for inclusion

from A0_global_vars_py import *

s = ''

for pln in ['gold', 'aurum']:
  s += f'--- {pln.upper()}\n'
  for condition in conditions:
    s += f'-- {condition.upper()} {pln}\n'
    s += f'''drop table if exists {sql_schema}.{pln}_{condition}_death;
create table {sql_schema}.{pln}_{condition}_death as (
    select c.patid, datediff(p.deathdate, c.diagdate) as death
    from {sql_schema}.{pln}_{condition}_patients c 
    left join atlas_followup.{pln}_cleaned_patients p on p.patid = c.patid
);\n\n'''
    s += f'''drop table if exists {sql_schema}.{pln}_{condition}_hosp;
create table {sql_schema}.{pln}_{condition}_hosp as (
    select c.patid, c.diagdate, f.admidate, f.discharged
    from {sql_schema}.{pln}_{condition}_patients c
    inner join atlas_data.{pln}_apc_hospitalisations f on f.patid = c.patid
    where ((f.admidate > c.diagdate) or ((f.discharged > c.diagdate) and (f.discharged is not null)))
    and f.admidate is not null
    and datediff(f.admidate, c.diagdate) <= 365
);\n\n'''

with open(rf'{filepath}\B4_extract_prognosis.sql', 'w') as output_file:
    output_file.write(s)
