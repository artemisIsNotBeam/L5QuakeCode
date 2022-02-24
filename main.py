import pandas as pd
from PIL import Image, ImageDraw


url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=1900-01-01&minmagnitude=8"
myData = pd.read_csv(url,sep ="|")
map = Image.open("world-map.png")
mapctx = ImageDraw.Draw(map)
width,height = map.size

mid_width = width//2
mid_height = height//2
for idx,item in myData.iterrows():
	x = mid_width + item["Longitude"] / 10 * 32.25
	y = mid_height - item["Latitude"] / 10 * 32.25
	mapctx.pieslice([x - 16, y - 16, x + 16, y + 16], 240, 300, fill="blue")
	
'''
myImage = Image.open("blankCanvas.png")
draw = ImageDraw.Draw(myImage)

draw.rectangle([0,0,100,100], fill="red")
draw.line([5,10,80,100], width = 10, fill="green")
'''

map.save("quakeImage.png")
