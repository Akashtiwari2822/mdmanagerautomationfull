from selenium import webdriver
import pytest
from clear_cache import clear as clear_cache
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome"], scope='class')
# @pytest.fixture(params=["chrome", "firefox", "edge"], scope='class')
def init_driver(request):
    clear_cache(dir=".")
    print("======================================= setup ========================================")

    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service)
    if request.param == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        web_driver = webdriver.Edge(service=service)
    web_driver.maximize_window()
    # delete_cache(web_driver)
    request.cls.driver = web_driver
    # request.cls.driver = web_driver

    yield
    print("======================================= close setup ========================================")
    web_driver.close()
