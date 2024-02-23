import yaml
from typing import Union


class _Configs:
    configs: dict

    @classmethod
    def init_configs(cls) -> None:
        with open('configs.yaml', 'r') as f:
            cls.configs = yaml.load(f, Loader=yaml.FullLoader)


class Logger(_Configs):
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


class Database(_Configs):
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


class Documents(_Configs):
    config_name = 'documents'

    @classmethod
    def sample_exemption(cls):
        return cls.configs[cls.config_name]['sample_exemption_dir']

    @classmethod
    def sample_thanks(cls):
        return cls.configs[cls.config_name]['sample_thanks_dir']


def start():
    _Configs.init_configs()


start()
print(Database.user())
