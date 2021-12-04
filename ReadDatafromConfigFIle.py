from configparser import ConfigParser
config=ConfigParser()
config.read("D:\\RobotFramework\\config.cfg")
print(config.get('Details','Application_URL'))
print(config.get('Details','Browser_name'))