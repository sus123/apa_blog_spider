from scrapy import cmdline

cmdline.execute("scrapy runspider apablogspider.py -o apablog.csv".split())
