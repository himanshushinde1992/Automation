import unittest

import pytest

from pages.loginpagetest import loginpage
from utils.customLogger import customLogger as log


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = loginpage(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.gt.invalid_login()

    @pytest.mark.run(order=2)
    def test_Sso(self):
        self.gt.valid_sso_login()
        log.allurelogs("sucess")


