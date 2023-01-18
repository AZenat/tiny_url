import os
from configparser import ConfigParser


class Config():

    def __init__(self):
        cfg = ConfigParser()
        cfg.read("config/application.conf")
        # API configuration
        self.__api_protocol = cfg['api']['protocol']
        self.api_host = cfg['api']['host']
        self.api_port = int(cfg['api']['port'])
        self.api_base_url = f"{self.__api_protocol}://{self.api_host}:{self.api_port}"
        self.api_secret_key = cfg['api']['secret_key']
        # DB configuration
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.__db_engine = cfg["database"]["engine"]
        self.__db_data_dir = cfg["database"]["data_dir"]
        self.__db_file_name = cfg["database"]["file_name"]
        db_path = f"{root_dir}/{self.__db_data_dir}/{self.__db_file_name}"
        self.db_url = f"{self.__db_engine}:///{db_path}"
