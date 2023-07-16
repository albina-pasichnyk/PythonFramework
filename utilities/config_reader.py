import configparser

config = configparser.RawConfigParser()
if not config.read('../configurations/config_file.ini'):  # to run from test file
    config.read('./configurations/config_file.ini')  # to run from terminal using marks


class ReadConfig:
    @staticmethod
    def get_app_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_user_creds():
        return config.get('user_data', 'token')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')
