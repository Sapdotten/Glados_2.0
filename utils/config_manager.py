import yaml
from typing import Union


class Configs:
    configs: dict

    @classmethod
    def init_configs(cls) -> None:
        with open('configs.yaml', 'r') as f:
            cls.configs = yaml.load(f, Loader=yaml.FullLoader)


class Logger(Configs):
    @classmethod
    def is_console(cls) -> int:
        return cls.configs['logging']['console']

    @classmethod
    def file(cls) -> str:
        return cls.configs['logging']['file']


def start():
    Configs.init_configs()
