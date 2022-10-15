#!/usr/bin/env python
# coding: utf-8

import requests
from bs4       import BeautifulSoup
from rescraper import REBaseProfile

class REVivaRealProfile(REBaseProfile):
    """Real Estate Scraper Profile for Viva Real Site"""
    
    def __init__(self, url, fields, nPages=1, headers={}, params={}):
        REBaseProfile.__init__(self, url, fields, nPages=nPages, headers=headers, params=params)
    
    def get_data(self, pages, url_base):
        result = REBaseProfile.get_data(self, pages)
        
        for pageN in pages:
            ads  = pageN.find_all('a', class_="property-card__content-link js-card-title")
            
            for ad in ads:
                link         = url_base + ad['href']
                
                endereco     = self.safe_text(ad.find('span', class_="property-card__address"))
                
                area         = self.safe_text(ad.find('span', class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area"))
                
                qtdQuartos   = ad.find('li', class_="property-card__detail-item property-card__detail-room js-property-detail-rooms")
                if qtdQuartos:
                    qtdQuartos = self.safe_text(qtdQuartos.find('span', class_="property-card__detail-value js-property-card-value"))
                
                qtdBanheiros = ad.find('li', class_="property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom")
                if qtdBanheiros:
                    qtdBanheiros = self.safe_text(qtdBanheiros.find('span', class_="property-card__detail-value js-property-card-value"))
                
                qtdVagas     = ad.find('li', class_="property-card__detail-item property-card__detail-garage js-property-detail-garages")
                if qtdVagas:
                    qtdVagas = self.safe_text(qtdVagas.find('span', class_="property-card__detail-value js-property-card-value"))
                
                valor        = ad.find('div', class_="property-card__price js-property-card-prices js-property-card__price-small")
                if valor:
                    valor = self.safe_text(valor.find('p'))
                
                condominio   = ad.find('div', class_="property-card__price-details--condo")
                if condominio:
                    condominio = self.safe_text(condominio.find('strong'))
                
                responseAd = requests.get(link, headers=self.headers, params=self.params)
                pageAd     = BeautifulSoup(responseAd.content, self.parser)
                
                iptu       = self.safe_text(pageAd.find('span', class_="price__list-value iptu js-iptu"))
                
                # criado sob demanda na pagina, ou seja, nao eh possivel por codigo por enquanto
                # informante = self.safe_text(pageAd.find('a', class_="publisher__name"))
                
                result.append({'link': link, 'endereco': endereco, 'area': area, 'qtdQuartos': qtdQuartos, 'qtdBanheiros': qtdBanheiros, 'qtdVagas': qtdVagas, 'valor': valor, 'condominio': condominio, 'iptu': iptu})
        return result
