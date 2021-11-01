
# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        "https://www.ssongwatches.com/collections/modern?page=1",
    ]

    def parse(self, response):
        for quote in response.css("div.global-product-each"):
            yield {
                'images': quote.css("div.global-image-con > img::attr(src)").extract(),
                'title': quote.css("div.global-product-content-details > h4.header::text").extract_first(),
                'price': quote.css("div.global-product-content-details > div.global-price::text").extract_first(),
                'id': quote.css("a::attr(href)").extract_first(),
            }

        next_page_url = response.css("div.global-pages  > a.right-arrow::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.ssongwatches.com/products/omega-speedmaster-speedy-tuesday-ultraman',
        'https://www.ssongwatches.com/products/vacheron-constantin-historiques-triple-calendrier-1942',
        'https://www.ssongwatches.com/products/rolex-yachtmaster-40-116655-everose',
        'https://www.ssongwatches.com/products/omega-speedmaster-racing-tin-tin-1',
        'https://www.ssongwatches.com/products/tudor-black-bay-harrods-edition-1',
        'https://www.ssongwatches.com/products/jaeger-lecoultre-master-compressor-diving-alarm-navy-seals',
        'https://www.ssongwatches.com/products/nomos-metro-chronometer-for-hodinkee',
        'https://www.ssongwatches.com/products/rolex-submariner-16610-full-set',
        'https://www.ssongwatches.com/products/rolex-datejust-36mm-blue-116234',
        'https://www.ssongwatches.com/products/omega-speedmaster-apollo-11-50th-anniversary',
        'https://www.ssongwatches.com/products/iwc-aquatimer-2000-titanium',
        'https://www.ssongwatches.com/products/patek-philippe-calatrava-pilot-travel-time-5524g',
        'https://www.ssongwatches.com/products/audemars-piguet-royal-oak-dual-time-26120st',
        'https://www.ssongwatches.com/products/maitres-du-temps-chapter-three-reveal',
        'https://www.ssongwatches.com/products/jaeger-lecoultre-master-ultra-thin-perpetual-calendar',
        'https://www.ssongwatches.com/products/audemars-piguet-royal-oak-offshore-bumblebee',
        'https://www.ssongwatches.com/products/h-moser-cie-mayu-fume-dial',
        'https://www.ssongwatches.com/products/omega-speedmaster-apollo-soyuz-meteorite',
        'https://www.ssongwatches.com/products/zenith-el-primero-for-hodinkee',
        'https://www.ssongwatches.com/products/tudor-black-bay-harrods-edition',
        'https://www.ssongwatches.com/products/tudor-black-bay-bronze',
        'https://www.ssongwatches.com/products/omega-speedmaster-skywalker-x-33'
    ]

    def parse(self, response):
        for quote in response.css("div.product-content-each"):
            yield {
                'productYear': quote.css("div.product-year::text").extract_first(),
                'title': quote.css("h1.product-product-header::text").extract_first(),
                'productPrice': quote.css("#product-price::text").extract_first(),
                'productDescription': quote.css("div.product-description > div.rte > p.p1 > span.s1::text").extract(),
                'productCr': quote.css("div.product-cr > div.rte > p::text").extract_first(),
                'images': quote.css("div.image-gallery-each > img::attr(src)").extract(),
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = ["https://www.ssongwatches.com/products/rolex-cosmograph-daytona-6263","https://www.ssongwatches.com/products/rolex-double-red-sea-dweller-mk-2-tropical","https://www.ssongwatches.com/products/tudor-monte-carlo-7159","https://www.ssongwatches.com/products/heuer-carrera-2447s","https://www.ssongwatches.com/products/longines-sei-tacche-35mm","https://www.ssongwatches.com/products/zenith-a-271-chronograph","https://www.ssongwatches.com/products/movado-m95-sub-sea-4","https://www.ssongwatches.com/products/rolex-submariner-5513-non-serif","https://www.ssongwatches.com/products/rolex-submariner-5513-meters-first","https://www.ssongwatches.com/products/grand-seiko-6155-8000","https://www.ssongwatches.com/products/rolex-explorer-ref-1016-gilt","https://www.ssongwatches.com/products/lemania-royal-air-force-series-3","https://www.ssongwatches.com/products/mulco-prima-spillman-chronograph","https://www.ssongwatches.com/products/angelus-cal-215-l-e-hungarian-air-force","https://www.ssongwatches.com/products/camy-sports-chronograph","https://www.ssongwatches.com/products/breitling-avi-765","https://www.ssongwatches.com/products/vetta-oversized-chronograph","https://www.ssongwatches.com/products/clebar-supercompressor-1","https://www.ssongwatches.com/products/lemania-105-chronograph","https://www.ssongwatches.com/products/leonidas-cp-2-esercito-italiano-italian-army","https://www.ssongwatches.com/products/bulova-oversized-supercompressor-1","https://www.ssongwatches.com/products/richard-triple-calendar-chronograph","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675-8-president","https://www.ssongwatches.com/products/rolex-cosmograph-daytona-6265-yellow-gold","https://www.ssongwatches.com/products/rolex-explorer-ii-1657","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1676","https://www.ssongwatches.com/products/rolex-gmt-master-ii-16760-coke-fat-lady","https://www.ssongwatches.com/products/tudor-oysterdate-7962-t-a-rahman","https://www.ssongwatches.com/products/heuer-autavia-2446-second-execution","https://www.ssongwatches.com/products/rolex-explorer-ref-1017","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675-mk-iv","https://www.ssongwatches.com/products/patek-philippe-calatrava-3445-rose","https://www.ssongwatches.com/products/rolex-gmt-master-ref-16750-spider-dial","https://www.ssongwatches.com/products/heuer-carrera-dato-45-ref-3147n-3","https://www.ssongwatches.com/products/patek-philippe-3579-steel","https://www.ssongwatches.com/products/rolex-day-date-1803-linen-dial-1","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675-gilt","https://www.ssongwatches.com/products/zenith-el-primero-a-387","https://www.ssongwatches.com/products/jaeger-lecoultre-mk-12","https://www.ssongwatches.com/products/rolex-explorer-ref-1016-tropical-gilt","https://www.ssongwatches.com/products/rolex-datejust-1601-white-gold","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675-fuchsia","https://www.ssongwatches.com/products/mido-multi-centerchrono","https://www.ssongwatches.com/products/heuer-autavia-3646-second-execution","https://www.ssongwatches.com/products/zenith-el-primero-a-386","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675-yellow-gold","https://www.ssongwatches.com/products/rolex-red-submariner-1680-mk-iv","https://www.ssongwatches.com/products/rolex-day-date-1803-ghost-dial","https://www.ssongwatches.com/products/rolex-day-date-1803-matte-blue-dial","https://www.ssongwatches.com/products/rolex-day-date-1803-matte-grey-brown","https://www.ssongwatches.com/products/rolex-day-date-1803-linen-dial","https://www.ssongwatches.com/products/iwc-aquatimer-812-ad","https://www.ssongwatches.com/products/zodiac-heuer-carrera-12-dato-2547ns","https://www.ssongwatches.com/products/eberhard-scafograf-300","https://www.ssongwatches.com/products/jaeger-lecoultre-jumbo-memovox-e855","https://www.ssongwatches.com/products/rolex-explorer-ii-1656","https://www.ssongwatches.com/products/heuer-autavia-7763","https://www.ssongwatches.com/products/rolex-gmt-master-ref-1675","https://www.ssongwatches.com/products/tudor-home-plate-7031","https://www.ssongwatches.com/products/copy-of-girard-perregaux-triple-calendar","https://www.ssongwatches.com/products/jaeger-lecoultre-polaris-e-859","https://www.ssongwatches.com/products/rolex-sea-dweller-great-white-1665","https://www.ssongwatches.com/products/lemania-tg-195","https://www.ssongwatches.com/products/zenith-el-primero-a-3817-chronograph","https://www.ssongwatches.com/products/rolex-explorer-ii-1655-straight-hand","https://www.ssongwatches.com/products/omega-speedmaster-ed-white-105-003","https://www.ssongwatches.com/products/heuer-carrera-dato-45-ref-3147n-1","https://www.ssongwatches.com/products/omega-speedmaster-2998-6","https://www.ssongwatches.com/products/breguet-type-20","https://www.ssongwatches.com/products/breitling-co-pilot-7650","https://www.ssongwatches.com/products/lemania-dive-supervisor-vintage-watch","https://www.ssongwatches.com/products/certina-ds-diver-first-execution-5601-013","https://www.ssongwatches.com/products/omega-suveran-2400-4-grey","https://www.ssongwatches.com/products/heuer-404-chronograph-pre-carrera","https://www.ssongwatches.com/products/zenith-el-primero-g-381","https://www.ssongwatches.com/products/zenith-cairelli-a-m-i-italian-air-force","https://www.ssongwatches.com/products/wittnauer-242t-1","https://www.ssongwatches.com/products/universal-geneve-compax-22705-1","https://www.ssongwatches.com/products/smiths-w10-military-1","https://www.ssongwatches.com/products/breitling-top-time-ref-810-aopa","https://www.ssongwatches.com/products/omega-seamaster-300-165-24","https://www.ssongwatches.com/products/heuer-carrera-3647t","https://www.ssongwatches.com/products/heuer-carrera-2447n-gubelin-silver-script","https://www.ssongwatches.com/products/movado-triple-date-lnos","https://www.ssongwatches.com/products/hamilton-reverse-panda-chronograph","https://www.ssongwatches.com/products/wakmann-triple-calendar-chronograph-37mm","https://www.ssongwatches.com/products/longines-dirty-dozen-w-w-w-4","https://www.ssongwatches.com/products/croton-chronomaster-aviator-sea-diver-1","https://www.ssongwatches.com/products/iwc-porsche-design-compass-3510","https://www.ssongwatches.com/products/doxa-sub-300t-sharkhunter-aqua-lung","https://www.ssongwatches.com/products/heuer-carrera-dato-45-ref-3147n-2","https://www.ssongwatches.com/products/rolex-day-date-1803-white-gold-1","https://www.ssongwatches.com/products/tudor-big-crown-submariner-ref-7924","https://www.ssongwatches.com/products/rolex-explorer-ii-1655-unpolished","https://www.ssongwatches.com/products/rolex-double-red-sea-dweller-mk-iv-provenance","https://www.ssongwatches.com/products/rolex-gmt-master-ref-16750","https://www.ssongwatches.com/products/universal-geneve-polerouter-20357-2","https://www.ssongwatches.com/products/omega-seamaster-chronograph-145-005-68","https://www.ssongwatches.com/products/omega-ranchero-2990-1","https://www.ssongwatches.com/products/rolex-oyster-perpetual-1005","https://www.ssongwatches.com/products/omega-seamaster-300-166-024","https://www.ssongwatches.com/products/zodiac-reverse-panda-chronograph","https://www.ssongwatches.com/products/heuer-carrera-belgian-air-forceref-7753","https://www.ssongwatches.com/products/wittnauer-stepped-case-24-hr-dial","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-5","https://www.ssongwatches.com/products/clebar-reverse-panda-chronograph-poor-mans-heuer","https://www.ssongwatches.com/products/audemars-piguet-royal-oak-calendar-moon-25594","https://www.ssongwatches.com/products/zodiac-panda-chronograph-valjoux-72","https://www.ssongwatches.com/products/cartier-santos-dumont-1575","https://www.ssongwatches.com/products/breitling-top-time-ref-813","https://www.ssongwatches.com/products/heuer-carrera-2447nst","https://www.ssongwatches.com/products/iwc-porsche-design-compass-3511","https://www.ssongwatches.com/products/lemania-tg-195-swedish-military-3","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-6","https://www.ssongwatches.com/products/heuer-ref-345-gilt-gloss","https://www.ssongwatches.com/products/heuer-orvis-solunagraph","https://www.ssongwatches.com/products/yema-yachtingraf","https://www.ssongwatches.com/products/hamilton-panda-chronograph-lnos","https://www.ssongwatches.com/products/hamilton-chronomatic-cal-11-lnos-full-set","https://www.ssongwatches.com/products/hamilton-reverse-panda-chronograph-lnos","https://www.ssongwatches.com/products/rolex-submariner-5513-maxi-mk-v","https://www.ssongwatches.com/products/grand-seiko-4520-8010","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-3","https://www.ssongwatches.com/products/universal-geneve-polerouter-sub-green","https://www.ssongwatches.com/products/girard-perregaux-deep-diver","https://www.ssongwatches.com/products/eterna-baby-chrono-valjoux-69","https://www.ssongwatches.com/products/tollet-landeron-39-chronograph","https://www.ssongwatches.com/products/wittnauer-242t","https://www.ssongwatches.com/products/hamilton-6b-raf-3","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-3","https://www.ssongwatches.com/products/universal-geneve-oversized-dress-watch","https://www.ssongwatches.com/products/zodiac-heuer-12-dato-2547s","https://www.ssongwatches.com/products/grana-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/jardur-bezelmeter-1","https://www.ssongwatches.com/products/lip-breitling-765","https://www.ssongwatches.com/products/universal-geneve-uni-compax","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-2","https://www.ssongwatches.com/products/rolex-explorer-ii-1655-full-set","https://www.ssongwatches.com/products/eterna-kontiki-first-execution","https://www.ssongwatches.com/products/rolex-explorer-ii-1655","https://www.ssongwatches.com/products/technos-skydiver","https://www.ssongwatches.com/products/lanco-barracuda-diver","https://www.ssongwatches.com/products/tissot-mediostat","https://www.ssongwatches.com/products/hamilton-6b-raf-1","https://www.ssongwatches.com/products/lecoultre-valjoux-72","https://www.ssongwatches.com/products/universal-geneve-uni-compax-lnos","https://www.ssongwatches.com/products/movado-m95-sub-sea-3","https://www.ssongwatches.com/products/iwc-mk-11-raf","https://www.ssongwatches.com/products/mido-multi-centerchrono-1","https://www.ssongwatches.com/products/heuer-autavia-2446c","https://www.ssongwatches.com/products/omega-320-chronograph-101-009","https://www.ssongwatches.com/products/heuer-carrera-dato-45-ref-3147n","https://www.ssongwatches.com/products/zenith-a277-diver","https://www.ssongwatches.com/products/jaeger-lecoultre-mk-11","https://www.ssongwatches.com/products/iwc-tropical-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/vixa-flyback-type-20","https://www.ssongwatches.com/products/iwc-mk-11-raf-radium-dial","https://www.ssongwatches.com/products/movado-m95-sub-sea","https://www.ssongwatches.com/products/lemania-series-2-royal-navy-monopusher-chronograph","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-1","https://www.ssongwatches.com/products/zenith-a-271","https://www.ssongwatches.com/products/jaeger-4atm-e-13001","https://www.ssongwatches.com/products/breitling-premier-ref-734","https://www.ssongwatches.com/products/longines-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/copy-of-zenith-el-primero-g-381","https://www.ssongwatches.com/products/benrus-type-ii-class-a-1","https://www.ssongwatches.com/products/benrus-type-i-class-a","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-4","https://www.ssongwatches.com/products/breitling-navitimer-806-box-10-full-set","https://www.ssongwatches.com/products/iwc-hermet-oversized","https://www.ssongwatches.com/products/hamilton-fab-four-6bb-chronograph","https://www.ssongwatches.com/products/breitling-long-playing-815","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf","https://www.ssongwatches.com/products/copy-of-cyma-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/omega-seamaster-chronograph-145-005-67","https://www.ssongwatches.com/products/rolex-day-date-18038","https://www.ssongwatches.com/products/omega-constellation-pie-pan-168-005","https://www.ssongwatches.com/products/iwc-dirty-dozen-w-w-w-1","https://www.ssongwatches.com/products/zenith-el-primero-a-384","https://www.ssongwatches.com/products/zenith-el-primero-a-385","https://www.ssongwatches.com/products/aristo-gallet-multichron-regulator","https://www.ssongwatches.com/products/movado-m95-sub-sea-full-set","https://www.ssongwatches.com/products/omega-jumbo-2580-2505-tropical-salmon","https://www.ssongwatches.com/products/jaeger-valjoux-72-chronograph","https://www.ssongwatches.com/products/breitling-top-time-ref-812","https://www.ssongwatches.com/products/lecoultre-valjoux-72-e-335","https://www.ssongwatches.com/products/copy-of-hamilton-6b-raf","https://www.ssongwatches.com/products/gallet-multichron-30-m","https://www.ssongwatches.com/products/accurist-schockmaster","https://www.ssongwatches.com/products/lemania-royal-air-force-series-4","https://www.ssongwatches.com/products/wakmann-triple-calendar-chronograph-1","https://www.ssongwatches.com/products/girard-perregaux-aero-compax","https://www.ssongwatches.com/products/heuer-autavia-2446c-gmt","https://www.ssongwatches.com/products/hamilton-6b-raf-2","https://www.ssongwatches.com/products/rolex-explorer-ref-1016","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-tropical","https://www.ssongwatches.com/products/zodiac-heuer-carrera-12-dato-2547sn","https://www.ssongwatches.com/products/zodiac-panda-chronograph","https://www.ssongwatches.com/products/longines-dirty-dozen-w-w-w-3","https://www.ssongwatches.com/products/lecoultre-shark-e-2643","https://www.ssongwatches.com/products/heuer-carrera-3647s","https://www.ssongwatches.com/products/trematic-bidynator-triple-calendar-moonphase","https://www.ssongwatches.com/products/record-w-w-w-nato-dial-1","https://www.ssongwatches.com/products/lemania-tg-195-swedish-military-2","https://www.ssongwatches.com/products/rolex-day-date-1803-matte-black","https://www.ssongwatches.com/products/zenith-excelsior-park-143-yugoslavian-air-force","https://www.ssongwatches.com/products/omega-seamaster-300-165-014","https://www.ssongwatches.com/products/universal-geneve-polerouter-20217-4","https://www.ssongwatches.com/products/heuer-bundeswehr-sternzeit-reguliert","https://www.ssongwatches.com/products/girard-perregaux-triple-calendar","https://www.ssongwatches.com/products/rolex-datejust-1603-red-flake","https://www.ssongwatches.com/products/breitling-top-time-long-playing-815","https://www.ssongwatches.com/products/omega-w-w-w-dirty-dozen","https://www.ssongwatches.com/products/vixa-flyback-type-21","https://www.ssongwatches.com/products/smiths-w10-military","https://www.ssongwatches.com/products/ulysse-nardin-dress-watch","https://www.ssongwatches.com/products/lemania-royal-navy-monopusher-chronograph","https://www.ssongwatches.com/products/movado-hs-360-sub-sea-el-primero","https://www.ssongwatches.com/products/lemania-royal-navy-series-2-monopusher","https://www.ssongwatches.com/products/copy-of-omega-fat-arrow-53-raf","https://www.ssongwatches.com/products/lemania-royal-navy-monopusher-chronograph-1","https://www.ssongwatches.com/products/rolex-gmt-master-ref-16750-matte-dial","https://www.ssongwatches.com/products/zenith-a-277-diver","https://www.ssongwatches.com/products/avia-incabloc-chronograph","https://www.ssongwatches.com/products/zenith-a-279","https://www.ssongwatches.com/products/longines-sei-tacche","https://www.ssongwatches.com/products/breitling-top-time-ref-810-chronograph","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-1","https://www.ssongwatches.com/products/iwc-cal-89-dress-watch","https://www.ssongwatches.com/products/eterna-valjoux-22-chronograph","https://www.ssongwatches.com/products/clebar-supercompressor","https://www.ssongwatches.com/products/wakmann-albino-triple-calendar-chronograph","https://www.ssongwatches.com/products/moeris-blancpain-bathyscaphe","https://www.ssongwatches.com/products/tudor-oyster-prince-black-waffle-ref-7909","https://www.ssongwatches.com/products/bulova-supercompressor","https://www.ssongwatches.com/products/favre-leuba-deep-blue","https://www.ssongwatches.com/products/hamilton-h-67-raf-3289","https://www.ssongwatches.com/products/minerva-gilt-gloss-vintage-chronograph","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-1","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/movado-m95-sub-sea-1","https://www.ssongwatches.com/products/lemania-royal-air-force-monopusher-series-3","https://www.ssongwatches.com/products/longines-dirty-dozen-w-w-w-1","https://www.ssongwatches.com/products/wittnauer-7004a","https://www.ssongwatches.com/products/bulova-oversized-supercompressor","https://www.ssongwatches.com/products/technos-skydiver-1","https://www.ssongwatches.com/products/benrus-type-ii-class-a","https://www.ssongwatches.com/products/universal-geneve-polerouter-second-gen","https://www.ssongwatches.com/products/movado-m95-sub-sea-2","https://www.ssongwatches.com/products/seiko-monopusher-chronograph","https://www.ssongwatches.com/products/grana-dirty-dozen-w-w-w-1","https://www.ssongwatches.com/products/lemania-tg-195-swedish-military","https://www.ssongwatches.com/products/breitling-surfboard-datora-ref-2031","https://www.ssongwatches.com/products/doxa-triple-calendar-chronograph","https://www.ssongwatches.com/products/moeris-blancpain-bathyscaphe-1","https://www.ssongwatches.com/products/wyler-incaflex","https://www.ssongwatches.com/products/hamilton-h-67-raf","https://www.ssongwatches.com/products/breitling-chronomatic-ref-2110","https://www.ssongwatches.com/products/jardur-bezelmeter","https://www.ssongwatches.com/products/yema-rallye","https://www.ssongwatches.com/products/hamilton-g-s-24-hour-dial","https://www.ssongwatches.com/products/omega-seamaster-300-165-024","https://www.ssongwatches.com/products/wittnauer-supercompressor-8007","https://www.ssongwatches.com/products/wakmann-triple-calendar-chronograph-39mm","https://www.ssongwatches.com/products/hamilton-g-s-abu-dhabi-defence-force","https://www.ssongwatches.com/products/wakmann-triple-calendar-chronograph","https://www.ssongwatches.com/products/hamilton-6b-raf","https://www.ssongwatches.com/products/omega-fat-arrow-53-raf-ck-2777-2","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-tropical-1","https://www.ssongwatches.com/products/breitling-chronomatic-ref-2110-panda","https://www.ssongwatches.com/products/wittnauer-7004a-1","https://www.ssongwatches.com/products/eterna-dirty-dozen-w-w-w","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-tropical-2","https://www.ssongwatches.com/products/meylan-decimal-chronograph-cal-321","https://www.ssongwatches.com/products/rolex-day-date-1803-white-gold","https://www.ssongwatches.com/products/mido-multi-centerchrono-2","https://www.ssongwatches.com/products/heuer-ref-346-salmon","https://www.ssongwatches.com/products/breitling-top-time-ref-811","https://www.ssongwatches.com/products/gallet-multichron-yachting","https://www.ssongwatches.com/products/heuer-camaro-7220n-chocolate","https://www.ssongwatches.com/products/breitling-top-time-ref-810","https://www.ssongwatches.com/products/lemania-tg-195-swedish-military-1","https://www.ssongwatches.com/products/longines-dirty-dozen-w-w-w-2","https://www.ssongwatches.com/products/cyma-dirty-dozen-w-w-w-tropical-3","https://www.ssongwatches.com/products/benrus-sky-chief","https://www.ssongwatches.com/products/record-w-w-w-nato-dial","https://www.ssongwatches.com/products/croton-chronomaster-aviator-sea-diver","https://www.ssongwatches.com/products/breitling-premier-ref-789","https://www.ssongwatches.com/products/heuer-autavia-11063v","https://www.ssongwatches.com/products/universal-geneve-tri-compax-linen-dial","https://www.ssongwatches.com/products/omega-speedmaster-145-022-69","https://www.ssongwatches.com/products/lemania-15tl","https://www.ssongwatches.com/products/breitling-premier-ref-788","https://www.ssongwatches.com/products/gigandet-wakmann-big-boy","https://www.ssongwatches.com/products/tenexact-panda-chronograph","https://www.ssongwatches.com/products/jardur-water-resistant-chronograph"]

    def parse(self, response):
        for quote in response.css("div.product-content-each"):
            yield {
                'year': quote.css("div.product-year::text").extract_first(),
                'name': quote.css("h1.product-product-header::text").extract_first(),
                'price': quote.css("#product-price::text").extract_first(),
                'description': quote.css("div.product-description > div.rte > p.p1 > span.s1::text").extract(),
                'condition': quote.css("div.product-cr > div.rte > p::text").extract(),
                'images': quote.css("div.image-gallery-each > img::attr(src)").extract(),
                'url':response.url
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))