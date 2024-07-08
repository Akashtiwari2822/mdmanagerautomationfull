from selenium import webdriver
import pytest
from clear_cache import clear as clear_cache
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["chrome", "firefox", "edge", "safari"], scope='class')
def init_driver(request):
    clear_cache(dir=".")
    print("======================================= setup ========================================")

    try:
        if request.param == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            web_driver = webdriver.Chrome(service=service)
        elif request.param == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            web_driver = webdriver.Firefox(service=service)
        elif request.param == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            web_driver = webdriver.Edge(service=service)
        elif request.param == "safari":
            web_driver = webdriver.Safari()

        web_driver.maximize_window()
        request.cls.driver = web_driver

        yield
    except Exception as e:
        print(f"Error during driver initialization: {e}")
    finally:
        print("======================================= close setup ========================================")
        try:
            web_driver.quit()
        except Exception as e:
            print(f"Error closing the browser: {e}")
