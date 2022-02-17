import pandas as pd
from PIL import Image, ImageDraw

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=1900-01-01&minmagnitude=8'

myData = pd.read_csv(url,sep="|")

#myList = ["Amy","Keshav","Andy","Owen","Aries","Calista","Mr. Russ","Amanda"]

for item in myData.iterrows():
  print(item)

print(len(myData.index))

# opens the image to be drawn
myImage = Image.open("blankCanvas.png")
# "Get Context"
draw = ImageDraw.Draw(myImage)

draw.rectangle([0,0,100,100],fill="green",outline="red",width=4)
draw.ellipse([200,250,300,350], fill="yellow")
myImage.save("newImage.png")
'''
 draw.ellipse((25, 50, 175, 200), fill="red")
'''


