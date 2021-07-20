from bs4 import BeautifulSoup

from urllib.request import urlopen as uReq
import re


with open("quotes.csv", "w",encoding='utf8') as my_file:
    my_file.write("Quote#Author#Category#Wordcount\n")
    for i in range(0,318):
        url = "https://www.goodreads.com/quotes/tag/knowledge?page={}".format(i)

        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        soup = BeautifulSoup(page_html, "html.parser")
        print(f"-------------------------\n")
        print(f"Page Number: {i}\n")
        print(f"-------------------------\n")

        for product_div in soup.find_all('div', {'class':'quote mediumText'}):
                quote = product_div.find("div",class_="quoteDetails").find("div",class_="quoteText")
                quote_string = quote.text.strip().replace('\n', '')
                author = quote.find("span", class_="authorOrTitle").text.strip().replace('\n','')

                tag = url.split('?')[0].split('/')[5].capitalize()
                author_name = author.replace('“', '"').replace('”', '"')
                quote_string = quote_string.split('    ―      ')[0]
                combined_string = str(quote_string + "#" + author_name + "#" + tag + "#" + str(len(quote_string)))
                my_file.write(combined_string)
                my_file.write("\n")

