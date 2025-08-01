# Generate sql script to extract patient followupfor each condition
# Requires tables containing patients for inclusion and hospitalisations and ae attendances data

from A0_global_vars_py import *

s = ''

for pln in ['gold', 'aurum']:
  s += f'--- {pln.upper()} ---\n'
  for condition in conditions:
    s += f'-- {condition.upper()}\n'
    s += f'''
drop table if exists {sql_schema}.{pln}_{condition}_admissions;
create table {sql_schema}.{pln}_{condition}_admissions as (
	select c.patid, f.admidate, a.description
    from {sql_schema}.{pln}_{condition}_patients c
    inner join {data_schema}.{pln}_apc_hospitalisations f on f.patid = c.patid
    left join {lookup_schema}.apc_admimeth a on f.admimeth = a.admimeth
	where ((a.category = 'Emergency') or (a.category = 'Other MH'))
    and f.admidate <= c.diagdate
	and f.admidate >= c.startdate
	and f.admidate is not null
);

drop table if exists {sql_schema}.{pln}_{condition}_attends;
create table {sql_schema}.{pln}_{condition}_attends as (
	select c.patid, f.arrivaldate, f.aepatgroup
	from {sql_schema}.{pln}_{condition}_patients c
	inner join {data_schema}.{pln}_ae_attendance f on f.patid = c.patid
	where f.arrivaldate <= c.diagdate
	and f.arrivaldate >= c.startdate
	and f.arrivaldate is not null
);

\n\n'''
    
with open(rf'{filepath}\B2_extract_patient_followup.sql', 'w') as output_file:
    output_file.write(s)

