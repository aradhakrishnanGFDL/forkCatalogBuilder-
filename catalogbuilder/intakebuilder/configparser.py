import yaml
import os
class Config:
    def __init__(self, config):
        self.config = config
        with open(self.config, 'r') as file:
            configfile = yaml.safe_load(file)
        try:
            self.input_path = configfile['input_path']
        except:
            self.input_path = None
            print("input_path does not exist in config")
            pass
        try:
            self.output_path = configfile['output_path']
            #print("output_path :",self.output_path)
        except:
            self.output_path = None
            print("output_path does not exist in config")
            pass 
        try:
            self.headerlist = configfile['headerlist']
            print("headerlist :",self.headerlist)
        except:
            raise KeyError("headerlist does not exist in config")
        try:
            self.output_path_template = configfile['output_path_template']
            print("output_path_template :",self.output_path_template)
        except:
            raise KeyError("output_path_template does not exist in config")
        try:
            self.output_file_template = configfile['output_file_template']
            print("output_file_template :", self.output_file_template)
        except:
            raise KeyError("output_file_template does not exist in config")
        try:
            self.schema = configfile['schema']
            print("schema:", self.schema)
        except:
            self.schema = None
            pass

