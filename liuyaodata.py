#coding=utf-8
#阳1阴2老阳3老阴4
#             6-1爻六亲                                           世应爻合冲 宫
a1=['父戌土','兄申金','官午火','父辰土','财寅木','孙子水',6,3,'六冲','','乾宫']
a2=['父戌土','兄申金','官午火','兄酉金','孙亥水','父丑土',1,4,'','','乾宫']
a3=['父戌土','兄申金','官午火','兄申金','官午火','父辰土',2,5,'','','乾宫']
a4=['父戌土','兄申金','官午火','财卯木','官巳火','父未土',3,6,'六合','','乾宫']
a5=['财卯木','官巳火','父未土','财卯木','官巳火','父未土',4,1,'','','乾宫']
a6=['财寅木','孙子水','父戌土','财卯木','官巳火','父未土',5,2,'','','乾宫']
a7=['官巳火','父未土','兄申金','财卯木','官巳火','父未土',4,1,'','游魂卦','乾宫']
a8=['财卯木','官巳火','父未土','财卯木','官巳火','父未土',3,6,'','归魂卦','乾宫']

b1=['父未土','兄酉金','孙亥水','父丑土','财卯木','官巳火',6,3,'六冲','','兑宫']
b2=['父未土','兄酉金','孙亥水','官午火','父辰土','财寅木',1,4,'六合','','兑宫']
b3=['父未土','兄酉金','孙亥水','财卯木','官巳火','父未土',2,5,'','','兑宫']
b4=['父未土','兄酉金','孙亥水','兄申金','官午火','父辰土',3,6,'','','兑宫']
b5=['孙子水','父戌土','兄申金','兄申金','官午火','父辰土',4,1,'','','兑宫']
b6=['兄酉金','孙亥水','父丑土','兄申金','官午火','父辰土',5,2,'','','兑宫']
b7=['父戌土','兄申金','官午火','兄申金','官午火','父辰土',4,1,'','游魂卦','兑宫']
b8=['父戌土','兄申金','官午火','父丑土','财卯木','官巳火',3,6,'','归魂卦','兑宫']

c1=['兄巳火','孙未土','财酉金','官亥水','孙丑土','父卯木',6,3,'六冲','','离宫']
c2=['兄巳火','孙未土','财酉金','财申金','兄午火','孙辰土',1,4,'六合','','离宫']
c3=['兄巳火','孙未土','财酉金','财酉金','官亥水','孙丑土',2,5,'','','离宫']
c4=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',3,6,'','','离宫']
c5=['父寅木','官子水','孙戌土','兄午火','孙辰土','父寅木',4,1,'','','离宫']
c6=['父卯木','兄巳火','孙未土','兄午火','孙辰土','父寅木',5,2,'','','离宫']
c7=['孙戌土','财申金','兄午火','兄午火','孙辰土','父寅木',4,1,'','游魂卦','离宫']
c8=['孙戌土','财申金','兄午火','官亥水','孙丑土','父卯木',3,6,'','归魂卦','离宫']

d1=['兄巳火','孙未土','财酉金','官亥水','孙丑土','父卯木',6,3,'六冲','','震宫']
d2=['兄巳火','孙未土','财酉金','财申金','兄午火','孙辰土',1,4,'六合','','震宫']
d3=['兄巳火','孙未土','财酉金','财酉金','官亥水','孙丑土',2,5,'','','震宫']
d4=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',3,6,'','','震宫']
d5=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',4,1,'','','震宫']
d6=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',5,2,'','','震宫']
d7=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',4,1,'','游魂卦','震宫']
d8=['兄巳火','孙未土','财酉金','兄午火','孙辰土','父寅木',3,6,'','归魂卦','震宫']

e1=['兄卯木','孙巳火','财未土','官酉金','父亥水','财丑土',6,3,'六冲','','巽宫']
e2=['兄卯木','孙巳火','财未土','财辰土','兄寅木','父子水',1,4,'六合','','巽宫']
e3=['兄卯木','孙巳火','财未土','父亥水','财丑土','兄卯木',2,5,'','','巽宫']
e4=['兄卯木','孙巳火','财未土','财辰土','兄寅木','父子水',3,6,'','','巽宫']
e5=['财戌土','官申金','孙午火','财辰土','兄寅木','父子水',4,1,'','','巽宫']
e6=['孙巳火','财未土','官酉金','财辰土','兄寅木','父子水',5,2,'','','巽宫']
e7=['兄寅木','父子水','财戌土','财辰土','兄寅木','父子水',4,1,'','游魂卦','巽宫']
e8=['兄寅木','父子水','财戌土','官酉金','父亥水','财丑土',3,6,'','归魂卦','巽宫']

f1=['兄子水','官戌土','父申金','财午火','官辰土','孙寅木',6,3,'六冲','','坎宫']
f2=['兄子水','官戌土','父申金','官丑土','孙卯木','财巳火',1,4,'六合','','坎宫']
f3=['兄子水','官戌土','父申金','官辰土','孙寅木','兄子水',2,5,'','','坎宫']
f4=['兄子水','官戌土','父申金','兄亥水','官丑土','孙卯木',3,6,'','','坎宫']
f5=['官未土','父酉金','兄亥水','兄亥水','官丑土','孙卯木',4,1,'','','坎宫']
f6=['官戌土','父申金','财午火','兄亥水','官丑土','孙卯木',5,2,'','','坎宫']
f7=['父酉金','兄亥水','官丑土','兄亥水','官丑土','孙卯木',4,1,'','游魂卦','坎宫']
f8=['父酉金','兄亥水','官丑土','财午火','官辰土','孙寅木',3,6,'','归魂卦','坎宫']

g1=['官寅木','财子水','兄戌土','孙申金','父午火','兄辰土',6,3,'六冲','','艮宫']
g2=['官寅木','财子水','兄戌土','财亥水','兄丑土','官卯木',1,4,'六合','','艮宫']
g3=['官寅木','财子水','兄戌土','兄辰土','官寅木','财子水',2,5,'','','艮宫']
g4=['官寅木','财子水','兄戌土','兄丑土','官卯木','父巳火',3,6,'','','艮宫']
g5=['父巳火','兄未土','孙酉金','兄丑土','官卯木','父巳火',4,1,'','','艮宫']
g6=['兄戌土','孙申金','父午火','兄丑土','官卯木','父巳火',5,2,'','','艮宫']
g7=['官卯木','父巳火','兄未土','兄丑土','官卯木','父巳火',4,1,'','游魂卦','艮宫']
g8=['官卯木','父巳火','兄未土','孙申金','父午火','兄辰土',3,6,'','归魂卦','艮宫']

h1=['孙酉金','财亥水','兄丑土','官卯木','父巳火','兄未土',6,3,'六冲','','坤宫']
h2=['孙酉金','财亥水','兄丑土','兄辰土','官寅木','财子水',1,4,'六合','','坤宫']
h3=['孙酉金','财亥水','兄丑土','兄丑土','官卯木','父巳火',2,5,'','','坤宫']
h4=['孙酉金','财亥水','兄丑土','兄辰土','官寅木','财子水',3,6,'','','坤宫']
h5=['兄戌土','孙申金','父午火','兄辰土','官寅木','财子水',4,1,'','','坤宫']
h6=['兄未土','孙酉金','财亥水','兄辰土','官寅木','财子水',5,2,'','','坤宫']
h7=['财子水','兄戌土','孙酉金','兄辰土','官寅木','财子水',4,1,'','游魂卦','坤宫']
h8=['财子水','兄戌土','孙申金','官卯木','父巳火','兄未土',3,6,'','归魂卦','坤宫']
#从初爻到上爻
gua64={
		'111111':a1,'211111':a2,'221111':a3,'222111':a4,'222211':a5,'222221':a6,'222121':a7,'111121':a8,'112112':b1,'212112':b2,'222112':b3,'221112':b4,'221212':b5,'221222':b6,'221122':b7,'112122':b8,'121121':c1,'221121':c2,'211121':c3,'212121':c4,'212221':c5,'212211':c6,'212111':c7,'121111':c8,'122122':d1,'222122':d2,'212122':d3,'211122':d4,'211222':d5,'211212':d6,'211112':d7,'122112':d8,'211211':e1,'111211':e2,'121211':e3,'122211':e4,'122111':e5,'122121':e6,'122221':e7,'211221':e8,'121112':f1,'112212':f2,'122212':f3,'121212':f4,'121112':f5,'121122':f6,'121222':f7,'212222':f8,'221221':g1,'121221':g2,'111221':g3,'112221':g4,'112121':g5,'112111':g6,'112211':g7,'221211':g8,'222222':h1,'122222':h2,'112222':h3,'111222':h4,'111122':h5,'111112':h6,'111212':h7,'222212':h8

		}
if __name__=='__main__':
	print gua64['111111'][0].decode('utf-8')