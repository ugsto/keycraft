from keycraft.config.cli_connector import CliConnector
from keycraft.config.config_builder import ConfigBuilder
from keycraft.config.env_connector import EnvConnector


class ConfigLoader:
    @staticmethod
    def load_config():
        return (
            ConfigBuilder()
            .merge(EnvConnector.build_config())
            .merge(CliConnector.build_config())
            .build()
        )
