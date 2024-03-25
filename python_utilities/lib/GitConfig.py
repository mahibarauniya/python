import utils.logutils as lu
import yaml

class GitConfig(object):
    def __init__(self, product, yaml, tmpLocation, debug):
        self.product     = product
        self.yaml        = yaml
        self.tmpLocation = tmpLocation if tmpLocation else "D:\gitrepository\\tmp"
        self.debug       = debug



    def _parse_yaml(self, yaml_file):
        lu.log_message_debug(self.debug, "parsing input yaml file in Class GitConfig......")

        with open (yaml_file, "r") as file:
            data = yaml.safe_load(file) #yaml.load(file, Loaded=yaml.SafeLoader)  ## yaml.full_load as well but safeloader is safest way to load aymal file
            return data  #Now 'data' contains the contents of the YAML file as a Python dictionary

    def _display_attributes(self):
        for attribute in dir(self):   #dir() function returns a list of valid attributes and methods for an object.
            if not (attribute.startswith("_") or attribute.startswith("init")  or attribute.startswith("_parse_yaml")  or attribute.startswith("initialize_variable")):
                print(attribute, ":", getattr(self, attribute))


    def initialize_variable(self):
        lu.log_message("Initialing the variables after loading the yaml file", "INFO")
        data = self._parse_yaml(self.yaml)
        self.source_repo_name          = data[self.product]["source"]["name"]
        self.source_repo_url           = data[self.product]["source"]["repo_url"]
        self.source_branch_name        = data[self.product]["source"]["branch_name"]
        self.source_folder_to_include  = data[self.product]["source"]["folder_to_include"]
        self.source_files_to_exclude   = data[self.product]["source"]["files_to_exclude"]

        self.target_repo_name          = data[self.product]["target"]["name"]
        self.target_repo_url           = data[self.product]["target"]["repo_url"]
        self.target_branch_name        = data[self.product]["target"]["branch_name"]
        self.target_folder_to_include  = data[self.product]["target"]["folder_to_include"]
        self.target_files_to_exclude   = data[self.product]["target"]["files_to_exclude"]

        if self.debug:
            lu.log_message_debug(self.debug, "debug mode is ON [ True ] so displaying all the attributes of the class")
            self._display_attributes()