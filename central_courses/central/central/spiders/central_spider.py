# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request 

class CentralSpiderSpider(scrapy.Spider):
    name = 'central_spider'
    allowed_domains = ['www.class-central.com']
    start_urls = ['https://www.class-central.com/search?q=']
    def __init__(self,search_query = None):
    	self.search_query = search_query
    def parse(self,response):
    	search_url = "https://www.class-central.com/search?q=" + self.search_query
    	yield Request(search_url,callback = self.parse_course)

    def parse_course(self, response):
         course_titles = response.xpath('//tbody/tr/td[contains(@class,course-name-column)]/a/span/text()').extract()
         for course_title in course_titles:
         	yield {
         	'course_title' : course_title
         	}
         next_url = response.xpath('//*[@rel = "next"]/@href').extract_first()
         next_page_url = response.urljoin(next_url)
         yield Request(next_page_url,callback = self.parse_course)