from collections import OrderedDict

class Twtokenizer():
    
    def __init__(self, lang='nl'):
        self.toReplaceDict = OrderedDict({'!!*':' ! ','\?':' ? ', '\"':' " ',"“":" “ ","”":" ” ", "\'\'*":"'","\' ":" ' "
    ," \'":" ' ","’ ":" ’ ",'&amp;':'&','&gt;':'>','&lt;':'<', '~~*':' ~ ',"¿¿*":" ¿ ",'\.\.\.':' ... ','\.\.':' .. '
    ,'…':' … ',"\(\(*":'(',"\)\)*":')',"\+\+*":'+',"\*\**":'*',"\|\|*":"|","\$\$*":"$","%%*":"%",">>*":">","<<*":"<","--*":"-" 
    ,"\/\/\/*":"//","(:d)(:d)*":":d",":ddd*":" :d ",":ppp*":" :p ",";;;*":";",":\* ":" :* ",":\(":" :( ","\(:":" (: ",":\)":" :) "
    ,'\):':' ): ',";\)":" ;) ","\+\+":" + ",":\|":" :| ",":-\)":" :-) ",";-\)":" ;-) ",":-\(":" :-( ",":\'\(":" :'( ",":p ":" :p "
    ,";p ":" ;p ",":d ":" :d ","-_-":" -_- ",":o\)":" :o) ",":\$":" :$ ","\.@":". @",'#':' #',' \.': ' . ','    ':' '
    ,'   ':' ','   ':' ','  ':' ',"😡😡*":" :( ","☺️☺️*":" :) ","😄😄*":" :d ","😃😃*":" :d ","😆😆*":" :d ","😷😷*":" :d "
    ,"😅😅*":" :d ","😋😋*":" :d ","😜😜*":" :p " ,"😝😝*":" :p ","😂😂*":" :'( ","😢😢*":" :'( ","😁😁*":" :( ","😞😞*":" :( "
    ,"😖😖*":" :( " ,"😥😥*":" :( ","😩😩*":" :( ","😊😊*":" :) ","😉😉*":" :) ","😎😎*":" :) " ,"😇😇*":" :) ","😭😭*":" :'d " 
    ,"😨😨*":" :| ","😏😏*":" :| " ,"😔😔*":" :| ","😒😒*":" :| ","😫😫*":" :( ","😪😪*":" :'( "
    ,"😰😰*":" :'( " ,"😍😍*":" <3 ","😘😘*":" <3 ","<33*":" <3 ","<3(<3)*":" <3 ","😳😳*":" 😳 ", "😻😻*":" 😻 ", "\n\n*":" \n ", "♪♪*":" ♪ "
    ,"💧💧*":" 💧 ", """\xa0""":" ", "\n":" . ","【【*":" 【 ","】】*":" 】 ","「「*":" 「 ","」」*":" 」 ","❤️❤️*":" <3 ","🎶🎶*":" 🎶 "
    ,"😌😌*":" :) ","💖💖*":" <3 ","😐😐*":" :| ","\.: ":" .: "})
    
    # '\. ': ' . ' --> deleted from toReplaceDict to be able to process the abbreviations.
        self.abbreviations_dict =  {"nl":['i.v.m.','a.s.','knp.','st.','St.','Aardoliemij.','Adm.','Adriaansz.','Afd.','Am.','Ant.','Anthoniszn.','Ave.','BMCie.','Bel.','Belastinggr.','Bfr.','Bijv.','Bk.','Blvd.','Br.','Bros.','Burg.','CHR.','Ch.','Chr.','Cie.','Co.','Com.','Corneliszn.','Corp.','CvN.','Cy.','Dep.','Dept.','Di.','Do.','Dhr.','Dr.','Drs.','Ed.','Em.','Eng.','Esq.','Eur.','Exc.','Exp.','F.','Fa.','Fam.','Fed.','Fl.','Fr.','Fred.','Gebr.','Gem.','Gen.','Gld.','H.','HH.','Hd.','Herv.','Hoogl.','Hr.','Hub.','Hzn.','Inc.','Ing.','Inl.','Inst.','Int.','Ir.','Isr.','It.','J-P.','Jac.','Jacq.','Jan.','Jhr.','Jkvr.','Joh.','Jr.','Jul.','Jzn.','KLu.','Kcal.','Kon.','Krj.','L.','Lat.','Ltd.','M.','Ma.','Mad.','Mass.','Mej.','Mevr.','Mgr.','Mij.','Min.','Mr.','Mrs.','Ms.','Mus.','Mw.','N.','NH.','NL.','Nd.','Ndl.','Ned.','Nic.','Nov.','O.','Oct.','Olym.','Org.','Oud-Eng.','P.','PE.','Pct.','PepsiCo.','Ph.','Phs.','Pol.','Prof.','Prov.','RED.','Red.','Rijkscomm.','RK.','Rom.','SEPT.','Sept.','Sj.','Sp.','Sr.','St.','Stbl.','Stct.','Sted.','TH.','Tel.','Th.','Tijdschr.','Tj.','Uitg.','Univ.','VS.','Ver.','Vic.','Vl.','Vlnr.','Vr.','Vz.','W.','Werkn.','Wo.','Z.','Za.','Zl.','Zn.','a.','aanv.','acad.','acc.','adj.','adm.','adv.','afb.','afd.','afk.','afl.','afz.','alg.','alt.','arr.','art.','asp.','ass.','atm.','aug.','beh.','beheerscomm.','ben.','benod.','betr.','bijv.','bijz.','bl.','blz.','br.','brab.','brandm.','btw.','bur.','bv.','c.','ca.','cal.','cand.','cao.','cap.','cat.','cc.','cf.','chr.','cm.','cod.','com.','commer.','comp.','coop.','cq.','ct.','deb.','dec.','derg.','dgl.','dgs.','dhr.','di.','dipl.','dir.','distr.','div.','do.','don.','dr.','drs.','ds.','dw.','ed.','eerste-luit.','eerw.','eig.','em.','enk.','enz.','etc.','ev.','evt.','ex.','excl.','f.','fa.','feb.','febr.','fec.','fig.','fl.','fol.','fr.','geb.','gebr.','gedipl.','geh.','gem.','gep.','gesch.','get.','gez.','gld.','gr.','gymn.','h.','herv.','hh.','hoogl.','hs.','ib.','ibid.','id.','ill.','imp.','impr.','inc.','incl.','indiv.','inf.','ing.','ink.','inl.','insp.','int.','intr.','inw.','inz.','ir.','it.','j.','jan.','jg.','jhr.','jl.','joh.','jr.','kHz.','kand.','kath.','kcal.','kg.','kl.','km.','l.','lb.','lib.','lic.','ll.','lt.','ltd.','m.','ma.','maj.','max.','med.','medew.','mej.','mevr.','mg.','mgr.','mil.','milj.','mld.','mln.','mm.','mnd.','mr.','mrd.','mrs.','mrt.','ms.','mtr.','muz.','mv.','mw.','n.','ned.','nl.','nom.','nov.','nr.','o.','oa.','ob.','obl.','okt.','olv.','ong.','ongeh.','onz.','opm.','opp.','or.','org.','oud-bevelv.','oud-penn.','oud-secr.','oud-voorz.','oud-vrijw.','oud-vrz.','p.','pCt.','pag.','par.','pct.','pd.','penn.','penningm.','perf.','persc.','pl.','plm.','plv.','pnt.','pr.','praes.','pres.','prk.','proc.','prof.','prot.','prov.','ps.','pt.','r.','re.','reg.','resp.','ret.','rk.','sc.','scholengem.','schr.','scr.','sec.','sept.','seq.','ser.','sin.','sing.','soc.','spr.','sq.','sr.','st.','subs.','subst.','sup.','t.','tab.','td.','tech.','temp.','terugbez.','tg.','tgov.','theel.','tit.','tv.','tw.','v.','vac.','var.','vdt.','verb.','verg.','versch.','vert.','vgl.','vice-voorz.','vice-vrz.','vid.','vlg.','vlgg.','vlnr.','vml.','vnl.','vnlr.','vnw.','voc.','voorl.','voorm.','voorw.','voorz.','vorstverl.','vr.','vrijw.','vrijwil.','vrijwill.','vrz.','vs.','wd.','weled.','weledelgeb.','weledelgestr.','weleerw.','werkg.','wo.','wsch.','z.','za.','zelfst.','zg.','zgn.','zn.','zog.','zw.','zwemb.',"t.h.v.","t.h.v"], 
            "en":['acc.','AD.','Adm.','al.','Ala.','anon.','Apr.','Ariz.','Ark.','arr.','assoc.','Aug.','av.','Ave.','Bancorp.','Bart.','BC.','Bhd.','Bros.','B.S.','B.Sc.','Calif.','cap.','Capt.','cf.','Cie.','Co.','CO.','col.','Col.','Colo.','comb.','comb.form.','compar.','Conn.','cont.','contd.','contr.','Corp.','CORP.','Cos.','COS.','cu.','Dec.','Del.','dept.','Dept.','dist.','div.','D-Mass.','doc.','doz.','Dr.','e.g.','esp.','Esq.','est.','etc.','Etc.','Ex.','Feb.','fem.','ff.','fig.','Fla.','for.','Fri.','ft.','Ga.','Gen.','gm.','Gov.','Hon.','Ill.','Inc.','INC.','Ind.','inst.','Jan.','Jansz.','Jos.','Jr.','Jul.','Jun.','Kan.','Ky.','La.','Lt.','Ltd.','M.A.','M.Sc.','MA.','MSc.','Maj.','masc.','Mass.','Md.','Messrs.','met.','Mfg.','Mich.','Minn.','Miss.','Mo.','Mon.','Mr.','Mrs.','Ms.','Neb.','neg.','Nev.','no.','No.','nom.','Nos.','Nov.','Oct.','Okla.','Ore.','Pa.','pass.','pers.','Ph.','phr.','pla.','poss.','pres.','Prof.','Prop.','Pty.','ref.','refl.','Rep.','Reps.','Rev.','sc.','Sen.','Sens.','Sept.','sing.','Sr.','St.','superl.','Tenn.','Tex.','Tues.','usu.','v.','Va.','var.','viz.','vs.','Vt.','Wash.','Wis.','Wyo.']}
        self.lang = lang
        print('The language is:',lang, 'Active Abbreviation List:',self.abbreviations_dict)

    def tokenize(self, tw):
        #abbcheck = False
        newtw = ''
        lentw = len(tw)
        #print(tw)
        for i, c in enumerate(tw):
            if (c in "'`´’‘") and ((i+1 != lentw) and (i!=0)) and ((tw[i-1].isalpha()) or tw[i-1] in "0123456789") and (tw[i+1].isalpha()):
                newtw += ' '+c+' '
            elif (c in "'`´’()+*-") and ((lentw>i+1) and (i>0)) and (tw[i-1] in ' 0123456789') and (tw[i+1].isalpha()):
                newtw += c+' '
            elif (c in '();>:') and ((lentw>i+1) and (i!=0)) and ((tw[i-1].isalpha()) or (tw[i-1] in '0123456789')) and ((tw[i+1] == ' ') or (i == lentw-1)):
                newtw += ' '+c
            elif (c in '.') and ((lentw>i+1) and (i!=0)) and ((tw[i-1].isalpha()) or (tw[i-1] in '0123456789')) and ((tw[i+1] == ' ') or (i == lentw-1)) \
                            and (newtw.split()[-1]+c not in self.abbreviations_dict[self.lang]):
                abbcheck = True
                newtw += " "+c
            elif (c in "'`´’‘()+*->") and (i==0) and (lentw > 1) and ((tw[1].isalpha()) or tw[1] in "0123456789"):
                newtw += c+' '
            elif (c in "'`´’‘()+*->") and (i+1 == lentw) and (lentw > 1) and ((tw[i-1].isalpha()) or tw[i-1] in "0123456789"):
                newtw += ' '+c
            elif (c in ",") and ((i != 0) and (i+1 != lentw)) and tw[i-1].isdigit() and tw[i+1].isdigit(): # for 3,5 7,5
                newtw += c
            elif (c in ",&"):
                newtw += " "+c+" "
            elif (c in "â"): # create a dictionary for character mappings. if c in dict: newtw += dict[c]
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
            #if abbcheck:
            #    print("abbcheck is true:",newtw.split())
            #print(i,c,(c in '.'), ((lentw>i+1) and (i!=0)), ((tw[i-1].isalpha()) or (tw[i-1] in '0123456789')), ((tw[i+1] == ' ') or (i == lentw-1)) \
            #                and (newtw.split()[-1]+c not in self.abbreviations))
        #print('\n\n')
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
        #tokdf[rescol] = tokdf[newtexcol].str.split()
        
        if addLowerTok:
            tokdf[newtexcol[:-3]] = tokdf[newtexcol].str.lower()
    
        return tokdf.copy()
