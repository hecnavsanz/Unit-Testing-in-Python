# -*- coding: utf-8 -*-


class Utils:

    # get the emails
    @staticmethod
    def get_emails(names, domains):
        return [name.lower().replace(' ', '.') + "@" + domain for (name, domain) in zip(names, domains)]

    # get the home blog urls
    @staticmethod
    def get_home_urls(names, domains):
        return ['http://blog.' + domain + '/' + name.lower().replace(' ', '.')
                for (name, domain) in zip(names, domains)]
