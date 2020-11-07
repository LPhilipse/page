#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     generate code for the source editer of the Love Nikki Wikia
#
# Author:      laura
#
# Created:     01-11-2018
# Copyright:   (c) laura 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def page(insuit, nation, suitname, sort, suit, alternative, original, altsuit):
  cust = ""
  evofrom = ""
  evolves = ""
  fro = ""
  use = ""
  obcust = ""
  name = input("name:")
  caption = input("caption:")
  itemtype = input ("type:")
  if itemtype.lower() == "left hand ornament" or itemtype.lower() == "left bracelet":
    itemtype = "Accessory, Bracelet (Left)"
  if itemtype.lower() == "right hand ornament" or itemtype.lower() == "right bracelet":
    itemtype = "Accessory, Bracelet (Right)" 
  if itemtype.lower() == "hair ornament" or itemtype.lower() == "veil" or itemtype.lower() == "hairpin" or itemtype.lower() == "ears" or itemtype.lower() == "earrings" or itemtype.lower() == "necklace" or itemtype.lower() == "scarf" or itemtype.lower() == "bracelet (right)" or itemtype.lower() == "bracelet (left)" or itemtype.lower() == "gloves" or itemtype.lower() == "handheld (left)" or itemtype.lower() == "handheld (right)" or itemtype.lower() == "handheld (both)" or itemtype.lower() == "waist" or itemtype.lower() == "face" or itemtype.lower() == "brooch" or itemtype.lower() =="tattoo" or itemtype.lower() =="wings" or itemtype.lower() == "tail" or itemtype.lower() == "foreground" or itemtype.lower() == "background" or itemtype.lower() == "ground" or itemtype.lower() == "head ornament" or itemtype.lower() == "skin":
    itemtype = "Accessory, " + itemtype
  style = input("style, if multiple, just put spaces inbetween:")
  styl = ""
  if (style !=''):
    styles = style.split()
    styl = ''
    for i in styles:
      styl +="{{S|"+ i+ "}}"
  gh = False
  while not gh:
    attribute1 = input("attribute1:")
    if attribute1.lower() == "simple" or attribute1.lower() == "si":
      attribute1 = "Si"
      gh = True
    elif attribute1.lower() == "gorgeous" or attribute1.lower() == "g" or attribute1.lower()=="go":
      attribute1 = "G"
      gh = True
    elif attribute1.lower() == "elegant" or attribute1.lower()=="elegance" or attribute1.lower() == "e" or attribute1.lower()=="el":
      attribute1 = "E"
      gh = True
    elif attribute1.lower() == "lively" or attribute1.lower() == "l" or attribute1.lower()== "li":
      attribute1 = "L"
      gh = True
    elif attribute1.lower() == "mature" or attribute1.lower() == "m" or attribute1.lower() == "ma" :
      attribute1 = "M"
      gh = True
    elif attribute1.lower() == "cute" or attribute1.lower() == "cu":
      attribute1 = "Cu"
      gh = True
    elif attribute1.lower() == "sexy" or attribute1.lower() == "se":
      attribute1 = "Se"
      gh = True
    elif attribute1.lower() == "pure" or attribute1.lower() == "p" or attribute1.lower()=="pu":
      attribute1 = "P"
      gh = True
    elif attribute1.lower() == "warm" or attribute1.lower() == "w" or attribute1.lower()=="wa":
      attribute1 = "W"
      gh = True
    elif attribute1.lower() == "cool" or attribute1.lower() == "co":
      attribute1 = "Co"
      gh = True
    else:
      print("please fill in an valid attribute")
  gh = False
  while not gh:
    attribute2 = input("attribute2:")
    if attribute2.lower() == "simple" or attribute2.lower() == "si":
      attribute2 = "Si"
      gh = True
    elif attribute2.lower() == "gorgeous" or attribute2.lower() == "g" or attribute2.lower()=="go":
      attribute2 = "G"
      gh = True
    elif attribute2.lower() == "elegant" or attribute2.lower()=="elegance" or attribute2.lower() == "e" or attribute2.lower()=="el":
      attribute2 = "E"
      gh = True
    elif attribute2.lower() == "lively" or attribute2.lower() == "l" or attribute2.lower()== "li":
      attribute2 = "L"
      gh = True
    elif attribute2.lower() == "mature" or attribute2.lower() == "m" or attribute2.lower() == "ma" :
      attribute2 = "M"
      gh = True
    elif attribute2.lower() == "cute" or attribute2.lower() == "cu":
      attribute2 = "Cu"
      gh = True
    elif attribute2.lower() == "sexy" or attribute2.lower() == "se":
      attribute2 = "Se"
      gh = True
    elif attribute2.lower() == "pure" or attribute2.lower() == "p" or attribute2.lower()=="pu":
      attribute2 = "P"
      gh = True
    elif attribute2.lower() == "warm" or attribute2.lower() == "w" or attribute2.lower()=="wa":
      attribute2 = "W"
      gh = True
    elif attribute2.lower() == "cool" or attribute2.lower() == "co":
      attribute2 = "Co"
      gh = True
    else:
      print("please fill in an valid attribute")
  rarity = input("rarity:")
  color = input("color:")
  number = input ("wardrobe number:")

  sdafs = False
  while not sdafs:
    nrobt = input("how many obtainment methods?")
    try:
      int(nrobt)
      sdafs = True
    except ValueError:
      print("Please fill in a number")
  obt = ""
  intro = ""
  cat = []
  ev = "n"
  for i in range (0,int(nrobt)):
    obtain = input("enter an obtainment method, like event, log in, stage, store, pav, crafting, customization, recharge, evolution, reconstruction, monthly, achievement, styling gift box:")

    if(obtain.lower()== "event"):
      event = input("what event?")
      cat.append("Event")
      cat.append(event)
      if obt == "":
        obt = event + " event"
      else:
        obt = obt + "<br/>" + event + " event"
      ev = "y"
      intro= intro + "could be obtained from the [["+ event + "]] event"
      if int(nrobt) == 1:
        intro +="."
    elif(obtain.lower()== "log in"):
      intro= intro + "could be obtained from a [[Log-in Event]]."
      ev = "y"
      if obt == "":
        obt ="Log-in Event"
      else:
        obt = obt + "<br/>Log-in Event"
      cat.append("Log-in Event")
    elif (obtain.lower()=="monthly"):
      intro = intro + "can be obtained as a [[Monthly Sign-In]] reward."
      if obt == "":
        obt ="Monthly Sign-In"
      else:
        obt = obt + "<br/>Monthly Sign-In"
      cat.append("Monthly Sign-In")
    elif(obtain.lower()== "recharge"):
      intro = intro  +"could be obtained through a [[Recharge]]."
      ev = "y"
      if obt == "":
        obt ="Recharge"
      else:
        obt = obt + "<br/>Recharge"
      cat.append("Recharge")
    elif(obtain.lower()== "reconstruction"):
      intro = intro + "can be obtained through [[Reconstruction]]."
      if obt == "":
        obt ="Reconstruction"
      else:
        obt = obt + "<br/>Reconstruction"
      cat.append("Reconstruction")
    elif obtain.lower()=="styling gift box":
      intro += "can be obtained from a Styling Gift Box after completing [[" + suitname + "]]."
      if obt == "":
        obt ="Styling gift box"
      else:
        obt = obt + "<br/>Styling gift box"
      cat.append("Styling Gift Box")
    elif (obtain.lower()=="achievement"):
      ach = input("What achievement?")
      if obt == "":
        obt ="Achievement"
      else:
        obt = obt + "<br/>Achievement"
      cat.append("Achievement")
      if (intro == ""):
        intro = "can be obtained from the [[Achievements|Achievement]] "+ ach + "."
      else :
        intro = intro + " It can also be obtained from the [[Achievement]] " + ach + "."
    elif(obtain.lower()== "stage"):
      cat.append("Drop")

      safs = False
      while not safs:
        num = input("how many stages?")
        try:
          int(num)
          safs = True
        except ValueError:
          print("Please fill in a number")

      if (intro == ""):
        intro = "can be obtained from stage "
      else :
        intro = intro + " It can also be obtained from stage "
      for i in range (0,int(num)):
        stage = input("what stage?")
        le = False
        while not le:
          level = input("Maiden or Princess?")
          if (level.lower()=="m" or level.lower()=="maiden"):
            level = "Maiden"
            le = True
          elif (level.lower()=="p" or level.lower()=="princess"):
            level = "Princess"
            le = True
          else:
            print("please put in maiden or princess")
        if obt == "":
          obt = "Stage " + stage +" (" + level + ")"
        else:
          obt = obt + "<br/>Stage " + stage +" (" + level + ")"
        if str(level+ " Drop") not in cat:
          cat.append(str(level + " Drop"))
        intro = intro + "{{Stages|" + stage + "}} ("+ level +")"
        if(i<int(num)-1):
          intro = intro + ", "
      intro = intro + "."
      li = intro.rsplit(',', 1)
      new = " and"
      intro = new.join(li)
    elif (obtain.lower()=="evolution"):
      if obt == "":
        obt ="Evolution"
      else:
        obt = obt + "<br/>Evolution"
      cat.append("Evolution")
      if (intro == ""):
        intro = "can be obtained through [[Evolution]]."
      else:
        intro = intro + " It can also be obtained through [[Evolution]]."
    elif(obtain.lower()=="pav"):
      sdafs = False
      while not sdafs:
        pavs = input ("How many pavs?")
        try:
          int(pavs)
          sdafs = True
        except ValueError:
          print("Please fill in a number")
    
      if (intro == ""):
        intro = "can be obtained from "
      else :
        intro = intro + " It can also be obtained from "
      for i in range (0,int(pavs)):
        q = input("what pav")
        intro = intro + "the [[" + q + "]]"
        cat.append(q)
        if(i<int(pavs)-1):
          intro = intro + ", "
        if obt == "":
          obt = q
        else:
          obt = obt + "<br/>" + q
      intro = intro + "."
      li = intro.rsplit(',', 1)
      new = " and"
      intro = new.join(li)
    elif(obtain.lower()== "store"):
      sdafs = False
      while not sdafs:
        num = input ("how many stores?")
        try:
          int(num)
          sdafs = True
        except ValueError:
          print("Please fill in a number")
      for i in range (0,int(num)):
        store = input ("what store?")
        if obt == "":
          obt = store
        else:
          obt = obt + "<br/>" + store
        cat.append(store)
        value = input("how much does it cost?")
        currency = input("what currency?")
        if (intro == ""):
          intro = "can be bought in the [[" + store + "]] for " + value + " {{Currency|" + currency +"}}."
        elif ev == "y":
          intro += "and can now be bought in the [[" + store + "]] for " + value + " {{Currency|" + currency +"}}."
        else :
          intro= intro + " It can also be bought in the [[" + store + "]]  for " + value + " {{Currency|" + currency +"}}."
    elif(obtain.lower()=="crafting"):
      cat.append("Crafting")
      if (intro == ""):
        intro = "can be obtained through [[Recipe Crafting]]."
      elif ev == "y":
        intro += " and can now be obtained through [[Recipe Crafting]]."
      else :
        intro = intro + " It can also be obtained through [[Recipe Crafting]]."
      if obt == "":
        obt = "Crafting"
      else:
        obt = obt + "<br/>Crafting" 
    elif(obtain.lower()=="customization"):
      obcust = "y"
      cat.append("Customization")
      if obt == "":
        obt = "Customization"
      else:
        obt = obt + "<br/>Customization" 
      cus = input("customization of what item?")
      if (intro == ""):
        intro = "can be obtained through the [[Customization]] of [["+ cus + "]]."
      else :
        intro = intro + " It can also be obtained through the [[Customization]] of [["+ cus + "]]."

  appearance = input("appearance:")
  cust = input("customization y/n?")
  if (cust.lower()=="y"):
    sdafs = False
    while not sdafs:
      count = input("how many?")
      try:
        int(count)
        sdafs = True
      except ValueError:
        print("Please fill in a number")

    custom = ""
    for i in range (0, int(count)):
      x = input("name of customization:")
      y = input("amount of dye needed:")
      l = False
      while not l:
        z = input("what dye?")
        if (z.lower()=="red" or z.lower() == "garnet red" or z.lower()=="gr"):
          dye = "GR"
          l = True
        elif (z.lower()=="yellow" or z.lower()=="lemon yellow" or z.lower()=="ly"):
          dye = "LY"
          l = True
        elif (z.lower()=="orange" or z.lower()=="sunny orange" or z.lower()=="so"):
          dye = "SO"
          l = True
        elif (z.lower()=="green" or z.lower()=="lively green" or z.lower()=="lg"):
          dye = "LG"
          l = True
        elif (z.lower()=="blue" or z.lower()=="innocent blue" or z.lower()=="ib"):
          dye = "IB"
          l = True
        elif (z.lower()=="purple" or z.lower()=="elegant purple" or z.lower()=="ep"):
          dye = "EP"
          l = True
        elif (z.lower()=="pink" or z.lower()=="dreamy pink" or z.lower()=="dp"):
          dye = "DP"
          l = True
        elif (z.lower()=="white" or z.lower()=="pearl white" or z.lower()=="pw"):
          dye = "PW"
          l = True
        elif (z.lower()=="black" or z.lower()=="stardust black" or z.lower()=="sb"):
          dye = "SB"
          l = True
        elif (z.lower()=="other" or z.lower()=="other dye" or z.lower()=="od" or z.lower()=="rainbow"):
          dye = "OD"
          l = True
        elif (z.lower()=="polka" or z.lower()=="polka dots" or z.lower()=="dots" or z.lower()=="pd"):
          dye = "PD"
          l = True
        elif (z.lower()=="common" or z.lower()=="common plaid" or z.lower()=="plaid" or z.lower()=="cp"):
          dye = "CP"
          l = True
        elif (z.lower()=="stripes" or z.lower()=="fresh stripes" or z.lower()=="fs"):
          dye = "FS"
          l = True
        elif (z.lower()=="advanced" or z.lower()=="advanced pattern" or z.lower()=="ap"):
          dye = "AP"
          l = True
        else:
          print("please put in a valid dye or pattern")
      a = input("amount of material:")
      custom = custom + "\n* [[" + x + "]]: " + y + " {{Items|" + dye + "}}, " + a + " {{Items|M}}"
  evo = input("evolution y/n?")
  if(evo.lower() == "y"):
    evolution = '==[[Evolution]]=='
    evofrom = input("evolved from y/n?")
    if(evofrom.lower() == "y")   :
      evolution = evolution + "\n===Evolved from:===\n"
      count = input("how many?")
      h = input("how many needed?")
      g = input("name:")
      i = input ("how many gold?")
      evolution = evolution +"*" +  h + " [["+ g + "]], " + i + " {{Currency|G}}"
      if int(count) > 1:
        for q in range(0, int(count)-1):
          g = input("name:")
          evolution = evolution + "\n*[[" +g + "]]"
    evolves = input ("evolves into y/n?")
    if(evolves.lower() == "y") :
      evolution = evolution + "\n===Evolves into:===\n"
      count = input("how many?")
      j = input("name:")
      k = input ("how many needed?")
      l = input("how many gold needed?")
      evolution = evolution + "*[[" + j + "]] - " + k + " needed, " + l + " {{Currency|G}}"
      if(int(count)>1):
        for q in range (0, int(count)-1):
          j = input("name:")
          evolution = evolution + "\n*[[" + j + "]]"
  recon = input ("reconstruction y/n?")
  if (recon.lower() == "y"):
    rec = "==[[Reconstruction]]==\n===Reconstructed from:==="
    hr = input("how many hope rings?")
    re = input("how many rebirth earrings?")
    en = input("how many eternal necklaces?")
    m  = input("how much material?")
    if(int(hr)>0):
      rec = rec + "\n* " + hr + " {{Items|HR}}"
    if(int(re)>0):
      rec = rec + "\n* " + re + " {{Items|RE}}"
    if(int(en)>0):
      rec = rec + "\n* " + en + " {{Items|EN}}"
    if(int(m)>0):
      rec = rec + "\n* " + m + " {{Items|M}}"

  craf = input ("crafting y/n?")
  if (craf.lower()=="y"):
    crafting = "==[[Crafting]]=="
    fro = input("crafted from y/n?")
    if(fro.lower() == "y"):
      sdafs = False
      while not sdafs:
        count = input ("how many ingredients?")
        try:
          int(count)
          sdafs = True
        except ValueError:
          print("Please fill in a number")

      crafting = crafting + "\n===Crafted from:==="
      for i in range(0, int(count)) :
        b = input("amount needed:")
        c = input("name ingredient:")
        crafting = crafting + "\n* " + b + " [[" + c + "]]"
      rec = input("How to get the recipe? store, diary, bonus or mail?")
      crafting = crafting + "\n===Recipe:===\n"
      if (rec.lower() == 'store'):
        am = input("How many starcoins?")
        crafting = crafting + "The recipe can be bought in the [[Store of Starlight]] for " + am +" {{Currency|SC}}."
      elif (rec.lower() =="diary"):
        crafting = crafting + "The recipe can be claimed in the [[Time Diary]]."
      elif (rec.lower()=="bonus"):
        st = input("what stage?")
        d = input ("m or p?")
        crafting = crafting + "The recipe can be obtained from the [[Extra Stage Bonus]], after completing stage {{Stages|"+ st + "}}("
        if (d.lower() == "m"):
          crafting = crafting + "Maiden)."
        elif (d.lower() == "p"):
          crafting = crafting + "Princess)."
      elif (rec.lower() == "mail"):
        crafting = crafting + "The recipe could be claimed in the mailbox."

    use = input ("used to craft y/n?")
    if(use.lower() == "y"):
      sdafs = False
      while not sdafs:
        count = input ("how many?")
        try:
          int(nrobt)
          sdafs = True
        except ValueError:
          print("Please fill in a number")

      crafting = crafting + "\n===Used to craft:==="
      for i in range(0, int(count)) :
        d = input ("name item:")
        e = input("amount needed:")
        crafting = crafting + "\n*[[" + d + "]] - " + e + " needed"

  if(insuit == 'y'):
    items = ''
    for i in suit:
      if (i!= name or (original != "y" and alternative == "y")):
        if(items == ''):
          items = "[["+ i + "]]"
        else:
          items = items + ", [["+ i + "]]"
    items = items + "."
    li = items.rsplit(',', 1)
    new = " and"
    items = new.join(li)
    if (alternative == "y"):
      altitems = ''
      for i in altsuit:
        if (i!= name or original == "y"):
          if(altitems == ''):
            altitems = "[["+ i + "]]"
          else:
            altitems += ", [["+ i + "]]"
      altitems += "."
      li = altitems.rsplit(',', 1)
      new = " and"
      altitems = new.join(li)

  attributes = ''
  gr = False
  while not gr:
    att = input ("Simple or Gorgeous?")
    if att.lower() == "si" or att.lower() == "s" or att.lower()=="simple":
      att = "Simple"
      gr = True
    elif att.lower() == "go" or att.lower() == "g" or att.lower()=="gorgeous":
      att = "Gorgeous"
      gr = True
    else:
      print("please put in simple or gorgeous")
  grr = False
  while not grr:
    rating = input("rating of " + att + ":")
    if rating.lower()=="c" or rating.lower()=="b" or rating.lower()=="a" or rating.lower()=="s" or rating.lower()=="ss" or rating.lower()=="sss":
      rating = rating.upper()
      grr = True
    else:
      print("please put in a valid rating")
  attributes = attributes + "|" + att + "|" + rating

  gr = False
  while not gr:
    att = input ("Lively or Elegant?")
    if att.lower() == "li" or att.lower() == "l" or att.lower()=="lively":
      att = "Lively"
      gr = True
    elif att.lower() == "el" or att.lower() == "e" or att.lower()=="elegant" or att.lower()=="elegance":
      att = "Elegant"
      gr = True
    else:
      print("please put in lively or elegant")
  grr = False
  while not grr:
    rating = input("rating of " + att + ":")
    if rating.lower()=="c" or rating.lower()=="b" or rating.lower()=="a" or rating.lower()=="s" or rating.lower()=="ss" or rating.lower()=="sss":
      rating = rating.upper()
      grr = True
    else:
      print("please put in a valid rating")
  attributes = attributes + "|" + att + "|" + rating

  gr = False
  while not gr:
    att = input ("Cute or Mature?")
    if att.lower() == "cu" or att.lower() == "c" or att.lower()=="cute":
      att = "Cute"
      gr = True
    elif att.lower() == "ma" or att.lower() == "m" or att.lower()=="mature":
      att = "Mature"
      gr = True
    else:
      print("please put in cute or mature")
  grr = False
  while not grr:
    rating = input("rating of " + att + ":")
    if rating.lower()=="c" or rating.lower()=="b" or rating.lower()=="a" or rating.lower()=="s" or rating.lower()=="ss" or rating.lower()=="sss":
      rating = rating.upper()
      grr = True
    else:
      print("please put in a valid rating")
  attributes = attributes + "|" + att + "|" + rating

  gr = False
  while not gr:
    att = input ("Pure or Sexy?")
    if att.lower() == "pu" or att.lower() == "p" or att.lower()=="pure":
      att = "Pure"
      gr = True
    elif att.lower() == "se" or att.lower() == "s" or att.lower()=="sexy":
      att = "Sexy"
      gr = True
    else:
      print("please put in pure or sexy")
  grr = False
  while not grr:
    rating = input("rating of " + att + ":")
    if rating.lower()=="c" or rating.lower()=="b" or rating.lower()=="a" or rating.lower()=="s" or rating.lower()=="ss" or rating.lower()=="sss":
      rating = rating.upper()
      grr = True
    else:
      print("please put in a valid rating")
  attributes = attributes + "|" + att + "|" + rating

  gr = False
  while not gr:
    att = input ("Warm or Cool?")
    if att.lower() == "wa" or att.lower() == "w" or att.lower()=="warm":
      att = "Warm"
      gr = True
    elif att.lower() == "co" or att.lower() == "c" or att.lower()=="cool":
      att = "Cool"
      gr = True
    else:
      print("please put in warm or cool")
  grr = False
  while not grr:
    rating = input("rating of " + att + ":")
    if rating.lower()=="c" or rating.lower()=="b" or rating.lower()=="a" or rating.lower()=="s" or rating.lower()=="ss" or rating.lower()=="sss":
      rating = rating.upper()
      grr = True
    else:
      print("please put in a valid rating")
  attributes = attributes + "|" + att + "|" + rating

  print("{{Clothing\n|image = File:" + name + ".png\n|imagewidth = 180\n|caption ="
  + caption + "\n|type = "+itemtype + "\n|style = " + styl +
  "\n|attributes = {{A|"+attribute1 + "}} {{A|" + attribute2 +"}}\n|rarity = {{H|"+rarity+ "}}\n|color = "
  + color + "\n|wardrobe nr = "+ number + "\n|how to obtain = "+ obt +"\n}}")
  print( "'''"+ name + "''' "+ intro)

  print("==Appearance==\n"+ appearance)
  if (cust == "y"):
    print("==[[Customization]]==" + custom)
  if (evo=="y"):
    print(evolution)
  if(recon=="y"):
    print (rec)
  if(craf == "y"):
    print (crafting)
  if(insuit == "y") :
    if sort == "g":
      print("==[[Gallery Suits|Gallery Suit]]==")
      pre = "[[" + nation + "]]"
    if sort == "h":
      print ("==[[Hidden Suits|Hidden Suit]]==")
      pre = "hidden"
    if sort == "s":
      print ("==[[Story Suit]]==")
      pre = "story"
    if original == "y" or alternative == "n":
      print ("'''"+ name + "''' is part of the "+ pre + " suit [[" + suitname+ "]].\n\nThe other parts of this suit are " + items)
      if (alternative == "y"):
        print("\nThere is an alternative version of the suit. It contains " + altitems )
    else:
      print ("'''"+ name + "''' is part of an alternative version of the " + pre + " suit [[" + suitname+ "]].\n\nThe other parts of this suit are " + altitems)
      print("\nThe original version of this suit contains " + items )
  print("==Attributes==\n{{Attributes" + attributes + "}}")

  print("[[Category:Wardrobe Item]]")
  n = itemtype.split(", ")
  for i in n:
    i = i.lower()
    if i == "hair":
      print("[[Category:Hair]]")
    elif i == "dress":
      print("[[Category:Dresses]]")
    elif i == "coat":
      print("[[Category:Coat]]")
    elif i == "top":
      print("[[Category:Tops]]")
    elif i == "bottom":
      print("[[Category:Bottoms]]")
    elif i == "hosiery":
      print("[[Category:Hosiery]]")
    elif i == "hosiery (leglet)" or i == "leglet":
      print("[[Category:Hosiery (Leglet)]]")
    elif i == "shoes":
      print("[[Category:Shoes]]")
    elif i == "accessory":
      print("[[Category:Accessories]]")
    elif i == "hair ornament" or i == "veil" or i == "hairpin" or i == "ear":
      print("[[Category:Headwear]]")
      if(i=="hair ornament"):
        print("[[Category:Hair Ornaments]]")
      elif (i == "veil"):
        print("[[Category:Veil]]")
      elif (i == "hairpin"):
        print("[[Category:Hairpin]]")
      elif i == "ear":
        print("[[Category:Ears]]")
    elif i == "earrings":
      print("[[Category:Earrings]]")
    elif i == "necklace":
      print("[[Category:Necklace]]")
    elif i == "scarf":
      print("[[Category:Scarf]]")
    elif i == "bracelet (left)" or i == "bracelet (right)" or i == "gloves":
      print("[[Category:Bracelets]]")
      if i == "bracelet (left)":
        print("[[Category:Bracelets (Left)]]")
      elif i == "bracelet (right)":
        print("[[Category:Bracelets (Right)]]")
      elif i == "gloves":
        print("[[Category:Gloves]]")
    elif i == "handheld (left)" or i == "handheld (right)" or i == "handheld (both)":
      print("[[Category:Handheld]]")
      if i == "handheld (left)":
        print("[[Category:Handheld (Left)]]")
      elif i == "handheld (right)":
        print("[[Category:Handheld (Right)]]")
      elif i == "handheld (both)":
        print("[[Category:Handheld (Both)]]")
    elif i == "waist":
      print("[[Category:Waist]]")
    elif i == "face":
      print("[[Category:Special]]")
      print("[[Category:Face]]")
    elif i == "brooch":
      print("[[Category:Special]]")
      print("[[Category:Brooch]]")
    elif i == "tattoo":
      print("[[Category:Special]]")
      print("[[Category:Tattoo]]")
    elif i == "wings":
      print("[[Category:Special]]")
      print("[[Category:Wings]]")
    elif i == "tail":
      print("[[Category:Special]]")
      print("[[Category:Tail]]")
    elif i == "foreground":
      print("[[Category:Special]]")
      print("[[Category:Foreground]]")
    elif i == "background":
      print("[[Category:Special]]")
      print("[[Category:Background]]")
    elif i == "head ornament":
      print("[[Category:Special]]")
      print("[[Category:Head Ornaments]]")
    elif i == "ground":
      print("[[Category:Special]]")
      print("[[Category:Ground]]")

    elif i == "skin":
      print("[[Category:Skin]]")

    elif i == "makeup":
      print("[[Category:Makeup]]")

  for i in attribute1, attribute2:
    if (i == "Si"):
      print("[[Category:Simple]]")
    elif (i=="G"):
      print("[[Category:Gorgeous]]")
    elif (i=="L"):
      print("[[Category:Lively]]")
    elif (i=="E"):
      print("[[Category:Elegant]]")
    elif (i=="Cu"):
      print("[[Category:Cute]]")
    elif (i=="M"):
      print("[[Category:Mature]]")
    elif (i=="P"):
      print("[[Category:Pure]]")
    elif (i=="Se"):
      print("[[Category:Sexy]]")
    elif (i=="W"):
      print("[[Category:Warm]]")
    elif (i=="Co"):
      print("[[Category:Cool]]")
  if (style != ''):
    styles = style.split()
    for i in styles:
      if i == "Sun":
        print("[[Category:Sun Care]]")
      elif i =="Dan":
        print("[[Category:Dancer]]")
      elif i == "Flo":
        print("[[Category:Floral]]")
      elif i == "Win":
        print("[[Category:Winter]]")
      elif i == "Bri":
        print("[[Category:Britain]]")
      elif i == "Swi":
        print("[[Category:Swimsuit]]")
      elif i == "Sho":
        print("[[Category:Shower]]")
      elif i == "Kim":
        print("[[Category:Kimono]]")
      elif i == "Paj":
        print("[[Category:Pajamas]]")
      elif i == "Wed":
        print("[[Category:Wedding]]")
      elif i == "Arm":
        print("[[Category:Army]]")
      elif i =="Off":
        print("[[Category:Office]]")
      elif i == "Apr":
        print("[[Category:Apron]]")
      elif i == "Che":
        print("[[Category:Cheongsam]]")
      elif i == "Mai":
        print("[[Category:Maiden]]")
      elif i == "Eve":
        print("[[Category:Evening Gown]]")
      elif i == "Nav":
        print("[[Category:Navy]]")
      elif i == "Tra":
        print("[[Category:Traditional]]")
      elif i == "Bun":
        print("[[Category:Bunny]]")
      elif i == "Lad":
        print("[[Category:Lady]]")
      elif i == "Lol":
        print("[[Category:Lolita]]")
      elif i == "Got":
        print("[[Category:Gothic]]")
      elif i == "Spo":
        print("[[Category:Sports]]")
      elif i == "Har":
        print("[[Category:Harajuku]]")
      elif i == "Pre":
        print("[[Category:Preppy]]")
      elif i == "Uni":
        print("[[Category:Unisex]]")
      elif i == "Fut":
        print("[[Category:Future]]")
      elif i == "Fai":
        print("[[Category:Fairy]]")
      elif i == "Roc":
        print("[[Category:Rock]]")
      elif i == "Den":
        print("[[Category:Denim]]")
      elif i == "Pet":
        print("[[Category:Pet]]")
      elif i == "God":
        print("[[Category:Goddess]]")
      elif i == "POP":
        print("[[Category:POP]]")
      elif i == "Hom":
        print("[[Category:Homewear]]")
      elif i == "Chi":
        print("[[Category:Chinese Classical]]")
      elif i == "Hin":
        print("[[Category:Hindu]]")
      elif i== "Rep":
        print("[[Category:Republic of China]]")
      elif i == "Eur":
        print("[[Category:European]]")
      elif i == "Swo":
        print("[[Category:Swordsman]]")
      elif i == "Rai":
        print("[[Category:Rain]]")
      elif i == "Mod":
        print("[[Category:Modern China]]")
      elif i =="Dry":
        print("[[Category:Dryad]]")
      elif i == "Boh":
        print("[[Category:Bohemia]]")
      elif i == "Par":
        print("[[Category:Paramedics]]")
  if (rarity == "G"):
    print ("[[Category:5 Gold Heart]]")
  elif (rarity == "G2"):
    print ("[[Category:2 Gold Heart]]")
    print ("[[Category:Animated]]")
  elif (rarity == "G3"):
    print ("[[Category:3 Gold Heart]]")
    print ("[[Category:Animated]]")
  elif (rarity == "G4"):
    print ("[[Category:4 Gold Heart]]")
    print ("[[Category:Animated]]")
  elif (rarity == "G6"):
    print ("[[Category:6 Gold Heart]]")
    print ("[[Category:Animated]]")
  else:
    print("[[Category:"+ rarity + " Heart]]")
  if(obcust == "" and cust == "y"):
    print("[[Category:Customizable]]")
  if(evolves == "y"):
    print ("[[Category:Evolvable]]")
  if(use == "y"):
    print ("[[Category:Ingredient]]")
  for i in cat:
    print("[[Category:"+ i + "]]")
  if (insuit == "y"):
    print ("[[Category:" + suitname + "]]")