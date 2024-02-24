import yaml
from typing import Union


class _Configs:
    _configs: dict

    @classmethod
    def _init_configs(cls) -> None:
        with open('configs.yaml', 'r', encoding="utf8") as f:
            cls._configs = yaml.load(f, Loader=yaml.FullLoader)


class LoggerConfigs(_Configs):
    _config_name = 'logging'

    @classmethod
    def is_console(cls) -> int:
        return cls._configs[cls._config_name]['console']

    @classmethod
    def file(cls) -> str:
        return cls._configs[cls._config_name]['file']

    @classmethod
    def level(cls) -> str:
        return cls._configs[cls._config_name]['level']


class DatabaseConfigs(_Configs):
    _config_name = 'database'

    @classmethod
    def user(cls):
        return cls._configs[cls._config_name]['user']

    @classmethod
    def name(cls):
        return cls._configs[cls._config_name]['base_name']

    @classmethod
    def password(cls):
        return cls._configs[cls._config_name]['password']

    @classmethod
    def host(cls):
        return cls._configs[cls._config_name]['host']

    @classmethod
    def port(cls):
        return cls._configs[cls._config_name]['port']


class DocumentsConfigs(_Configs):
    _config_name = 'documents'

    @classmethod
    def sample_exemption(cls):
        return cls._configs[cls._config_name]['sample_exemption_dir']

    @classmethod
    def sample_thanks(cls):
        return cls._configs[cls._config_name]['sample_thanks_dir']

    @classmethod
    def institut_name(cls, num: int):
        return cls._configs[cls._config_name]['instituts'][num]

    @classmethod
    def director_name(cls, num: int):
        return cls._configs[cls._config_name]['directors_names'][num]


def start():
    _Configs._init_configs()

start()



