import configparser

config = configparser.ConfigParser()
config.read('./config.conf')

print('\n ===== Dev configs =====')
ENV_VAR = 'DEV'
schema_raw = config.get(ENV_VAR, "param1")
schema_stage = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', schema_raw)
print('Value of param2 is = ', schema_stage)

print('\n ===== QA configs =====')
ENV_VAR = 'QA'
schema_raw = config.get(ENV_VAR, "param1")
schema_stage = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', schema_raw)
print('Value of param2 is = ', schema_stage)

print('\n===== PROD configs =====')
ENV_VAR = 'PROD'
schema_raw = config.get(ENV_VAR, "param1")
schema_stage = config.get(ENV_VAR, "param2")
print('Value of param1 is = ', schema_raw)
print('Value of param2 is = ', schema_stage)