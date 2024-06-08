from bs4 import BeautifulSoup
import requests
import pandas as pd


product_name = []
prices = []
ratings = []
count_of_ratings = []
reviews = []

for i in range(1,7):
    URL = "https://www.amazon.in/s?k=smart+lock&crid=3F3ZD68Z29TU1&sprefix=smart+lo%2Caps%2C401&ref=nb_sb_ss_ts-doa-p_1_8"+str(i)

    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'Connection': 'keep-alive', 'Accept-Language': 'en-GB,en;q=0.6', 'Cookie': 'zero-chakra-ui-color-mode=light-zero; AMP_MKTG_8f1ede8e9c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; AMP_8f1ede8e9c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1MjgxOGYyNC05ZGQ3LTQ5OTAtYjcxMC01NTY0NzliMzAwZmYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA4MzgxNTQ4ODQzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwODM4MjE1NTQ2MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBNiU3RA==', 'Referer': 'https://books.toscrape.com/'})

    webpage = requests.get(URL, headers=HEADERS)

    print(webpage)

    soup = BeautifulSoup(webpage.text,'lxml')
    
    #print(soup)

    names = soup.find_all("span",class_="a-size-base-plus a-color-base a-text-normal")
    for i in names:
        name = i.text
        product_name.append(name)

    #print(len(product_name))

    price = soup.find_all("span",class_="a-price-whole")
    for i in price:
        name = i.astype(int)
        prices.append(name)
    #print(len(prices))

    rat = soup.find_all("span", class_="a-icon-alt")  

    for r in rat:
        rating = r.get_text()
        if rating:
            ratings.append(rating.strip())
        else:
            ratings.append('5 out of 5 ratings')
        
            
        

    #print(ratings)

    count_of_rating = soup.find_all("span",class_ = "a-size-base s-underline-text")

    for i in count_of_rating:
        name = i.text
        count_of_ratings.append(name)

   
    

    #print(len(count_of_ratings))
    min_length = min(len(product_name), len(prices), len(ratings), len(count_of_ratings))
    product_name = product_name[:min_length]
    prices = prices[:min_length]
    ratings = ratings[:min_length]
    count_of_ratings = count_of_ratings[:min_length]

    df = pd.DataFrame({
        "product_name": product_name,
        "prices": prices,
        "ratings": ratings,"count_of_ratings": count_of_ratings,
    })


    print(df)

    #df.to_csv("D:/smart_looccksasmart_lockss.csv")




















































    #while True:
    #names = soup.find("a",class_ = "_9QVEpD").get("href")
    #name = "https://www.flipkart.com"+names

    #print(name)
    #rl = name

        #URL = name
        #webpage = requests.get(URL, headers=HEADERS)

        #soup = BeautifulSoup(webpage.text,'lxml')

