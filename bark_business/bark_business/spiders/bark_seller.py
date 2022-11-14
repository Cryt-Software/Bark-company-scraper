# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider


class BarkSellerSpider(SitemapSpider):
    name = 'bark_seller'
    allowed_domains = ['bark.com']
    sitemap_urls = ['https://www.bark.com/sitemaps/sitemap-seller-1-en-gb.xml','https://www.bark.com/sitemaps/sitemap-seller-2-en-gb.xml']  

    def parse(self, response):

        # item_prop_list = response.xpath('//*[@itemprop]/@itemprop')
        # item_prop_list = response.xpath('//*[@itemprop]')
        desc = response.xpath("//div[contains(@class,'section-about')]//p[@itemprop='description']/text()").get()

        name = response.xpath('//*[@itemprop="name"]/text()').get()
        services = response.xpath('//span[@itemprop="knowsAbout"]/text()').getall()
        address = response.xpath('//span[@itemprop="address"]/text()').get()
        address_two = response.xpath('//p[@class="seller-location"]/span[2]/span/text()').get()
        url = response.request.url
        links = response.xpath('//div[contains(@class,"section-external-links")]//a/@href').getall()
        facebook = response.xpath("//a[@data-thing = 'facebook']/@href").get()
        tel = response.xpath("//a[@data-thing = 'tel']/@href").get()
        website = response.xpath("//a[@data-thing = 'website']/@href").get()
        email = response.xpath("//a[@data-thing = 'email']/@href").get()
        
        return {
            'Name': name,
            'About': desc,
            'List_of_services': services,
            'Address': address,
            'Address_2': address_two,
            'Url': url,
            'Links': links,
            'Facebook': facebook,
            'Tel': tel,
            'Website': website,
            'Email': email,
            'Bark_url':response.url,
            'services 1': services[1] if 1 < len(services) else '',
            'services 2': services[2] if 2 < len(services) else '',
            'services 3': services[3] if 3 < len(services) else '',
            'links 1': links[1] if 1 < len(links) else '',
            'links 2': links[2] if 2 < len(links) else '',
            'links 3': links[3] if 3 < len(links) else '',
        }
