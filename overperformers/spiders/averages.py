import scrapy

class AveragesSpider(scrapy.Spider):
    name = "averages"

    def start_requests(self): 
        for i in range(1, 4):
            url = "https://basketball.realgm.com/nba/stats/2024/Averages/Qualified/points/All/desc/"+str(i)+"/Regular_Season"
            yield scrapy.Request(url=url)


    

    def parse(self, response):
        rows = response.xpath('//div[@class = "main-container"]/div/table/tbody/tr')

        for row in rows :
            name = row.xpath("./td[2]/a/text()").get()
            team = row.xpath("./td[3]/text()").get()
            pts = row.xpath("./td[6]/text()").get()
            fg3 = row.xpath("./td[10]/text()").get()
            ast = row.xpath("./td[19]/text()").get()
            reb = row.xpath("./td[18]/text()").get()
           
    

            yield {
                "Name" : name, 
                "Team" : team,  
                "PPG" : pts, 
                "3PM" : fg3, 
                "APG" : ast, 
                "RPG" : reb, 
                 
            }





        
