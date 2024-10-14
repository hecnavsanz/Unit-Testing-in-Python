# -*- coding: utf-8 -*-
from utils import Utils


class TestUtils:

    # test the get_emails function
    def test_get_emails(self):

        # utils instance
        utils = Utils()

        # author name and email test cases (the third test case has a typo in the email)
        test_cases = [{"name": 'Ferren Adrea', "domain": "labs.io", "email": 'ferren.adrea@labs.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea', "domain": "recip.es", "email": 'dane.garcea@recip.es'}]

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]

    def test_another_get_emails(self):

        # utils instance
        utils = Utils()

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "labs.io", "email": 'ferren.adrea@labs.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea', "domain": "recip.es", "email": 'dane.garcea@recip.esss'}]

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]
