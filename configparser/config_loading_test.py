import configparser


""" read config file """
config = configparser.ConfigParser()
config.read('config.ini')
 
print(config['database']['host'])
print(config['database']['port'])
print(config['database']['user'])
print(config['database']['passwd'])
print(config['database']['db_name'])
print(config['database']['charset'])
