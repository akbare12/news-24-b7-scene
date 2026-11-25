import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; BG=(250,246,236); INK=(22,22,24); RED=(178,34,34); NAVY=(24,48,88); GREY=(108,108,112); LINE=(198,190,176); PAPER=(255,253,247)
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def fs(s): return F(SERIF,s)
def fn(s): return F(SANS,s)
def fb(s): return F(SANSB,s)
def wrap(t,font,mw):
    lines=[]; cur=""
    for w in t.split():
        x=(cur+" "+w).strip()
        if font.getlength(x)<=mw: cur=x
        elif cur: lines.append(cur); cur=w
        else: cur=w
    if cur: lines.append(cur)
    return lines
def para(d,x,y,lines,font,fill=INK,lh=None):
    lh=lh or int(font.size*1.25)
    for ln in lines: d.text((x,y),ln,font=font,fill=fill); y+=lh
    return y
CHIP={"CONFIRMED":(0,122,62),"OFFICIAL":(18,84,180),"REPORTED":(96,110,138),"CLAIM":(205,110,0)}
def chip(d,x,y,label):
    c=CHIP.get(label,(96,110,138)); f=fb(8); w=f.getlength(label)+10
    d.rounded_rectangle([x,y,x+w,y+12],radius=3,fill=c); d.text((x+5,y+1.5),label,font=f,fill=(255,255,255)); return w
NA=[(-168,66),(-150,70),(-135,69),(-125,71),(-110,68),(-95,80),(-85,76),(-78,71),(-70,62),(-60,55),(-55,52),(-60,46),(-65,44),(-70,42),(-75,38),(-80,32),(-81,26),(-84,30),(-90,21),(-94,17),(-90,14),(-84,12),(-79,9),(-83,9),(-90,14),(-97,16),(-104,20),(-110,24),(-114,29),(-120,34),(-124,42),(-124,48),(-132,56),(-145,60),(-155,58),(-162,55),(-168,60),(-168,66)]
SA=[(-79,9),(-74,11),(-68,12),(-62,9),(-55,6),(-52,5),(-50,0),(-44,-3),(-38,-5),(-35,-8),(-38,-15),(-40,-21),(-46,-24),(-50,-29),(-54,-34),(-58,-38),(-63,-41),(-66,-47),(-69,-52),(-71,-54),(-73,-50),(-73,-44),(-73,-37),(-72,-30),(-71,-20),(-75,-15),(-79,-8),(-81,-4),(-80,1),(-79,9)]
AF=[(-17,15),(-16,20),(-13,27),(-10,31),(-6,35),(-1,35),(3,37),(9,37),(11,34),(15,32),(20,32),(25,32),(30,31),(33,28),(35,28),(37,22),(39,18),(43,12),(48,11),(51,11),(50,5),(48,0),(44,-5),(40,-10),(38,-15),(36,-19),(34,-23),(33,-26),(30,-30),(27,-33),(22,-35),(19,-35),(16,-32),(14,-27),(12,-18),(12,-13),(10,-5),(9,4),(4,6),(-4,5),(-8,5),(-13,8),(-17,12),(-17,15)]
EU=[(-10,36),(-9,43),(-4,48),(-2,49),(0,51),(3,53),(5,58),(8,57),(11,58),(14,55),(18,56),(21,55),(24,58),(24,60),(28,62),(30,66),(30,70),(35,68),(40,68),(45,68),(50,69),(55,69),(60,69),(68,73),(75,73),(85,75),(95,76),(105,77),(115,74),(125,73),(135,72),(145,72),(155,70),(165,67),(170,66),(178,65),(173,64),(170,60),(163,60),(162,56),(158,52),(156,51),(150,59),(142,50),(141,45),(140,40),(137,35),(132,33),(129,32),(127,35),(126,38),(122,38),(122,30),(120,26),(118,24),(112,21),(108,18),(105,9),(103,7),(100,6),(98,10),(97,16),(94,17),(92,21),(89,22),(86,20),(83,17),(80,13),(77,8),(76,10),(73,16),(71,21),(68,23),(66,25),(62,25),(58,26),(55,27),(52,28),(50,29),(48,30),(46,29),(44,29),(41,31),(40,36),(37,36),(34,36),(31,36),(28,37),(26,38),(23,40),(21,40),(19,42),(16,40),(14,42),(12,44),(9,44),(6,43),(3,43),(0,40),(-2,37),(-5,36),(-9,37),(-10,36)]
AU=[(114,-22),(114,-30),(115,-35),(118,-35),(124,-33),(129,-32),(132,-32),(135,-35),(138,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(151,-24),(148,-20),(146,-19),(143,-15),(142,-11),(137,-12),(135,-12),(132,-12),(130,-13),(126,-14),(122,-14),(118,-20),(114,-22)]
GL=[(-55,60),(-48,60),(-43,60),(-40,64),(-35,66),(-30,68),(-24,70),(-22,71),(-25,76),(-30,78),(-38,80),(-45,79),(-52,77),(-58,76),(-60,74),(-58,70),(-55,64),(-55,60)]
JP=[(130,31),(132,33),(134,34),(136,35),(138,35),(140,36),(140,39),(141,41),(142,42),(143,43),(145,44),(143,43),(141,40),(140,38),(138,36),(135,34),(133,34),(131,32),(130,31)]
ID=[(95,5),(98,3),(100,0),(103,-2),(106,-6),(110,-7),(114,-8),(118,-9),(122,-9),(126,-8),(130,-4),(132,-1),(135,-2),(138,-4),(141,-3),(141,-1),(138,0),(135,0),(131,0),(127,0),(123,0),(119,-1),(115,-3),(110,-6),(106,-6),(102,-3),(98,2),(95,5)]
NZ=[(167,-45),(169,-44),(172,-42),(174,-41),(176,-40),(178,-38),(177,-37),(175,-36),(174,-35),(173,-35),(171,-38),(169,-41),(167,-44),(167,-45)]
UK=[(-5,50),(-3,53),(-5,56),(-3,58),(-1,57),(0,53),(1,51),(-1,50),(-5,50)]
CONT=[NA,SA,AF,EU,AU,GL,JP,ID,NZ,UK]
RCOL={"ME":(178,34,34),"ASIA":(0,122,62),"EU":(18,84,180),"AFR":(198,138,0),"AM":(122,62,168),"WS":(0,138,138)}
PINS=[(24.7,46.7,1,"ME"),(31.2,121.5,2,"ASIA"),(40.7,-74.0,3,"AM"),(47.8,35.2,4,"EU"),(14.7,-17.4,5,"AFR"),(26.5,56.2,6,"ME"),(40.7,-74.0,7,"AM"),(47.7,-122.1,8,"AM"),(39.8,30.5,9,"EU"),(10.4,-75.5,10,"AM"),(12.8,45.0,11,"ME"),(13.0,44.9,12,"ME"),(39.8,98.5,13,"WS")]
POFF={7:(11,-9),12:(-10,8)}
def draw_map(d,x0,y0,mw,mh):
    d.rectangle([x0,y0,x0+mw,y0+mh],fill=(213,231,240),outline=LINE)
    def px(lon,lat): return x0+(lon+180)/360*mw, y0+(72-lat)/130*mh
    for poly in CONT: d.polygon([px(lo,la) for lo,la in poly],fill=(176,196,148),outline=(118,140,104))
    for lat,lon,n,rg in PINS:
        ox,oy=POFF.get(n,(0,0)); cx,cy=px(lon,lat); cx+=ox; cy+=oy
        d.ellipse([cx-7,cy-7,cx+7,cy+7],fill=RCOL[rg],outline=(255,255,255),width=1); d.text((cx,cy-0.5),str(n),font=fb(8),fill=(255,255,255),anchor="mm")
def night_sky(d,x0,y0,w,h):
    d.rectangle([x0,y0,x0+w,y0+h],fill=(16,24,52))
    for sx,sy in [(8,10),(30,22),(55,8),(80,26),(120,12),(150,20),(180,9),(210,24),(240,14),(270,8),(300,18)]:
        d.ellipse([x0+sx%w,y0+sy%h,x0+sx%w+2,y0+sy%h+2],fill=(255,255,220))
def hero_riyadh(d,x0,y0,w,h):
    night_sky(d,x0,y0,w,h)
    import random; r=random.Random(7)
    for i,bx in enumerate(range(0,w,26)):
        bh=34+r.randint(0,34); d.rectangle([x0+bx,y0+h-bh,x0+bx+20,y0+h],fill=(34,44,78))
        for wy in range(y0+h-bh+6,y0+h-4,9):
            for wx in range(x0+bx+4,x0+bx+17,7):
                if r.random()<0.45: d.rectangle([wx,wy,wx+3,wy+4],fill=(255,214,120))
    tx=x0+w//2-13; d.polygon([(tx,y0+h),(tx+4,y0+18),(tx+22,y0+18),(tx+26,y0+h)],fill=(96,116,178))
    for wy in range(y0+24,y0+h-6,10):
        for wx in (tx+8,tx+14):
            d.rectangle([wx,wy,wx+3,wy+5],fill=(255,214,120))
    d.ellipse([x0+w//2-26,y0+2,x0+w//2+26,y0+34],fill=(255,120,30)); d.ellipse([x0+w//2-16,y0+8,x0+w//2+16,y0+30],fill=(255,210,90))
    d.ellipse([x0+w//2-2,y0+30,x0+w//2+30,y0+52],fill=(120,120,128)); d.ellipse([x0+w//2+8,y0+18,x0+w//2+34,y0+38],fill=(150,150,158))
    dx,dy=x0+w-58,y0+26; d.rectangle([dx-3,dy-1,dx+3,dy+1],fill=(30,30,34)); d.rectangle([dx-14,dy-10,dx-6,dy-6],fill=(60,60,66)); d.rectangle([dx+6,dy-10,dx+14,dy-6],fill=(60,60,66))
    d.line([dx-14,dy-10,dx-6,dy-6],fill=(200,200,200)); d.line([dx+6,dy-10,dx+14,dy-6],fill=(200,200,200)); d.ellipse([dx-2,dy-4,dx+2,dy],fill=(255,60,60))
def hero_shanghai(d,x0,y0,w,h):
    d.rectangle([x0,y0,x0+w,y0+h],fill=(196,52,44))
    d.rectangle([x0+18,y0+22,x0+w-18,y0+h],fill=(228,214,196))
    d.polygon([(x0+8,y0+24),(x0+w//2,y0+4),(x0+w-8,y0+24)],fill=(150,28,24))
    for i in range(5):
        cx=x0+34+i*(w-68)//4; d.rectangle([cx,y0+30,cx+12,y0+h-16],fill=(178,34,30))
    d.rectangle([x0+w//2-26,y0+h-44,x0+w//2+26,y0+h-16],fill=(90,30,26))
    d.rectangle([x0+w-96,y0+h-52,x0+w-14,y0+h-10],fill=(255,255,255),outline=(120,120,120))
    for i in range(5): d.line([x0+w-88,y0+h-44+i*7,x0+w-22,y0+h-44+i*7],fill=(150,150,150))
    d.ellipse([x0+w-52,y0+h-46,x0+w-24,y0+h-18],outline=(196,52,44),width=3); d.text((x0+w-38,y0+h-38),"CCDI",font=fb(8),fill=(196,52,44),anchor="mm")
    d.rectangle([x0+22,y0+h-58,x0+92,y0+h-18],fill=(255,255,255),outline=(120,120,120))
    for i in range(4): d.line([x0+30,y0+h-50+i*8,x0+84,y0+h-50+i*8],fill=(150,150,150))
def hero_court(d,x0,y0,w,h):
    d.rectangle([x0,y0,x0+w,y0+h],fill=(214,224,236))
    d.polygon([(x0+14,y0+10),(x0+w//2,y0-6),(x0+w-14,y0+10)],fill=(96,110,138))
    for i in range(5):
        cx=x0+26+i*(w-52)//4; d.rectangle([cx,y0+12,cx+12,y0+h-22],fill=(240,240,236),outline=(150,150,150))
    d.rectangle([x0+10,y0+h-22,x0+w-10,y0+h-16],fill=(120,120,124)); d.rectangle([x0+4,y0+h-14,x0+w-4,y0+h],fill=(90,90,94))
    import math
    cx,cy=x0+w-52,y0+h-34
    for k in range(6):
        a=math.radians(-70+k*28); d.polygon([(cx,cy),(cx+22*math.cos(a),cy+22*math.sin(a)),(cx+30*math.cos(a+0.22),cy+30*math.sin(a+0.22))],fill=(214,48,49))
    d.ellipse([cx-6,cy-6,cx+6,cy+6],fill=(214,48,49))
    gx,gy=x0+34,y0+h-46; d.line([gx,gy,gx+34,gy-12],fill=(120,74,40),width=4); d.rectangle([gx+30,gy-22,gx+52,gy-8],fill=(90,52,28))
def strip(d,x0,y0,w,h,kind):
    sky={"drone":(18,26,54),"trophy":(24,48,88),"ship":(30,90,140),"chart":(24,48,88),"server":(40,20,24),"heli":(150,180,210),"shop":(240,220,180),"desert":(232,200,140),"strike":(120,40,30),"rocket":(12,18,44)}[kind]
    d.rectangle([x0,y0,x0+w,y0+h],fill=sky)
    if kind=="drone":
        for bx in range(0,w,22): d.rectangle([x0+bx,y0+h-16-rand(bx),x0+bx+16,y0+h],fill=(8,12,28))
        d.ellipse([x0+w-40,y0+6,x0+w-16,y0+30],fill=(255,120,30)); d.rectangle([x0+w-64,y0+14,x0+w-58,y0+18],fill=(40,40,44))
    elif kind=="trophy":
        d.polygon([(x0+w//2-16,y0+8),(x0+w//2+16,y0+8),(x0+w//2+10,y0+26),(x0+w//2-10,y0+26)],fill=(240,190,60)); d.rectangle([x0+w//2-3,y0+26,x0+w//2+3,y0+34],fill=(240,190,60)); d.rectangle([x0+w//2-12,y0+34,x0+w//2+12,y0+38],fill=(240,190,60))
        d.rectangle([x0+10,y0+10,x0+26,y0+34],fill=(0,122,62)); d.rectangle([x0+w-26,y0+10,x0+w-10,y0+34],fill=(178,34,34))
    elif kind=="ship":
        d.rectangle([x0,y0+h-14,x0+w,y0+h],fill=(18,60,110))
        d.rectangle([x0+20,y0+h-30,x0+w-20,y0+h-14],fill=(60,60,66))
        for i,c in enumerate([(200,60,50),(240,190,60),(60,120,200),(240,240,240)]): d.rectangle([x0+26+i*34,y0+h-42,x0+52+i*34,y0+h-30],fill=c)
        d.rectangle([x0+w-14,y0+4,x0+w-8,y0+h-30],fill=(120,120,126))
    elif kind=="chart":
        d.line([(x0+8,y0+h-10),(x0+w//3,y0+h-22),(x0+2*w//3,y0+16),(x0+w-8,y0+6)],fill=(255,214,120),width=3); d.line([(x0+8,y0+18),(x0+w-8,y0+18)],fill=(255,255,255),width=2)
        d.text((x0+w-52,y0+2),"50,018",font=fb(10),fill=(255,255,255))
    elif kind=="server":
        for i in range(3): d.rectangle([x0+12+i*52,y0+6,x0+56+i*52,y0+h-6],fill=(30,30,36),outline=(100,100,110))
        for i in range(3):
            for j in range(3): d.rectangle([x0+18+i*52,y0+12+j*10,x0+50+i*52,y0+18+j*10],fill=(255,60,60) if (i+j)%3==0 else (60,200,90))
    elif kind=="heli":
        d.polygon([(x0,y0+h),(x0+40,y0+8),(x0+80,y0+h)],fill=(120,140,160)); d.polygon([(x0+70,y0+h),(x0+130,y0+16),(x0+w,y0+h)],fill=(100,120,145))
        d.ellipse([x0+w//2-12,y0+10,x0+w//2+12,y0+22],fill=(40,40,46)); d.line([x0+w//2-24,y0+12,x0+w//2+24,y0+12],fill=(30,30,34),width=2); d.line([x0+w//2+12,y0+16,x0+w//2+30,y0+22],fill=(30,30,34),width=2)
    elif kind=="shop":
        d.rectangle([x0,y0+16,x0+w,y0+h],fill=(120,80,50))
        for i in range(6): d.polygon([(x0+i*w//6,y0+8),(x0+(i+1)*w//6,y0+8),(x0+(i+1)*w//6,y0+18),(x0+i*w//6,y0+18)],fill=(178,34,34) if i%2==0 else (255,255,255))
        d.rectangle([x0+w//2-20,y0+26,x0+w//2+20,y0+h],fill=(60,40,24))
    elif kind=="desert":
        d.rectangle([x0,y0+h-12,x0+w,y0+h],fill=(200,170,110)); d.line([(x0+8,y0+h-12),(x0+w-8,y0+10)],fill=(120,90,60),width=3)
        d.polygon([(x0+w-30,y0+8),(x0+w-12,y0+8),(x0+w-21,y0+22)],fill=(178,34,34)); d.text((x0+8,y0+4),"60 km",font=fb(10),fill=(120,60,20))
    elif kind=="strike":
        d.ellipse([x0+w//2-18,y0+6,x0+w//2+18,y0+34],fill=(255,120,30)); d.ellipse([x0+w//2-9,y0+12,x0+w//2+9,y0+28],fill=(255,210,90))
        d.rectangle([x0+12,y0+h-16,x0+w-12,y0+h-6],fill=(50,50,56)); d.rectangle([x0+30,y0+h-26,x0+70,y0+h-16],fill=(90,90,96))
    else:
        for sx,sy in [(12,8),(60,20),(120,6),(160,18)]: d.ellipse([x0+sx,y0+sy,x0+sx+2,y0+sy+2],fill=(255,255,220))
        d.polygon([(x0+w//2,y0+6),(x0+w//2+8,y0+26),(x0+w//2+4,y0+34),(x0+w//2-4,y0+34),(x0+w//2-8,y0+26)],fill=(240,240,240)); d.polygon([(x0+w//2-8,y0+26),(x0+w//2-16,y0+34),(x0+w//2-8,y0+32)],fill=(255,120,30)); d.polygon([(x0+w//2+8,y0+26),(x0+w//2+16,y0+34),(x0+w//2+8,y0+32)],fill=(255,120,30))
def rand(n): return (n*37+11)%14
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
NUMS=[("11","hurt in Riyadh"),("9","dead in Ukraine"),("50,018","Dow, first over 50k"),("+8.99%","Taiex, record high"),("25","dead or missing, Yemen"),("26","Cikande fire toll")]
HEROES=[("1 · RIYADH · MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","PIF tower struck for the 2nd time in a week. 11 hurt: 2 Saudi, 2 Indian, 3 Nepali, 4 Egyptian. 14:27 UTC. (Saudi officials)",hero_riyadh),("2 · SHANGHAI · ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen, 62, probed for \u201cserious violations\u201d \u2014 the 4th Politburo member to fall this year. (CCDI)",hero_shanghai),("3 · NEW YORK · US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","Jury convicts on trade-secret theft + bank fraud; cleared of racketeering. Sentence Sep 2027; Huawei to appeal. (US court)",hero_court)]
CARDS=[("4 · ZAPORIZHZHIA · EUROPE / WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","9 dead, 81 hurt. 96 drones launched, 73 downed or jammed. (Kyiv officials)","drone"),("5 · DAKAR · AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","Morocco forfeit 3\u20130; Senegal win 1\u20130. (CAS)","trophy"),("6 · HORMUZ · MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","Navigation cut, 18:58 UTC; exclusion zone north of Khasab, Oman. (UKMTO)","ship"),("7 · NEW YORK · MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","Dow 50,018. Nasdaq \u22121.5%; Taiex +8.99% record 40,122. (Exchanges)","chart"),("8 · REDMOND · TECH","REPORTED","Microsoft declares \u2018Code Red\u2019 after historic outage","After a 24-hour outage, global recovery target 1 hour; 11,000+ Teams messages. (Reuters)","server"),("9 · ESKISEHIR · EUROPE","REPORTED","Turkish military helicopter crash kills 5","AS-532 down in Eskisehir, 5 dead. 19:52 UTC. (Turkish officials)","heli"),("10 · CARTAGENA · AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","25 held; 5 elderly women freed; airport landings paused ~45 min. (Colombia)","shop"),("11 · ADEN · MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces 60 km from Aden, Yemen. 16:51 UTC. (Wires)","desert"),("12 · LAHJ · MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Bus and truck hit in Wadi Maabaq: 25 dead or missing, 6 hurt. 10:42 UTC. (Yemen)","strike"),("13 · JIUQUAN · SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","Shenzhou-24 crew: Tang Hongbo, Wu Yi, Muhammad Zeeshan Ali of Pakistan. (CMSA)","rocket")]
ALSO=["14 Ankara: Haftar visits Turkey for the first time (13:45 UTC)","15 London: UK sanctions Houthis + 4 officials","16 Villavicencio: Car bomb injures 23","17 Gaza: Israel kills Hamas internal security chief","18 Baghdad: Iraq orders federal control of Kurdish oilfields","19 Gaza: Meningitis epidemic alert \u2014 272 cases in October","20 DR Congo: Missing Cessna 208; rebels claim shootdown","21 Hanoi: Hot-pot explosion kills \u22656","22 Gulf of Finland: Ukraine hits Russian ship Sparta II","23 Kuala Lumpur: Malaysia to return thousands of migrants to Myanmar","24 Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ","25 Dhaka: Hasina plans return 16 Dec","26 The Hague: 14 nations endorse ICJ Myanmar ruling (9\u20136)","27 Jakarta: Indonesia nominates 2 VP candidates","28 Beijing: China sentences official Ma to death for spying","29 Brussels: NATO vows defence against space threat","30 Mexico City: El Chapo Isidro \u2014 US drone aided capture; Mexico to try him","31 San Salvador: Bukele names 3 soldiers killed in Haiti","32 Ottawa: Pentagon rebukes Canada \u2014 only 41.9% of air fleet ready","33 Washington: US adds Megaspeed to trade blacklist","34 Kyiv: Zelensky urges Ukraine/Russia/US/Europe talks soon","35 Ras Al Khaimah: UAE bus-truck crash kills 13","36 London: England record 5,258 heat deaths, summer 2026","37 Kourou: Ariane 6 lofts 36 Amazon satellites","38 Cikande: Factory-fire toll rises to 26"]
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img); MX=12; CW=W-2*MX; y=10
d.text((MX,y),"THE WORLD ON ONE DAY",font=fb(11),fill=RED); d.text((MX+CW,y),"38 STORIES \u00b7 7 REGIONS \u00b7 13 FIELDS \u00b7 ALL FROM TUESDAY 24 NOVEMBER 2026",font=fb(11),fill=INK,anchor="ra"); y+=17
d.text((MX,y),"Tuesday 24 November 2026",font=fs(30),fill=INK); y+=38
d.text((MX,y),"Riyadh tower hit again  \u00b7  Shanghai party chief probed  \u00b7  Huawei guilty 10 of 12",font=fs(13),fill=RED); y+=19
REG=[("Europe",7,(18,84,180)),("Middle East",8,(178,34,34)),("Asia",9,(0,122,62)),("Africa",5,(198,138,0)),("Americas",5,(122,62,168)),("Oceania",0,(120,120,120)),("World / Space",4,(0,138,138))]
bx=MX; tot=sum(c for _,c,_ in REG)
for name,c,col in REG:
    sw=max(6,CW*c/tot); d.rectangle([bx,y,bx+sw-2,y+16],fill=col)
    if sw>=90: d.text((bx+sw/2,y+3),f"{name} {c}",font=fb(8),fill=(255,255,255),anchor="ma")
    bx+=sw
y+=20; d.text((MX,y),"THE DAY IN UTC",font=fb(10),fill=RED); y+=14
cellw=(CW-70)/7; x=MX+70
for t,ev in UTC:
    d.text((x,y),t,font=fb(9),fill=RED); para(d,x,y+11,wrap(ev,fn(8),cellw-4),fn(8),lh=10); x+=cellw
y+=34; d.line([MX,y,MX+CW,y],fill=LINE); y+=5
d.text((MX,y),"THE DAY IN NUMBERS",font=fb(10),fill=RED); y+=13
cellw=CW/6; x=MX
for num,lab in NUMS:
    d.text((x+4,y),num,font=fs(19),fill=INK); d.text((x+4,y+22),lab,font=fn(8),fill=GREY); x+=cellw
y+=30; d.line([MX,y,MX+CW,y],fill=LINE); y+=6
hw=(CW-12)//3; hh=190
for i,(kick,ch,head,deck,fn_scene) in enumerate(HEROES):
    x0=MX+i*(hw+6); d.rectangle([x0,y,x0+hw,y+hh],fill=PAPER,outline=LINE)
    fn_scene(d,x0+1,y+1,hw-2,88); ty=y+94
    d.text((x0+7,ty),kick,font=fb(8.5),fill=NAVY); wch=fb(8).getlength(ch)+10; chip(d,x0+hw-7-wch,ty,ch)
    para(d,x0+7,ty+15,wrap(head,fs(12.5),hw-14),fs(12.5),lh=15)
    para(d,x0+7,ty+47,wrap(deck,fn(9.5),hw-14),fn(9.5),lh=12)
y+=hh+6
cw2=(CW-4*6)//5; ch2=118
for i,(kick,ch,head,deck,kind) in enumerate(CARDS):
    r,c=divmod(i,5); x0=MX+c*(cw2+6); y0=y+r*(ch2+6)
    d.rectangle([x0,y0,x0+cw2,y0+ch2],fill=PAPER,outline=LINE)
    strip(d,x0+1,y0+1,cw2-2,40,kind); ty=y0+44
    d.text((x0+6,ty),kick,font=fb(7.5),fill=NAVY); ty+=11
    ty=para(d,x0+6,ty,wrap(head,fs(10),cw2-12),fs(10),lh=12)
    ty=para(d,x0+6,ty+1,wrap(deck,fn(8.5),cw2-12),fn(8.5),lh=10)
    chip(d,x0+6,y0+ch2-16,ch)
y+=2*(ch2+6)
d.text((MX,y),"THE WORLD IN ONE MAP  \u2014  pins 1\u201313 = stories 1\u201313",font=fb(10),fill=RED)
d.text((MX+CW,y),"Red Middle East \u00b7 Green Asia \u00b7 Blue Europe \u00b7 Gold Africa \u00b7 Purple Americas \u00b7 Teal Space \u00b7 Oceania 0",font=fn(8.5),fill=GREY,anchor="ra"); y+=15
draw_map(d,MX,y,CW,76); y+=86
d.text((MX,y),"ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES",font=fb(10),fill=RED); y+=14
colw=(CW-20)//2
for i,line in enumerate(ALSO):
    c,r=divmod(i,13); x0=MX+c*(colw+20); d.text((x0,y+r*11),line,font=fn(9),fill=INK)
y+=13*11+6; d.line([MX,y,MX+CW,y],fill=LINE); y+=5
d.rectangle([MX,y,MX+CW,y+76],fill=(255,238,238),outline=RED)
d.text((MX+8,y+5),"DATE CHECK",font=fb(10),fill=RED)
para(d,MX+8,y+19,wrap("Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.",fn(9),CW-16),fn(9),lh=11)
para(d,MX+8,y+31,wrap("LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) \u00b7 Huang returns as Nvidia CEO (23 Nov) \u00b7 EU sanctions package 22 (23 Nov) \u00b7 COP31 ends no deal (22 Nov) \u00b7 Merkury sinks (22 Nov) \u00b7 El Chapo Isidro arrested (20 Nov) \u00b7 Cikande fire starts (21 Nov) \u00b7 Shenzhou-24 launch (25 Nov) \u00b7 Trump hush-money appeal ruling (23 Nov) \u00b7 ATP Finals (22 Nov) \u00b7 F1 Las Vegas GP (21 Nov) \u00b7 ICJ Myanmar ruling (last week).",fn(9),CW-16),fn(9),lh=11)
d.text((MX+8,y+57),"NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) \u00b7 Huawei sentence (Sep 2027) \u00b7 Hasina return (16 Dec) \u00b7 MPR VP vote (11 Dec) \u00b7 COP32 venue (undecided).",font=fn(9),fill=INK)
y+=80; d.line([MX,y,MX+CW,y],fill=LINE); y+=4
para(d,MX,y,wrap("Sources: dailysummaryof.com \u00b7 Reuters \u00b7 AP \u00b7 WSOC \u00b7 CCDI \u00b7 CAS \u00b7 UKMTO \u00b7 CMSA \u00b7 UKHSA.  CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side\u2019s claim.  Scenes are drawn illustrations, not photographs.",fn(8),CW),fn(8),lh=10)
out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); img.save(out,optimize=True)
print("saved",out,img.size)
