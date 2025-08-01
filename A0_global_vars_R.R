# file for storing variables
filepath <- ""
conditions <- c('AS', 'brain_tumours', 'celiac', 'CHD', 'colon_cancer', 'COPD', 'IBD', 'lung_cancer', 'lyme', 'MS', 'ovarian_cancer', 'pancreatic_cancer', 'parkinsons', 'PCOS', 'RA', 'SBE', 'schizophrenia', 'TB')
results_filepath <- ""
analysis_dt <- "2025-01-01"

# sql schemas/tables that are called in scripts
sql_schema <- 'atlas_emergency'
data_schema <- 'atlas_data'
lookup_schema <- 'atlas_lookups'

# sql connection details
host <- '' 
user <- ''
password <- ''
dbname <- ''
port <- 1