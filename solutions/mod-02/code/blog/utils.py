# -*- coding: utf-8 -*-


class Utils:

    # (private) format a name by replacing spaces with dots
    @staticmethod
    def __format_name(name):
        return name.lower().replace(' ', '.')

    # (private) convert a name into an email address
    @staticmethod
    def __convert_to_email(self, name, domain=None):
        return self.__format_name(name) + "@" + domain

    # (private) convert a name into a blog's home url
    @staticmethod
    def __convert_to_home_url(self, name, domain=None):
        return 'http://blog.' + domain + '/' + self.__format_name(name)

    # get the blog emails
    @staticmethod
    def get_emails(self, names, domains=None):
        return [self.__convert_to_email(name, domain) for (name, domain) in zip(names, domains)]

    # get the home blog urls
    @staticmethod
    def get_home_urls(self, names, domains=None):
        return [self.__convert_to_home_url(name, domain) for (name, domain) in zip(names, domains)]
