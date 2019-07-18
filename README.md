# SG Bill Collector

All Bills introduced in the Singapore Parliament are on its <a href='https://www.parliament.gov.sg/parliamentary-business/bills-introduced?keyword=&title=&year=&page=1&pageSize=40'>website</a>. If you are ever so inclined to collect them all, it's your lucky day!

## Output

- Bill number
- Bill name
- Bill URL
- Date introduced
- Date of second reading
- Date passed

## Where's my data?
Data can be saved to a ```csv``` file with the follow command in terminal:

```scrapy crawl bills -o items.csv -t csv```

## Requirements
- Python
- Scrapy
- Unusual interest in Singapore legislation or politics

## Things to note

Actually, just one (so far). The ```bills_spider``` is coded to scrape 13 webpages of Bills, which is the total number of pages as of July 2019. The code needs to be tweaked when the number of pages grow in the future and the tweak needed is indicated by comments within the code.
