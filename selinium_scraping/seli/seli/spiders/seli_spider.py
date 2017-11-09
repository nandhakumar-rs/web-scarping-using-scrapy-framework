# -*- coding: utf-8 -*-
import scrapy,time
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions  import NoSuchElementException

class SeliSpiderSpider(scrapy.Spider):
	name = 'seli_spider'
	allowed_domains = ['books.toscrape.com']
	

	def start_requests(self):
		self.driver = webdriver.Chrome('F:\driver\driv')
		self.driver.get('http://books.toscrape.com')
		select = Selector(text = self.driver.page_source)
		books = select.xpath('//h3/a/@href').extract()
		for book in books:
			new_url = 'http://books.toscrape.com/'+ book
			yield Request(new_url, callback = self.parse_book)
		while True:
			try:
				driver_obj =self.driver.find_element_by_xpath('//a[text() = "next"]')
				time.sleep(3)
				driver_obj.click()
				select = Selector(text = self.driver.page_source)
				books = sel.xpath('//h3/a/@href').extract()
				for book in books:
					new_url = 'http://books.toscrape.com/catalogue/'+ book
					yield Request(new_url, callback = self.parse_book)
			except NoSuchElementException:
					self.driver.exit()
					break

	def parse_book(self,response):
		pass
