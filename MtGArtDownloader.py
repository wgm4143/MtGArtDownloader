import os
import urllib

#Last updated 5/13/2020
#https://www.mtgpics.com/sets

#(Acronym for set, number of card images)
sets = [

  #Starter sets
  ("por", 222),
  ("psa", 165),
  ("ptk", 180),
  ("sta", 173),
  ("s2k", 20),
  
  #Core
  ("alp", 295),
  ("bet", 302),
  ("abu", 302),
  ("rev", 306),
  ("4th", 378),
  ("5th", 449),
  ("6th", 350),
  ("7th", 350),
  ("8th", 357),
  ("9th", 359),
  ("xth", 389),
  ("10m", 257),
  ("11m", 255),
  ("12m", 256),
  ("13m", 260),
  ("14m", 262),
  ("15m", 298),
  ("ori", 303),
  ("m19", 332),
  ("m20", 356),

  #Commander
  ("cmd", 318),
  ("cma", 28),
  ("13c", 356),
  ("14c", 373),
  ("15c", 366),
  ("16c", 374),
  ("can", 340),
  ("17c", 320),
  ("cm2", 331),
  ("c18", 333),
  ("c19", 331),
  ("c20", 341),

  #Masters
  ("mma", 245),
  ("mmb", 265),
  ("ema", 265),
  ("mmc", 270),
  ("ima", 256),
  ("25m", 264),
  ("ulm", 270),

  #Duel Decks
  ("evg", 65),
  ("jvc", 63),
  ("dvd", 65),
  ("gvl", 66),
  ("pvc", 74),
  ("evt", 80),
  ("kvd", 82),
  ("avn", 82),
  ("vvk", 79),
  ("ivg", 91),
  ("svt", 81),
  ("hvm", 83),
  ("jvv", 89),
  ("svc", 82),
  ("dda", 260),
  ("evk", 67),
  ("zve", 80),
  ("bvc", 80),
  ("nvo", 76),
  ("mvm", 72),
  ("mvg", 66),
  ("evi", 80),

  #Signature Spellbook  
  ("ss1", 8),
  ("ss2", 8),

  #Masterpiece
  ("zex", 45),
  ("kli", 54),
  ("aki", 54),
  ("myt", 16),
  ("uma", 40),
  ("my2", 13),
  ("my3", 11),

  #Land sets
  ("apa", 15),
  ("gur", 6),
  ("eur", 15),

  #Un Sets
  ("ung", 94),
  ("2un", 45),
  ("unh", 141),
  ("ust", 236),
  ("und", 102),

  #Modern
  ("mh1", 276),

  #Global Series
  ("gs1", 42),

  #Conspiracy
  ("csn", 219),
  ("2cn", 234),
  
  #Archenemy
  ("ard", 150),
  ("arc", 45),
  ("and", 111),
  ("anb", 20),

  #Art Series
  ("as1", 54),

  #Old Promo
  ("vir", 116),
  ("pmo", 23),
  ("aaa", 71),
  ("are", 83),
  ("jss", 18),
  ("mpt", 24),
  ("rew", 53),
  ("gat", 86),
  
  #Current Promo
  ("dci", 143),
  ("pmo", 548),
  ("pre", 1553),
  ("10p", 1553),
  ("fnm", 230),
  ("pst", 424),

  #From the Vault
  ("fvd", 15),
  ("fve", 15),
  ("fvr", 15),
  ("fvl", 15),
  ("fre", 15),
  ("fvt", 20),
  ("anh", 15),
  ("fva", 15),
  ("fvo", 16),
  ("ftr", 15),

  #Premium Decks
  ("sli", 41),
  ("fir", 34),
  ("gra", 30),

  #Alternative Magic
  ("vab", 32),
  ("thh", 21),
  ("thc", 15),
  ("bnc", 15),
  ("joc", 15),
  ("eoi", 48),
  ("bbd", 264),
  ("gnt", 68),
  ("gn2", 64),

  #Planechase
  ("pcd", 169),
  ("pch", 40),
  ("2pd", 156),
  ("2pc", 40),
  ("pad", 175),
  ("pca", 86),

  #MtG Online Sets
  ("1me", 195),
  ("2me", 245),
  ("3me", 230),
  ("4me", 260),
  ("vma", 325),
  ("tpr", 269),
  
  #Misc. Reprints
  ("sum", 306),
  ("ren", 122),
  ("chr", 125),
  ("i2p", 67),
  ("ath", 85),
  ("bro", 136),
  ("bea", 90),
  ("dec", 58),
  ("cst", 62),
  ("dop", 113),
  ("med", 30),
  ("16w", 16),
  ("17w", 30),
  ("gk1", 138),
  ("gk2", 142),
  ("sld", 536),
  ("myb", 1936),
  ("mys", 1936),

  #Blocks
  ("ara", 78),
  ("ant", 100),
  ("leg", 310),
  ("dar", 119),
  ("fal", 187),
  ("hom", 140),
  ("ice", 383),
  ("all", 199),
  ("col", 155),
  ("mir", 350),
  ("vis", 167),
  ("wea", 167),
  ("tem", 350),
  ("str", 143),
  ("exo", 143),
  ("urs", 350),
  ("url", 143),
  ("urd", 143),
  ("mer", 350),
  ("nem", 143),
  ("pro", 143),
  ("inv", 350),
  ("pla", 143),
  ("apo", 143),
  ("ody", 350),
  ("tor", 143),
  ("jud", 143),
  ("ons", 350),
  ("lgi", 145),
  ("sco", 143),
  ("mrd", 306),
  ("drs", 165),
  ("fda", 165),
  ("chk", 306),
  ("bek", 165),
  ("sak", 165),
  ("rav", 306),
  ("gui", 165),
  ("dis", 180),
  ("tsp", 422),
  ("plc", 165),
  ("fut", 180),
  ("lor", 312),
  ("mor", 153),
  ("sha", 313),
  ("eve", 187),
  ("soa", 259),
  ("con", 147),
  ("alr", 149),
  ("zen", 260),
  ("wwk", 151),
  ("roe", 255),
  ("som", 259),
  ("mbs", 161),
  ("nph", 180),
  ("isd", 277),
  ("dka", 162),
  ("avr", 252),
  ("rtr", 286),
  ("gtc", 257),
  ("dgm", 157),
  ("ths", 260),
  ("bng", 176),
  ("jou", 171),
  ("ktk", 282),
  ("frf", 189),
  ("dtk", 272),
  ("bfz", 288),
  ("ogw", 195),
  ("soi", 317),
  ("emn", 216),
  ("kld", 286),
  ("aer", 199),
  ("akh", 313),
  ("hou", 222),
  ("xln", 300),
  ("rix", 212),
  ("dom", 296),
  ("grn", 281),
  ("rna", 286),
  ("war", 294),
  ("eld", 417),
  ("thb", 371),
  ("iko", 402)
]

if not os.path.exists("MtGArtDownloads"):
    os.makedirs("MtGArtDownloads")
    
for s in sets:
    if s[0] != "con":
        if not os.path.exists("MtGArtDownloads" + os.sep + s[0]):
            os.makedirs("MtGArtDownloads" + os.sep + s[0])
    else:
        if not os.path.exists("conn"):
            os.makedirs("conn")
        
    for i in range(1, s[1]+1):
        num = format(str(i).zfill(3))
        source = "https://www.mtgpics.com/pics/art/" + s[0] + "/" + num + ".jpg"
        if s[0] != "con":
            target = "MtGArtDownloads" + os.sep + s[0] + os.sep + num +".jpg"
        else:
            target = "conn" + os.sep + num +".jpg"
            
        if not os.path.exists(target):
            urllib.urlretrieve (source, target)
        if os.stat(target).st_size == 76: #missing art file length
            os.remove(target)
            print "Missing art " + str(i) + " for set " + s[0]
        else:
            print source
