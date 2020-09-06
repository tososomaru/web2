import pandas as pd
from sqlalchemy import create_engine


errors = pd.read_csv(r'G:\NN\config\Predictive Maintenance\PdM_errors.csv')
errors.columns = [c.lower() for c in errors.columns]
failures = pd.read_csv(r'G:\NN\config\Predictive Maintenance\PdM_failures.csv')
failures.columns = [c.lower() for c in failures.columns]
machines = pd.read_csv(r'G:\NN\config\Predictive Maintenance\PdM_machines.csv')
machines.columns = [c.lower() for c in machines.columns]
maint = pd.read_csv(r'G:\NN\config\Predictive Maintenance\PdM_maint.csv')
maint.columns = [c.lower() for c in maint.columns]



engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')

errors.to_sql("errors_machine", engine)
failures.to_sql("failures", engine)
machines.to_sql("machines", engine)
maint.to_sql("maint_machine", engine)