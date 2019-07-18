from bills.items import BillsItem
import scrapy
from scrapy.selector import Selector

class BillsSpider(scrapy.Spider):
    name = "bills"
    allowed_domains = ["parliament.gov.sg"]
    start_urls = [
        "https://www.parliament.gov.sg/parliamentary-business/bills-introduced?keyword=&title=&year=&page={}&pageSize=40".format(i) for i in range(1,14)
    ]#13 pages in total to be scapped so far in July 2019. When number of pages grow, tweak range(1, new-number-of-pages + 1). +1 is needed as range is until but not including second number.

    def parse(self, response): # Define parse() function.
        items = [] # Element for storing scraped information.
        hxs = Selector(response) # Selector allows us to grab HTML from the response (target website).
        for sel in hxs.xpath("//div[@class='indv-bill']"): # Because we're using XPath language, we need to specify that the paragraphs we're trying to isolate are expressed via XPath.
            item = BillsItem()
            item['name'] =  sel.xpath("div[@class='row bill-title']/div[@class='col-md-8 col-xs-12']/a/@title").extract() # name of bill from the 'a' element.
            item['link']  =  sel.xpath("div[@class='row bill-title']/div[@class='col-md-8 col-xs-12']/a/@href").extract() # Href/URL from the 'a' element.
            item['bill_no'] =  ''.join(sel.xpath("div[@class='row bill-title']/div[@class='col-md-4 col-xs-12']/text()").extract())# bill number. ''.join needed as output is a list with desired result together with empty entries - e.g [ , , 7/2018]. ''.join gets rid of unnecessary commas.
            item['intro'] =  ''.join(sel.xpath("div[@class='row']/div[@class='col-md-4 col-xs-12 xs-boxgap'][1]/text()").extract()) # Date bill introduced.
            item['second']  =  ''.join(sel.xpath("div[@class='row']/div[@class='col-md-4 col-xs-12 xs-boxgap'][2]/text()").extract()) # Date second reading.
            item['passed'] =  ''.join(sel.xpath("div[@class='row']/div[@class='col-md-4 col-xs-12 xs-boxgap'][3]/text()").extract()) # Date third reading.

            items.append(item)
        return items # Shows scraped information as terminal output.
