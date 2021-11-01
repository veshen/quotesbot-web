# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
	  'https://www.ssongwatches.com/collections/vintage/angelus',
	  'https://www.ssongwatches.com/collections/vintage/accurist',
	  'https://www.ssongwatches.com/collections/vintage/aristo',
	  'https://www.ssongwatches.com/collections/vintage/avia',
	  'https://www.ssongwatches.com/collections/vintage/benrus',
	  'https://www.ssongwatches.com/collections/vintage/breguet',
	  'https://www.ssongwatches.com/collections/vintage/breitling',
	  'https://www.ssongwatches.com/collections/vintage/bulova',
	  'https://www.ssongwatches.com/collections/vintage/camy',
	  'https://www.ssongwatches.com/collections/vintage/certina',
	  'https://www.ssongwatches.com/collections/vintage/clebar',
	  'https://www.ssongwatches.com/collections/vintage/croton',
	  'https://www.ssongwatches.com/collections/vintage/cyma',
	  'https://www.ssongwatches.com/collections/vintage/doxa',
	  'https://www.ssongwatches.com/collections/vintage/eberhard',
	  'https://www.ssongwatches.com/collections/vintage/eterna',
	  'https://www.ssongwatches.com/collections/vintage/favre-leuba',
	  'https://www.ssongwatches.com/collections/vintage/gallet',
	  'https://www.ssongwatches.com/collections/vintage/gigandet',
	  'https://www.ssongwatches.com/collections/vintage/girard-perregaux',
	  'https://www.ssongwatches.com/collections/vintage/grana',
	  'https://www.ssongwatches.com/collections/vintage/grand-seiko',
	  'https://www.ssongwatches.com/collections/vintage/hamilton',
	  'https://www.ssongwatches.com/collections/vintage/heuer',
	  'https://www.ssongwatches.com/collections/vintage/iwc',
	  'https://www.ssongwatches.com/collections/vintage/jaeger',
	  'https://www.ssongwatches.com/collections/vintage/jaeger-lecoultre',
	  'https://www.ssongwatches.com/collections/vintage/jardur',
	  'https://www.ssongwatches.com/collections/vintage/lanco',
	  'https://www.ssongwatches.com/collections/vintage/lemania',
	  'https://www.ssongwatches.com/collections/vintage/leonidas',
	  'https://www.ssongwatches.com/collections/vintage/lip',
	  'https://www.ssongwatches.com/collections/vintage/longines',
	  'https://www.ssongwatches.com/collections/vintage/lordial',
	  'https://www.ssongwatches.com/collections/vintage/meylan',
	  'https://www.ssongwatches.com/collections/vintage/mido',
	  'https://www.ssongwatches.com/collections/vintage/minerva',
	  'https://www.ssongwatches.com/collections/vintage/moeris',
	  'https://www.ssongwatches.com/collections/vintage/movado',
	  'https://www.ssongwatches.com/collections/vintage/mulco',
	  'https://www.ssongwatches.com/collections/vintage/nivada',
	  'https://www.ssongwatches.com/collections/vintage/omega',
	  'https://www.ssongwatches.com/collections/vintage/orvis',
	  'https://www.ssongwatches.com/collections/vintage/patek-philippe',
	  'https://www.ssongwatches.com/collections/vintage/record',
	  'https://www.ssongwatches.com/collections/vintage/recta',
	  'https://www.ssongwatches.com/collections/vintage/richard',
	  'https://www.ssongwatches.com/collections/vintage/rolex',
	  'https://www.ssongwatches.com/collections/vintage/seiko',
	  'https://www.ssongwatches.com/collections/vintage/smiths',
	  'https://www.ssongwatches.com/collections/vintage/technos',
	  'https://www.ssongwatches.com/collections/vintage/tenexact',
	  'https://www.ssongwatches.com/collections/vintage/tissot',
	  'https://www.ssongwatches.com/collections/vintage/tollet',
	  'https://www.ssongwatches.com/collections/vintage/tudor',
	  'https://www.ssongwatches.com/collections/vintage/trematic',
	  'https://www.ssongwatches.com/collections/vintage/ulysse-nardin',
	  'https://www.ssongwatches.com/collections/vintage/universal-geneve',
	  'https://www.ssongwatches.com/collections/vintage/vixa',
	  'https://www.ssongwatches.com/collections/vintage/vetta',
	  'https://www.ssongwatches.com/collections/vintage/wakmann',
	  'https://www.ssongwatches.com/collections/vintage/wittnauer',
	  'https://www.ssongwatches.com/collections/vintage/wyler',
	  'https://www.ssongwatches.com/collections/vintage/yema',
	  'https://www.ssongwatches.com/collections/vintage/zenith',
	  'https://www.ssongwatches.com/collections/vintage/zodiac'
	]
    def parse(self, response):
        for quote in response.css("div.global-product-each"):
            yield {
                'name': quote.css("div.global-product-content-details > h4.header::text").extract_first(),
                'url':response.url
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

