from bs4 import BeautifulSoup

htmldoc = """
<p>
    PASTE YOUR HTML CODE HERE!
</p>
"""

soup = BeautifulSoup(htmldoc, 'html.parser')

html_code = ""

imgs = soup.find_all('img')

for i in imgs:
    html_code += '<a href="' + i.get('src') + '"><img src="' + i.get('src') + '" width="500" />"</a>\n'

print(html_code)
