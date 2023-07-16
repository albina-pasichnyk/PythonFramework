import pytest

from utilities.config_reader import ReadConfig
from utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_app_base_url())
    yield driver
    driver.quit()
