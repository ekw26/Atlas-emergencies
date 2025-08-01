These scripts are dependent on sql schemas containing tables of eligible patients, patient characteristics (such as year of birth, gender, IMD, and comorbidities, date of death), and HES APC and A&E records.

To use these files first populate relevant variables in the A0 scripts indicating the working directory, the sql schema in which patient tables are stored and new tables should be created, and the schemas in which dependent data are stored. In particular the 'sql_schema' should contain for every population (pln) and condition to be considered:
(a) a table named {pln}_{condition}_patients (e.g., gold_AS_patients) containing the patient ID (patid), diagnosis date (diagdate), source of diagnosis (datasource), practice ID (pracid), year of birth (yob), gender, IMD twentile (imd), start date (i.e., current registration date or practice up to standard date), and death date (if applicable) for every patient with the condition of interest that meets the eligibility criteria for the study.
(b) a table named all_{pln}_patients (e.g., all_gold_patients) incorporating all rows of all {pln}_{condition}_patients tables in order to derive table 1 summary statistics.
(c) a table named {pln}_{condition}_launders (e.g., gold_AS_launders) containing the patient ID (patid), comorbidity, earliest record date of that comorbidity (recorddate), and the number of days between the recorddate and the diagnosis date for the condition of interest (ttd) for every patient in the corresponding patient table ({pln}_{condition}_patients) and for each comorbidity from the Launders comorbidity index that they have a primary care record for.

The data schema should contain all data tables for the study (e.g., HES APC tables, HES A&E tables), whilst the lookup schema should contain lookups for HES and CPRD data as provided by CPRD.
Further the A0 files should include the parameters need to connect to these sql schemas - namely the hostname, username, password, database name, and port.

Then to run the analyses run the following scripts in order:
1. B1_create_sql_extract_followup.py - creates the script B2_extract_patient_followup.sql including the relevant queries for every condition defined in the A0 files.
2. B2_extract_patient_followup.sql - extracts data on emergency admissions and attendances before the diagnosis date for each patient and condition of interest.
3. B3_create_sql_extract_prognosis.py - creates the script B4_extract_prognosis.sql including the relevant queries for every condition defined in the A0 files. 
4. B4_extract_prognosis.sql - extracts data on deaths and inpatient admissions in the year after diagnosis for each patient and condition of interest.
5. C1_table1.Rmd - produces table 1 summary statistics for each CPRD population
6. C2_run_analyses.Rmd - defines the presence of an emergency diagnosis, death in the year after diagnosis, and time spent in hospital in the year after diagnosis for each patient. From this carries out analyses of the frequency and prognostic implications of emergency diagnosis.
7. C3_report_EDs.Rmd - takes the outputs produced from C2_run_analyses.Rmd to produce tables and figures summarising the findings.