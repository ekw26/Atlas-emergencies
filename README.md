# Description
Code for analyses examining the frequency and prognostic implications of emergency diagnoses in 18 conditions
These scripts are dependent on sql schemas containing tables of eligible patients, patient characteristics (such as year of birth, gender, IMD, and comorbidities, date of death), and HES APC and A&E records.

To use these files first populate relevant variables in the A0 scripts indicating the working directory, the sql schema in which patient tables are stored and new tables should be created, and the schemas in which dependent data are stored. In particular the 'sql_schema' should contain for every population (pln) and condition to be considered:
<ol type="a">
  <li>a table named {pln}_{condition}_patients (e.g., gold_AS_patients) containing the patient ID (patid), diagnosis date (diagdate), source of diagnosis (datasource), practice ID (pracid), year of birth (yob), gender, IMD twentile (imd), start date (i.e., current registration date or practice up to standard date), and death date (if applicable) for every patient with the condition of interest that meets the eligibility criteria for the study.</li>
  <li>a table named all_{pln}_patients (e.g., all_gold_patients) incorporating all rows of all {pln}_{condition}_patients tables in order to derive table 1 summary statistics.</li>
  <li>a table named {pln}_{condition}_launders (e.g., gold_AS_launders) containing the patient ID (patid), comorbidity, earliest record date of that comorbidity (recorddate), and the number of days between the recorddate and the diagnosis date for the condition of interest (ttd) for every patient in the corresponding patient table ({pln}_{condition}_patients) and for each comorbidity from the Launders comorbidity index that they have a primary care record for.</li>
</ol>

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

# Session information
Scripts were originally run in Python (version 3.8.5), MySQL 8.0.41, and R (version 4.4.1). 
Session information and package versions at the time of analysis were as follows:

R version 4.4.1 (2024-06-14 ucrt) Platform: x86_64-w64-mingw32/x64 Running under: Windows Server 2019 x64 (build 17763)

Matrix products: default

locale: [1] LC_COLLATE=English_United Kingdom.1252 [2] LC_CTYPE=English_United Kingdom.1252
[3] LC_MONETARY=English_United Kingdom.1252 [4] LC_NUMERIC=C
[5] LC_TIME=English_United Kingdom.1252

time zone: Europe/London tzcode source: internal

attached base packages: [1] stats graphics grDevices utils datasets methods base

other attached packages: [1] ggstance_0.3.7 ggrepel_0.9.6 glue_1.8.0 flextable_0.9.7 [5] lubridate_1.9.4 forcats_1.0.0 stringr_1.5.1 dplyr_1.1.4
[9] purrr_1.0.4 readr_2.1.5 tidyr_1.3.1 tibble_3.2.1
[13] ggplot2_3.5.1 tidyverse_2.0.0

loaded via a namespace (and not attached): [1] generics_0.1.3 fontLiberation_0.1.0 xml2_1.3.6
[4] stringi_1.8.4 hms_1.1.3 digest_0.6.37
[7] magrittr_2.0.3 evaluate_1.0.3 grid_4.4.1
[10] timechange_0.3.0 fastmap_1.2.0 plyr_1.8.9
[13] zip_2.3.2 scales_1.3.0 fontBitstreamVera_0.1.1 [16] textshaping_1.0.0 cli_3.6.4 crayon_1.5.3
[19] rlang_1.1.5 fontquiver_0.2.1 bit64_4.6.0-1
[22] munsell_0.5.1 withr_3.0.2 yaml_2.3.10
[25] gdtools_0.4.1 parallel_4.4.1 tools_4.4.1
[28] officer_0.6.7 uuid_1.2-1 tzdb_0.4.0
[31] colorspace_2.1-1 vctrs_0.6.5 R6_2.6.1
[34] lifecycle_1.0.4 bit_4.5.0.1 vroom_1.6.5
[37] ragg_1.3.3 pkgconfig_2.0.3 pillar_1.10.1
[40] gtable_0.3.6 data.table_1.16.4 Rcpp_1.0.14
[43] systemfonts_1.2.1 xfun_0.51 tidyselect_1.2.1
[46] rstudioapi_0.17.1 knitr_1.49 farver_2.1.2
[49] htmltools_0.5.8.1 rmarkdown_2.29 compiler_4.4.1
[52] askpass_1.2.1 openssl_2.3.2


