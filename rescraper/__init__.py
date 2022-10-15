#!/usr/bin/env python
# coding: utf-8

# # REAL ESTATE SCRAPER

# Initial Link (replacing page number, is exists):

import csv
import math
import gettext
import requests
from bs4          import BeautifulSoup
from urllib.parse import urlparse, urlunparse

class REBaseProfile():
    """Real Estate Scraper Base Profile
    
    url: initial page url.
         If more than one page will be scraped, page number parameter as "{}"
         must be in the url to be replaced by the page number.
    
    nPages: number of pages to scrape.
            Scraper will start at 1 and stop at nPages.
    
    params: parameters for web requests.
    
    headers: for web requests."""
    
    def __init__(self, url, fields, nPages = 1, headers = {}, params = {}):
        self.url     = url
        self.fields  = fields
        self.nPages  = nPages
        self.headers = headers
        self.params  = params
        self.parser  = 'html.parser'
    
    
    @property
    def fields(self):
        return self._fields
    # fields = property(fget=get_fields, fset=set_fields, doc=gettext("scraper fields"))
    
    @fields.setter
    def fields(self, value):
        self._fields = None
        if value:
            if isinstance(value, list):
                self._fields = value
            else:
                print("{0} is not an List object! Setting 'None' for fields.".format(value))
        else:
            print("Setting 'None' for fields.".format(value))
    
    @property
    def url(self):
        return self._url.geturl()
    # url = property(fget=get_url, fset=set_url, doc=gettext("initial page url"))
    
    @url.setter
    def url(self, value):
        if value:
            self._url     = urlparse(value)
            self.url_base = urlunparse(self._url[:2] + ('', '', None, None))
        
    def safe_text(self, obj, currency=False, strip = True):
        result = obj
        if obj:
            result = obj.text
            if not currency:
                # TODO: implement locale string replacement
                result = result.replace('R$', '')
            if strip:
                result = result.strip()
        return result
    
    def get_data(self, pages):
        result = []
        return result

class REScraper():
    """Real Estate Scraper"""
    
    def __init__(self, profile):
        self.profile = profile
        self.data    = []
        self.pages   = []
    
    @property
    def profile(self):
        return self._profile
    # profile = property(fget=get_profile, fset=set_profile, doc=gettext("scraper profile"))
    
    @profile.setter
    def profile(self, value):
        self._profile = None
        if value:
            if isinstance(value, REBaseProfile):
                self._profile = value
            else:
                print("{0} is not an REBaseProfile object! Setting 'None' as scraper profile.".format(value))
        else:
            print("Setting 'None' as scraper profile.".format(value))
    
    def get_pages(self):
        self.pages = []
        for nPage in range(1, self.profile.nPages):
            if self.profile.nPages > 1:
                urlN      = self.profile.url.format(nPage)
            else:
                urlN      = self.profile.url
            responseN = requests.get(urlN, headers=self.profile.headers, params=self.profile.params)
            if responseN.status_code >= 300:
                if responseN.status_code >= 400:
                    print("Client or Server error response: {0}.".format(responseN.status_code))
                    self.profile.nPages = nPage
                    break
                else:
                    print("Redirection response: {0}. If you don't get the page, take out 'if-modified-since' from headers.".format(responseN.status_code))
            self.pages.append(BeautifulSoup(responseN.content, self.profile.parser))
    
    def get_data(self):
        self.data = self.profile.get_data(self.pages, self.profile.url_base)
    
    def save_csv(self, filename):
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = self.profile.fields)
            writer.writeheader()
            writer.writerows(self.data)
