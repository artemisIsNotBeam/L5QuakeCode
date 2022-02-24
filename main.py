import pandas as pd
from PIL import Image, ImageDraw

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=1900-01-01&minmagnitude=8'

myData = pd.read_csv(url,sep="|")
theMap = Image.open("world-map.png")
drawCtx = ImageDraw.Draw(theMap)
width,height=theMap.size

mid_width = width //2 + 1
mid_height = height //2 - 1

print(width)
print(height)
#myList = ["Amy","Keshav","Andy","Owen","Aries","Calista","Mr. Russ","Amanda"]

for idx,item in myData.iterrows():
    x = mid_width + item["Longitude"] / 10 * 32.25
    y = mid_height - item["Latitude"] / 10 * 32.25
    drawCtx.pieslice([x - 16, y - 16, x + 16, y + 16], 240, 300, fill="blue")

theMap.save("quakeImage.png")
  


'''
print(len(myData.index))

# opens the image to be drawn
myImage = Image.open("blankCanvas.png")
# "Get Context"
draw = ImageDraw.Draw(myImage)

draw.rectangle([0,0,100,100],fill="green",outline="red",width=4)
draw.ellipse([200,250,300,350], fill="yellow")
myImage.save("newImage.png")
'''
 #draw.ellipse((25, 50, 175, 200), fill="red")



