from PIL import Image
from math import*
#Les images sont codées depuis le coin en haut a gauche

#image=input("Drapeau a afficher (lettres minuscules)")

resx=300
resy=200

def DrawImage(xsize,ysize):#work
    img=Image.new('RGB',(xsize,ysize),"white")
    return img

def AddBox(img,xanchor,yanchor,width,height,color):#work
    for x in range(xanchor,xanchor+width):
        for y in range(yanchor,yanchor+height):
            img.putpixel((x,y),color)

def AddBoxRasLeBol (img,xanchor,yanchor,width,height,color):#wait...it works, ertgbeyguyrgr,FUUUUCK YEAHHHH !!! C'est pas opti du tt mais on s'en fout ca marche
    sizex,sizey=img.size
    for x in range(xanchor,xanchor+width):
        for y in range(yanchor,yanchor+height):
            if x<sizex and y<sizey:
                img.putpixel((x,y),color)

def AddDiagBox(img,xanchor,yanchor,sizex,sizey,pensize,color):
    if xanchor>sizex or yanchor>sizey or xanchor+pensize>sizex or yanchor+pensize>sizey:
        AddBoxRasLeBol(img,xanchor,yanchor,pensize,pensize,color)
    else:
        AddBox(img,xanchor,yanchor,pensize,pensize,color)
        return img

def AddDiag(img,startHautouBas,sizex,sizey,pensize,color):
    onesegwidth=ceil(sizex/sizey)
    onesegheight=ceil(sizey/sizex)
    if startHautouBas=="h":
        y=0
        for x in range(0,sizex,onesegwidth):
            y=y+onesegheight
            AddDiagBox(img,x,y,sizex,sizey,pensize,color)
    if startHautouBas=="b":
        y=sizey
        for x in range(0,sizex,onesegwidth):
            y=y-onesegheight
            AddDiagBox(img,x,y-pensize,sizex,sizey,pensize,color)

def tricolore(VouH,sizex,sizey,r1,g1,b1,r2,g2,b2,r3,g3,b3):#with rectangle draw function handmade
    drapeau=DrawImage(sizex,sizey)
    if VouH=="h":
        AddBox(drapeau,0,0,sizex//3,sizey,(r1,g1,b1))
        AddBox(drapeau,sizex//3,0,sizex//3,sizey,(r2,g2,b2))
        AddBox(drapeau,sizex//3*2,0,sizex//3,sizey,(r3,g3,b3))
        if sizex%3!=0:#if some pixel column are empty
            AddBox(drapeau,sizex-sizex%3,0,sizex%3,sizey,(r3,g3,b3))
        return drapeau
    if VouH=="v":
        AddBox(drapeau,0,0,sizex,sizey//3,(r1,g1,b1))
        AddBox(drapeau,0,sizey//3,sizex,sizey//3,(r2,g2,b2))
        AddBox(drapeau,0,sizey//3*2,sizex,sizey//3,(r3,g3,b3))
        if sizey%3!=0:#if some pixel line are empty
            AddBox(drapeau,0,sizey-sizey%3,sizex,sizey%3,(r3,g3,b3))
        return drapeau

def croixpenché(AvecouSansintérieur,sizex,sizey,r1,g1,b1,r2,g2,b2,r3,g3,b3):#ligne non aligné si résolution trop étirée
    width=sizex//6
    height=sizey//4
    xpos=sizex//4
    ypos=sizey//2-height//2
    drapeau=DrawImage(sizex,sizey)
    AddBox(drapeau,0,0,sizex,sizey,(r1,g1,b1))
    AddBox(drapeau,xpos,0,width,sizey,(r2,g2,b2))
    AddBox(drapeau,0,ypos,sizex,height,(r2,g2,b2))
    if AvecouSansintérieur=="a":
        AddBox(drapeau,xpos+width//4,0,width//2,sizey,(r3,g3,b3))
        AddBox(drapeau,0,ypos+height//4,sizex,height//2,(r3,g3,b3))
        return drapeau
    else:
        return drapeau

def grèce (sizex,sizey):#Ces pixels qui dépassent je vais les tuer
    onelineheight=sizey//9
    drapeau=DrawImage(sizex,sizey)
    AddBox(drapeau,0,0,sizex,sizey,(0,127,255))
    for y in range(onelineheight,sizey-sizey%9,onelineheight*2):
        AddBox(drapeau,0,y,sizex,onelineheight,(255,255,255))
    AddBox(drapeau,0,0,sizex//3+onelineheight//2,sizey//2+onelineheight//2,(0,127,255))
    AddBox(drapeau,sizex//6-onelineheight//4,0,onelineheight,sizey//2+onelineheight//2,(255,255,255))
    AddBox(drapeau,0,sizey//4-onelineheight//4,sizex//3+onelineheight//2,onelineheight,(255,255,255))
    return drapeau

def unionjack (sizex,sizey):#dégueulasse avec !=ratio ,mais je l'ai fait,JE L'AI FAIT
    sizex=sizex+sizex//4
    drapeau=DrawImage(sizex,sizey)
    AddBox(drapeau,0,0,sizex,sizey,(0,0,139))
#cross diag
    AddDiag(drapeau,"h",sizex,sizey,sizex//8,(255,255,255))
    AddDiag(drapeau,"b",sizex,sizey,sizex//8,(255,255,255))
    AddDiag(drapeau,"h",sizex,sizey,sizex//16,(255,0,0))
    AddDiag(drapeau,"b",sizex,sizey,sizex//16,(255,0,0))
#cross straight
    AddBox(drapeau,sizex//2-sizex//10,0,sizex//5,sizey,(255,255,255))
    AddBox(drapeau,0,sizey//2-sizey//8,sizex,sizey//4,(255,255,255))
    AddBox(drapeau,sizex//2-sizex//20,0,sizex//10,sizey,(255,0,0))
    AddBox(drapeau,0,sizey//2-sizey//16,sizex,sizey//8,(255,0,0))
    return drapeau
              
#tricolor
france=tricolore("h",resx,resy,0,127,255,255,255,255,255,0,0)
belgique=tricolore("h",resx,resy,0,0,0,240,195,0,255,0,0)
italie=tricolore("h",resx,resy,9,106,9,255,255,255,255,0,0)
allemagne=tricolore("v",resx,resy,0,0,0,255,0,0,240,195,0)
autriche=tricolore("v",resx,resy,255,0,0,255,255,255,255,0,0)
hongrie=tricolore("v",resx,resy,255,0,0,255,255,255,9,106,9)
#cross
finlande=croixpenché("s",resx,resy,255,255,255,0,127,255,0,0,0)
suède=croixpenché("s",resx,resy,0,127,255,240,195,0,0,0,0)
norvège=croixpenché("a",resx,resy,255,0,0,255,255,255,0,0,139)
islande=croixpenché("a",resx,resy,0,0,139,255,255,255,255,0,0)
#NON MAIS OH Y'A DES LIMITES A LA MALTRAITANCE NON!!!
grèce=grèce(resx,resy)#putain de pixel qui dépasse de merde !!!
royaumeuni=unionjack(resx,resy)#J'te casse les bandes saloperie d'angleterre

#eval(image)
royaumeuni.show()