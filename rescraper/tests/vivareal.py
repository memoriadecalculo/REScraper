#!/usr/bin/env python
# coding: utf-8

from rescraper                   import REScraper
from rescraper.profiles.vivareal import REVivaRealProfile

url     = "https://www.vivareal.com.br/venda/sp/santos/apartamento_residencial/?pagina={}#banheiros=2&quartos=2"
fields  = ['link', 'endereco', 'area', 'qtdQuartos', 'qtdBanheiros', 'qtdVagas', 'valor', 'condominio', 'iptu']
nPages  = 2
params  = {}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '__cfruid=b5950fdc04ba83069d6ae6f80f7c867ec72d8167-1665498123; new_vivareal_user_id_generation_date=Tue Oct 11 2022 11:22:09 GMT-0300 (HorÃ¡rio PadrÃ£o de BrasÃ­lia); new_vivareal_user_id=f3db595d-2d9f-4ed4-bef2-d8ef5cfb14c6; v_user_journey=1; v_user_journey_start=1; _gcl_au=1.1.100646375.1665498131; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22UHRL6YpIWVoRIpRh6Rkj%22%7D; _fbp=fb.2.1665498137238.1390066945; cookie-notifier=1; __gads=ID=96e8d673b849d84b:T=1665498138:S=ALNI_MZaeSLErzpOWJ7fzz83Fzluzl7hBw; _hjSessionUser_1729147=eyJpZCI6IjJjNmI1NTZmLTliM2EtNWVmYS1iZjcyLTM5NGIyZThmZDlhMCIsImNyZWF0ZWQiOjE2NjU0OTgxMzYwNDMsImV4aXN0aW5nIjp0cnVlfQ==; persistent_search=cGVyc2lzdGVudDo6dHJ1ZQ==; QSI_SI_41GDGa82WnPngQC_intercept=true; _gid=GA1.3.906432279.1665782401; _hjIncludedInSessionSample=0; _hjSession_1729147=eyJpZCI6ImIwZmUxZGYzLWIzMGItNGMwZi04YTU1LTlhYzIzOGZhNTYyNCIsImNyZWF0ZWQiOjE2NjU3ODI0MDcyMzUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __gpi=UID=0000097dba5678fb:T=1665498138:RT=1665782408:S=ALNI_MbIJ1ap0eGZtlG9cYzIsjX5L9jbpA; user_lat_lng=-15.779:-47.934; _gat_UA-126375-31=1; cto_bundle=mNON819MbzhmUGhCT1Z5ZWwycjhLeVFMSUxIYWdUZXpmZWdqRFZsbjk3Nmk3RnJqYUIlMkZaTVF6RmllYnZjY01sSXhGWTNTSG5GTGhzdG81clU5VFF3UTNwOUZ4ZSUyRnE1cmp5c2I2cDNEa21acjBpUUZ2eDJyVTBDdCUyQlZlV2NtcVRYRExJVzUyM1IlMkYzclZpJTJGSHNpd0wzZ0ltV0pnJTNEJTNE; _ga=GA1.3.1929628268.1665498127; _ga_GTHV18HK7H=GS1.1.1665782402.6.1.1665782513.0.0.0; _ga_SP7M9MSCB3=GS1.1.1665782404.6.1.1665782513.35.0.0; QSI_CT={"saleRankingRendered":25}',
    'dnt': '1',
    'referer': 'https://www.vivareal.com.br/venda/sp/santos/apartamento_residencial/?pagina=2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

VivaRealTeste   = REVivaRealProfile(url=url, fields=fields, nPages=nPages, headers=headers, params=params)
VivaRealScraper = REScraper(VivaRealTeste)
VivaRealScraper.get_pages()
VivaRealScraper.get_data()
VivaRealScraper.save_csv('vivareal.csv')