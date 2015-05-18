from collections import OrderedDict

class twtokenizer():
    
    def __init__(self):
        self.toReplaceDict = OrderedDict({'!!*':' ! ','\?':' ? ', '\"':' " ',"“":" “ ","”":" ” ", "\'\'*":"'","\' ":" ' "
    ," \'":" ' ","’ ":" ’ ",'&amp;':'&','&gt;':'>','&lt;':'<', '~~*':' ~ ',"¿¿*":" ¿ ",'\.\.\.':' ... ','\.\.':' .. '
    ,'…':' … ',"\(\(*":'(',"\)\)*":')',"\+\+*":'+',"\*\**":'*',"\|\|*":"|","\$\$*":"$","%%*":"%",">>*":">","<<*":"<","--*":"-" 
    ,"\/\/\/*":"//","(:d)(:d)*":":d",":ddd*":" :d ",":ppp*":" :p ",";;;*":";",":\* ":" :* ",":\(":" :( ","\(:":" (: ",":\)":" :) "
    ,'\):':' ): ',";\)":" ;) ","\+\+":" + ",":\|":" :| ",":-\)":" :-) ",";-\)":" ;-) ",":-\(":" :-( ",":\'\(":" :'( ",":p ":" :p "
    ,";p ":" ;p ",":d ":" :d ","-_-":" -_- ",":o\)":" :o) ",":\$":" :$ ","\.@":". @",'#':' #','\. ': ' . ',' \.': ' . ','    ':' '
    ,'   ':' ','   ':' ','  ':' ',"😡😡*":" :( ","☺️☺️*":" :) ","😄😄*":" :d ","😃😃*":" :d ","😆😆*":" :d ","😷😷*":" :d "
    ,"😅😅*":" :d ","😋😋*":" :d ","😜😜*":" :p " ,"😝😝*":" :p ","😂😂*":" :'( ","😢😢*":" :'( ","😁😁*":" :( ","😞😞*":" :( "
    ,"😖😖*":" :( " ,"😥😥*":" :( ","😩😩*":" :( ","😊😊*":" :) ","😉😉*":" :) ","😎😎*":" :) " ,"😇😇*":" :) ","😭😭*":" :'d " 
    ,"😨😨*":" :| ","😏😏*":" :| " ,"😔😔*":" :| ","😒😒*":" :| ","😫😫*":" :( ","😪😪*":" :'( "
    ,"😰😰*":" :'( " ,"😍😍*":" <3 ","😘😘*":" <3 ","<33*":" <3 ","<3(<3)*":" <3 ","😳😳*":" 😳 ", "😻😻*":" 😻 ", "\n\n*":" \n ", "♪♪*":" ♪ "
    ,"💧💧*":" 💧 ", """\xa0""":" ", "\n":" . ","【【*":" 【 ","】】*":" 】 ","「「*":" 「 ","」」*":" 」 ","❤️❤️*":" <3 ","🎶🎶*":" 🎶 "
    ,"😌😌*":" :) ","💖💖*":" <3 ","😐😐*":" :| ","\.: ":" .: "})

    def tokenize(self, tw):
        newtw = ''
        lentw = len(tw)
        for i, c in enumerate(tw):
            if (c in "'`´’‘") and ((i+1 != lentw) and (i!=0)) and ((tw[i-1].isalpha()) or tw[i-1] in "0123456789") and (tw[i+1].isalpha()):
                newtw += ' '+c+' '
            elif (c in "'`´’()+*-") and ((lentw>i+1) and (i>0)) and (tw[i-1] in ' 0123456789') and (tw[i+1].isalpha()):
                newtw += c+' '
            elif (c in '();>:.') and ((lentw>i+1) and (i!=0)) and ((tw[i-1].isalpha()) or (tw[i-1] in '0123456789')) and ((tw[i+1] == ' ') or (i == lentw-1)):
                newtw += ' '+c
            elif (c in "'`´’‘()+*->") and (i==0) and (lentw > 1) and ((tw[1].isalpha()) or tw[1] in "0123456789"):
                newtw += c+' '
            elif (c in "'`´’‘()+*->") and (i+1 == lentw) and (lentw > 1) and ((tw[i-1].isalpha()) or tw[i-1] in "0123456789"):
                newtw += ' '+c
            elif (c in ",") and ((i != 0) and (i+1 != lentw)) and tw[i-1].isdigit() and tw[i+1].isdigit(): # for 3,5 7,5
                newtw += c
            elif (c in ",&"):
                newtw += " "+c+" "
            elif (c in "â"):
                newtw += "a"
            elif (c in "ê"):
                newtw += "e"
            elif (c in "î"):
                newtw += "i"
            elif (c in "ú"):
                newtw += "ü"
            #elif (c in ":")
            else:
                newtw += c
            #print(c in "'`´’()+*-", lentw>i+1, i>0, tw[i-1] == ' 0123456789', tw[i+1].isalpha())
                
        return newtw

    def tokenize_df(self, tokdf,texcol="tweet", newtexcol='texttokCap',rescol="ttextlist", addLowerTok=True):
        #concert_table.drop_duplicates()
        # Note
        # tokdf[newtexcol] = tokdf[newtexcol].str.replace("""\xa0"""," ")
        # tokdf[newtexcol] = tokdf[newtexcol].str.replace("\n"," . ")
        
        tokdf[newtexcol] = tokdf[texcol].copy()
    
        tokdf[newtexcol] = tokdf[newtexcol].replace(self.toReplaceDict, regex=True)
        tokdf[newtexcol][tokdf[newtexcol].str.endswith(".")] = tokdf[tokdf[newtexcol].str.endswith(".")][newtexcol].apply(lambda tw: tw[:-1]+' .') 
        tokdf[newtexcol][tokdf[newtexcol].str.endswith(".'")] = tokdf[tokdf[newtexcol].str.endswith(".'")][newtexcol].apply(lambda tw: tw[:-2]+" . '") 
        tokdf[newtexcol][tokdf[newtexcol].str.startswith("'")] = tokdf[tokdf[newtexcol].str.startswith("'")][newtexcol].apply(lambda tw: "' "+tw[1:])
    
        tokdf[newtexcol] = tokdf[newtexcol].apply(self.tokenize)
        tokdf[newtexcol] = tokdf[newtexcol].str.strip()
        tokdf[rescol] = tokdf[newtexcol].str.split()
        
        if addLowerTok:
            tokdf[newtexcol[:-3]] = tokdf[newtexcol].str.lower()
    
        return tokdf.copy()
