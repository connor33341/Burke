import json

with open('Config/config.json','r') as configdata:
    config = json.load(configdata)
elua = config['elua'] # DO NOT BYPASS
burke_version = config['version']
