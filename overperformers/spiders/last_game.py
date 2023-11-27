import scrapy
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
# Format as 'yearmonthday'
formatted_yesterday = yesterday.strftime('%Y%m%d')


class LastGameSpider(scrapy.Spider):
    name = "last_game"
    allowed_domains = ["www.cbssports.com"]
    start_urls = ["https://www.cbssports.com/nba/stats/leaders/live/all-pos/"+formatted_yesterday+"/?sortcol=pts&sortdir=descending"]

    def parse(self, response):
        rows = response.xpath('//div[@id = "TableBase"]/div/div/table/tbody/tr')

        for row in rows: 
            name = row.xpath('./td/span[@class="CellPlayerName--long"]/span/a/text()').get().strip()
            pts = row.xpath('./td[5]/text()').get().strip()
            ast = row.xpath('./td[7]/text()').get().strip()
            reb = row.xpath('./td[6]/text()').get().strip()
            fg3 = row.xpath('./td[8]/text()').get().strip()

            # cleaning data
            name = ' '.join(name.split())
            pts = pts.replace(" ", "").replace("\n", "").replace(",", "")
            ast = ast.replace(" ", "").replace("\n", "").replace(",", "")
            reb = reb.replace(" ", "").replace("\n", "").replace(",", "")
            fg3 = fg3.replace(" ", "").replace("\n", "").replace(",", "")

            yield {
                "Name": name,
                "PTS": pts,
                "AST": ast,
                "REB": reb,
                "3PM": fg3,
            }


                
