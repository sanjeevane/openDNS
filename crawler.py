import scrapy
import httplib2
import time
from scrapy.loader import ItemLoader
import sys


class domainCrawlSpider(scrapy.Spider):
    name = "domainCrawl"
    rotate_user_agent = True

    def start_requests(self):
	#Read the seed urls from the file
	with open('domainCrawler/spiders/seed','r') as fileName:
	  lines = fileName.readlines()
	
	#Crawl and scrap each web URL  	
	for line in lines:
	    h = httplib2.Http()
            url = 'http://www.' + line.strip()	
	    try:
	    	resp = h.request(url, 'HEAD')
	
		#If domain name is valid
		if int(resp[0]['status']) == 200:		    
		   self.log(url);
		   yield scrapy.Request(url=url, callback=self.parse_url)
	    except Exception:
		pass

	self.log('Saved file')
	
	    
    def parse_url(self, response):
	scrappedContent = 'content_%s' % str(time.time());
	with open(scrappedContent, 'wb') as ww:
		ww.write("%s \n" %response.url);
		if bool(response.xpath("//meta[@name='keywords']/@content").extract_first()) ==True:
			keywords = response.xpath("//meta[@name='keywords']/@content").extract_first()
			ww.write(keywords.encode('utf-8'));
			


		if bool(response.xpath("//meta[@name='description']/@content").extract_first()) ==True:
			keywords = response.xpath("//meta[@name='description']/@content").extract_first()
			ww.write(keywords.encode('utf-8'));
		   
	
		if bool(response.xpath('//title/text()').extract_first()) == True:
			titles= response.xpath('//title/text()').extract_first()
			for title in titles:
				if bool(title) == True:
					ww.write(title.encode('utf_8'));
					
		
	
		if bool(response.xpath('//body/text()').extract_first()) == True:
			body = response.xpath('//body/text()').extract_first()
			for b in body:
				if bool(b) == True:
					ww.write(b.encode('utf-8'));
					
	
	
		if bool(response.xpath('//div/text()').extract_first()) == True:
			divs = response.xpath('//div/text()').extract_first()
			for div in divs:		
				if bool(div) == True:
					ww.write(div.encode('utf-8'));
					
	
	
		if bool(response.xpath('//span/text()').extract_first()) == True:
			spans = response.xpath('//span/text()').extract_first()
			for s in spans:
				if bool(s) == True:
					ww.write(s.encode('utf-8'));
					
	
	
		if bool(response.xpath('//h1/text()').extract_first()) == True:
			headers = response.xpath('//h1/text()').extract_first()
			for header in headers:
				if bool(header) == True:
					ww.write(header.encode('utf-8'));
					
	
	
		if bool(response.xpath('//p/text()').extract_first()) == True:
			paragraphs = response.xpath('//p/text()').extract_first()
			for paragraph in paragraphs:
				if bool(paragraph) == True:
					ww.write(paragraph.encode('utf-8'));			
					
	page = response.url
        filename = 'crawled_%s' % str(time.time());
	with open(filename, 'wb') as f:
    		f.write("URL --> %s \n" %response.url);
    		f.write(response.body)
    		f.close();
	yield page
