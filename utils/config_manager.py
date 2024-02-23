import yaml
from typing import Union


class Configs:
    configs: dict

    @classmethod
    def init_configs(cls) -> None:
        with open('configs.yaml', 'r') as f:
            cls.configs = yaml.load(f, Loader=yaml.FullLoader)


class Logger(Configs):
    config_name = 'logging'

    @classmethod
    def is_console(cls) -> int:
        return cls.configs[cls.config_name]['console']

    @classmethod
    def file(cls) -> str:
        return cls.configs[cls.config_name]['file']

    @classmethod
    def level(cls) -> str:
        return cls.configs[cls.config_name]['level']


class Database(Configs):
    config_name = 'database'

    @classmethod
    def user(cls):
        return cls.configs[cls.config_name]['user']

    @classmethod
    def name(cls):
        return cls.configs[cls.config_name]['base_name']

    @classmethod
    def password(cls):
        return cls.configs[cls.config_name]['password']

    @classmethod
    def host(cls):
        return cls.configs[cls.config_name]['host']

    @classmethod
    def port(cls):
        return cls.configs[cls.config_name]['port']


def start():
    Configs.init_configs()


start()
print(Database.user())
