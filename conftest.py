# test_config is a configuration file which can be used to set the configuration for your tests
# You will put that code in this files which will run before your tests will run and after you tests will end.

import pytest

@pytest.fixture(scope="function", autouse=True)
def setbrowserconfig(page) -> None:    
    page.goto("https://console.stg.intelcloud.cnvrg.io/#/", timeout=0)
    yield page
