'''
Created on 22 nov. 2018

@author: tuco
'''
import discogs_client
from tuco.org.tucotheque.server import config

client = discogs_client.Client('tuco.org.tucotheque.server/1.0', user_token=config.get('libraries.discogs.token'))

def search(barcode=None):
    results = []
    page = 0
    page_max = None
    
    while page is not page_max:
        page += 1
        discogs_results = client.search(barcode=barcode, page=page, type='release')

        page_max = discogs_results.pages
        
        for release in discogs_results:
            results.append({'source': 'discogs', 'id': release.id})
        
    return results