import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def invoke_browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\\Python38\\browserexefiles\\chromedriver.exe",options=chrome_options)
    driver.maximize_window()
    driver.get("https://interview2.supporthive.com/staff/login")
    request.cls.driver = driver
    yield
    driver.close()

