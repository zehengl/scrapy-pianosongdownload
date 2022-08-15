import scrapy

from .level3_spider import Level3Spider


class IntermediateSpider(Level3Spider):
    name = "intermediate"

    def start_requests(self):
        urls = [
            "https://pianosongdownload.com/intermediate_advanced.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
