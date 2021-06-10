import yaml 
import io


def read_yaml():
    with open('config/config.yaml', 'r') as stream:
        ymldata = yaml.safe_load(stream)
        #print(ymldata)
        return ymldata


   
