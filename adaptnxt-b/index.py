# // var data = [
# //     ["Alpha", "Beta"],
# //     ["Charlie", "Delta"],
# //     ["Echo", "Foxtrot",""]
# //   ];
# //   // (B) WRITE TO FILE
# //   const fs = require("fs");
# //   const stream = fs.createWriteStream("demoC.csv");
# //   for (let i of data) { stream.write(i.join(",") + "\r\n"); }
# //   stream.end();
# //   console.log("Done!");

# const request = require("request-promise");
# const cheerio = require("cheerio");
# const fs = require("fs");
# const json2csv = require("json2csv").parse;

# const productsUrl =
#   "https://www.staples.com/Computer-office-desks/cat_CL210795/663ea?icid=BTS:2020:STUDYSPACE:DESKS"(
#     async () => {
#       let productsdata = [];
#       const response = await request({
#         url: productsUrl,
#         headers: {
#           path: "/rest/v1/delivery?client=staples&sessionId=62f801fca1e34fe8b4aaf7b00a8e91f1&version=2.4.0",
#           "accept-encoding": "gzip, deflate, br",
#           "accept-language": "en-US,en;q=0.9",
#         },
#         gzip: true,
#       });


#       let $ =  cheerio.load(response)
#     }
#   )();
from bs4 import BeautifulSoup
import requests
url = "https://www.walmart.com/browse/electronics/dell-gaming-laptops/3944_3951_7052607_1849032_4519159"
# r = requests.get(url)		# r variable has all the HTML code
# htmlContent = r.content	# r returns response so if we want the code we write r.content
# print(htmlContent)		# printing the code

# htmlTexr = r.text
# print(htmlTexr)

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all("code"):
    print(i.text)
    title = soup.title
print(title)
print(soup.find('h1')) 
paras = soup.find_all('h1')
print(paras)
for i in paras:
    print(i)


anchors = soup.find_all('a')
for i in paras:
    print(i['href'])

for i in paras:
    print(i.get('href'))

ul = soup.find("ul")
print(ul.contents)


ul = soup.find("ul")
for i in ul.children:
	print(i)



ul = soup.find("ul")
print(ul.parent)


print(ul.parent.parent)


ul = soup.find(id="li")
print(ul.next_sibling.next_sibling)



ul = soup.find(id="li")

for j in ul.next_siblings:
    print(j)



f = open("file.csv", "w")
f.write("Every,word,will,go,in,separate,column\n")
f.write("This,will,go,in,next,row")
f.close()



with open("file.csv", "w") as f:
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")