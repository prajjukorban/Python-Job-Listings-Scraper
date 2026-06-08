from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cards = soup.find_all("div",class_="card-content")

data= {"Title": [], "Company": [], "Location": [], "Apply Link": []}

for card in cards:
    title = card.find("h2", class_="title").text
    compamy = card.find("h3",class_="company").text
    location = card.find("p", class_="location").text
    apply_link = card.find("a", class_="card-footer-item")["href"]
    data["Title"].append(title)
    data["Company"].append(compamy)
    data["Location"].append(location)
    data["Apply Link"].append(apply_link)

def preprocess(x):
    x = x.str.replace(r"\s+", " ", regex=True)
    return x

df = pd.DataFrame(data)
print(df.apply(preprocess))

print(df.isnull().sum())

df.to_csv("fake_jobs.csv", index=False)


