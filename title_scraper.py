#webpage Title Scraper
import requests
from bs4 import BeautifulSoup

print("🌐 Webpage Title Scraper")

url = input("Enter a website URL: ")

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string

    print("\n📝 Page Title Found:")
    print(title)

    with open("scraped_title.txt", "w") as file:
        file.write(f"URL: {url}\n")
        file.write(f"Title: {title}\n")

    print("\n📄 Title saved in scraped_title.txt")

except Exception as error:
    print("\n❌ Error occurred:")
    print(error)
