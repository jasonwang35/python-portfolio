import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers, timeout=15)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
titles = [a.get_text(strip=True) for a in soup.select("span.titleline a")]

df = pd.DataFrame({"Headline": titles})
df.to_excel("news_headlines_en.xlsx", index=False)
print(f"Saved {len(df)} headlines to news_headlines_en.xlsx")
