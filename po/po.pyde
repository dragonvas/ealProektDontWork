m=930
q=900
z=100
p=100
def setup():
    rectMode(CENTER)
    size (1000 ,1000)
    frameRate(3)
def draw():
    loop()
    global m,z,q,p
    background(255,255,255)
    fill (0,0,0)
    line (100,1000,100,100)
    line (200,900,200,0)
    line (300,1000,300,100)
    line (400,900,400,0)
    line (500,1000,500,500)
    line (600,900,600,0)
    line (700,1000,700,100)
    line (800,900,800,0)
    line (900,1000,900,100)
    line (400,400,600,400)
    rect (50,m,30,60)
    rect (950,m,30,60)
    rect (500,200,50,50)
    fill (255,255,255)
    text (u'Играть!',480,207)
    m=m-80
    if m < 100:
        background(255,255,255)
        fill(0,0,0)
        line (100,1000,100,100)
        line (200,900,200,0)
        line (300,1000,300,100)
        line (400,900,400,0)
        line (500,1000,500,500)
        line (600,900,600,0)
        line (700,1000,700,100)
        line (800,900,800,0)
        line (900,1000,900,100)
        line (400,400,600,400)
        rect (100,50,60,30)
        rect (900,50,60,30)
        rect (500,200,50,50)
        fill (255,255,255)
        text (u'Играть!',480,207)

        background(255,255,255)
        fill (0,0,0)
        line (100,1000,100,100)
        line (200,900,200,0)
        line (300,1000,300,100)
        line (400,900,400,0)
        line (500,1000,500,500)
        line (600,900,600,0)
        line (700,1000,700,100)
        line (800,900,800,0)
        line (900,1000,900,100)
        line (400,400,600,400)
        rect (150,z,30,60)
        rect (850,z,30,60)
        rect (500,200,50,50)
        fill (255,255,255)
        text (u'Играть!',480,207)
        z=z+80
        if z > 920:
            background(255,255,255)
            fill(0,0,0)
            line (100,1000,100,100)
            line (200,900,200,0)
            line (300,1000,300,100)
            line (400,900,400,0)
            line (500,1000,500,500)
            line (600,900,600,0)
            line (700,1000,700,100)
            line (800,900,800,0)
            line (900,1000,900,100)
            line (400,400,600,400)
            rect (200,950,60,30)
            rect (800,950,60,30)
            rect (500,200,50,50)
            fill (255,255,255)
            text (u'Играть!',480,207)
            
            
            background(255,255,255)
            fill (0,0,0)
            line (100,1000,100,100)
            line (200,900,200,0)
            line (300,1000,300,100)
            line (400,900,400,0)
            line (500,1000,500,500)
            line (600,900,600,0)
            line (700,1000,700,100)
            line (800,900,800,0)
            line (900,1000,900,100)
            line (400,400,600,400)
            rect (250,q,30,60)
            rect (750,q,30,60)
            rect (500,200,50,50)
            fill (255,255,255)
            text (u'Играть!',480,207)
            q=q-80
            if q < 80:
                background(255,255,255)
                fill(0,0,0)
                line (100,1000,100,100)
                line (200,900,200,0)
                line (300,1000,300,100)
                line (400,900,400,0)
                line (500,1000,500,500)
                line (600,900,600,0)
                line (700,1000,700,100)
                line (800,900,800,0)
                line (900,1000,900,100)
                line (400,400,600,400)
                rect (300,50,60,30)
                rect (700,50,60,30)
                rect (500,200,50,50)
                fill (255,255,255)
                text (u'Играть!',480,207)
                
                background(255,255,255)
                fill (0,0,0)
                line (100,1000,100,100)
                line (200,900,200,0)
                line (300,1000,300,100)
                line (400,900,400,0)
                line (500,1000,500,500)
                line (600,900,600,0)
                line (700,1000,700,100)
                line (800,900,800,0)
                line (900,1000,900,100)
                line (400,400,600,400)
                rect (350,p,30,60)
                rect (650,p,30,60)
                rect (500,200,50,50)
                fill (255,255,255)
                text (u'Играть!',480,207)
                p=p+80
                        
                        
