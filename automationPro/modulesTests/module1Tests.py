import pytest
from selenium.webdriver.common.by import By

from automationPro.commonLibs.Utilities import capital_case
from selenium import webdriver
import selenium


def test_test1():
    assert capital_case('semaphore') == 'Semaphore'
    print("hello")


@pytest.mark.smoke
def test_k():
    assert capital_case('semaphore') == 'Semaphore'
    print("hello")


@pytest.mark.smoke
@pytest.mark.api
def test_test3():
    assert capital_case('semaphore') == 'Semaphore'
    print("hello")


@pytest.mark.regression
def test_test4():
    assert capital_case('semaphore') == 'Semaphore'
    print("hello")


@pytest.mark.gui
def test_test5():
    driver_path = "C:/Users/Deepak Dontineni/Downloads/chromedriver_win32_1/chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.get("https://www.simplilearn.com")
    # System.setProperty("webdriver.chrome.driver","C:\\Users\\Deepak Dontineni\\Downloads\\chromedriver_win32\\chromedriver.exe");
    driver.find_element(By.XPATH, "//input[@type='search']").click()
    # driver.quit()
