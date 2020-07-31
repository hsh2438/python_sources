import configparser

""" create config file """
config = configparser.ConfigParser()

config['database'] = {}
config['database']['host'] = '127.0.0.1'
config['database']['port'] = '3306'
config['database']['user'] = 'user01'
config['database']['passwd'] = 'passwd01'
config['database']['db_name'] = 'test'
config['database']['charset'] = 'utf8'

with open('config.ini', 'w') as configfile:
    config.write(configfile)

