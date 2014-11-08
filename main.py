__author__ = 'JPaehr'
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from PIL import Image
import os
print("Name des Ausgabedatei eingeben: ")
outputname = input()

imagelist = list()

for i in os.listdir():
    if i[-3:] == 'jpg' or i[-3:] == 'gif':
        imagelist.append(i)

os.mkdir("compressed")
c = canvas.Canvas(str(outputname)+'.pdf')
for i in imagelist:
    im = Image.open(i)
    # print(im.size)
    im.thumbnail((1200, 1200))
    im.save("compressed/"+str(i), "JPEG")
    im.close()

    imNew = Image.open("compressed/"+str(i))
    # print(imNew.size)
    xlimit = 21
    ylimit = 29.7

    ratio_paper = xlimit / ylimit
    ratio_im = imNew.size[0] / imNew.size[1]

    if ratio_paper > ratio_im:
        # height relevant
        xlimit = ylimit*imNew.size[0] / imNew.size[1]
        # print("xlimit: "+str(xlimit))

    else:
        # with relevant
        ylimit = xlimit*imNew.size[1]/imNew.size[0]
        # print("ylim:" + str(ylimit))
    c.drawImage("compressed/"+str(i), 0, (29.7-ylimit)*cm, xlimit*cm, ylimit*cm)
    c.showPage()
    imNew.close()

c.save()
for i in imagelist:
    os.remove("compressed/"+str(i))
os.rmdir("compressed")