import pytest
import time

from base.driverclass import Driver


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    global driver
    print("before class")
    driver1 = Driver()
    driver = driver1.getDriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()


@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
