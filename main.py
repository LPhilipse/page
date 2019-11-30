

#change the values of these variables
insuit = 'n'                     # is the item in a suit y/n?
nation ="Lilith"                  # suit nation
suitname = "Red Hood's Adventure"          # suit name
sort = "g"         #g for gallery, h for hidden, s for story
suit = ["Red Hat-Epic", "Red Vest-Epic", "Red Apron-Epic", "Fairy Tale-Epic", "Leather Shoes-Epic", "Red Cloak-Epic", "Fantasy Shotgun", "Red Hat's Basket"]      # put the other (or all, the current one will be filtered out) items of the suit here
alternative = "n"             #is there an alternative version y/n? You dont have to change it to n if insuit already is n
original = "y"              #is the item part of the original version
altsuit = ["Rapid Short Hair", "Alumni Ace (Dress)|Alumni Ace", "King's Honor",  "Wild Warrior", "Nikki Rugby", "Invincible"]                # list the alternative suit items

def page():
  cust = ""
  evofrom = ""
  evolves = ""
  fro = ""
  use = ""
  name = input("name")
  caption = input("caption")
  itemtype = input ("type")
  style = input("style, if multiple, just put spaces inbetween")
  styl = ""
  if (style !=''):
    styles = style.split()
    styl = ''
    for i in styles:
      styl +="{{S|"+ i+ "}}"
  attribute1 = input("attribute1")
  attribute2 = input("attribute2")
  rarity = input("rarity")
  color = input("color")
  number = input ("wardrobe number")
  obt = input ("how to obtain (template)")
  intro = ""
  cat = []
  ev = "n"
  sdafs = False
  while not sdafs:
    nrobt = input("how many obtainment methods?")
    try:
      int(nrobt)
      sdafs = True
    except ValueError:
      print("Please fill in a number")

  intro = ""
  cat = []
  ev = "n"
  for i in range (0,int(nrobt)):
    obtain = input("enter an obtainment method, like event, log in, stage, store, pav, crafting, customization, recharge, evolution, reconstruction, monthly, achievement, styling gift box")

    if(obtain.lower()== "event"):
      event = input("what event?")
      cat.append("Event")
      cat.append(event)
      ev = "y"
      intro= intro + "could be obtained from the [["+ event + "]] event"
      if int(nrobt) == 1:
        intro +="."
    elif(obtain.lower()== "log in"):
      intro= intro + "could be obtained from a [[Log-in Event]]."
      ev = "y"
      cat.append("Log-in Event")
    elif (obtain.lower()=="monthly"):
      intro = intro + "can be obtained as a [[Monthly Sign-In]] reward."
      cat.append("Monthly Sign-In")
    elif(obtain.lower()== "recharge"):
      intro = intro  +"could be obtained through a [[Recharge]]."
      ev = "y"
      cat.append("Recharge")
    elif(obtain.lower()== "reconstruction"):
      intro = intro + "can be obtained through [[Reconstruction]]."
      cat.append("Reconstruction")
    elif obtain.lower()=="styling gift box":
      intro += "can be obtained from a Styling Gift Box after completing [[" + suitname + "]]."
      cat.append("Styling Gift Box")
    elif (obtain.lower()=="achievement"):
      ach = input("What achievement?")
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
        level = input("Maiden or Princess?")
        if str(level+ " Drop") not in cat:
          cat.append(str(level + " Drop"))
        intro = intro + "{{Stages|" + stage + "}}("+ level +")"
        if(i<int(num)-1):
          intro = intro + ", "
      intro = intro + "."
      li = intro.rsplit(',', 1)
      new = " and"
      intro = new.join(li)
    elif (obtain.lower()=="evolution"):
        cat.append("Evolution")
        if (intro == ""):
          intro = "can be obtained through [[Evolution]]."
        else :
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
    elif(obtain.lower()=="customization"):
      cat.append("Customization")
      cus = input("customization of what item?")
      if (intro == ""):
        intro = "can be obtained through the [[Customization]] of [["+ cus + "]]."
      else :
        intro = intro + " It can also be obtained through the [[Customization]] of [["+ cus + "]]."

  appearance = input("appearance")
  cust = input("customization y/n?")
  if (cust=="y"):
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
      x = input("name of customization")
      y = input("amount of dye needed")
      z = input("code of dye")
      a = input("amount of material")
      custom = custom + "\n* [[" + x + "]]: " + y + " {{Items|" + z + "}}, " + a + " {{Items|M}}"
  evo = input ("evolution y/n?")
  if(evo == "y"):
    evolution = '==[[Evolution]]=='
    evofrom = input("evolved from y/n?")
    if(evofrom == "y")   :
      evolution = evolution + "\n===Evolved from:===\n"
      count = input("how many?")
      h = input("how many needed?")
      g = input("name")
      i = input ("how many gold")
      evolution = evolution +"*" +  h + " [["+ g + "]], " + i + " {{Currency|G}}"
      if int(count) > 1:
        for q in range(0, int(count)-1):
          g = input("name")
          evolution = evolution + "\n*[[" +g + "]]"
    evolves = input ("evolves into y/n?")
    if(evolves == "y") :
      evolution = evolution + "\n===Evolves into:===\n"
      count = input("how many?")
      j = input("name")
      k = input ("how many needed")
      l = input("how many gold needed")
      evolution = evolution + "*[[" + j + "]] - " + k + " needed, " + l + " {{Currency|G}}"
      if(int(count)>1):
        for q in range (0, int(count)-1):
          j = input("name")
          evolution = evolution + "\n*[[" + j + "]]"
  recon = input ("reconstruction y/n?")
  if (recon == "y"):
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
  if (craf=="y"):
    crafting = "==[[Crafting]]=="
    fro = input("crafted from y/n?")
    if(fro == "y"):
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
        b = input("amount needed")
        c = input("name ingredient")
        crafting = crafting + "\n* " + b + " [[" + c + "]]"
      rec = input("How to get the recipe? store, diary, bonus or mail?")
      crafting = crafting + "\n===Recipe:===\n"
      if (rec == 'store'):
        am = input("How many starcoins?")
        crafting = crafting + "The recipe can be bought in the [[Store of Starlight]] for " + am +" {{Currency|SC}}."
      elif (rec =="diary"):
        crafting = crafting + "The recipe can be claimed in the [[Time Diary]]."
      elif (rec=="bonus"):
        st = input("what stage?")
        d = input ("m or p?")
        crafting = crafting + "The recipe can be obtained from the [[Extra Stage Bonus]], after completing stage {{Stages|"+ st + "}}("
        if (d == "m"):
          crafting = crafting + "Maiden)."
        elif (d == "p"):
          crafting = crafting + "Princess)."
      elif (rec == "mail"):
        crafting = crafting + "The recipe could be claimed in the mailbox."

    use = input ("used to craft y/n?")
    if(use == "y"):
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
        d = input ("name item")
        e = input("amount needed")
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
  for i in range (0,5):
    att = input ("Attribute")
    rating = input("rating of " + att)
    attributes = attributes + "|" + att + "|" + rating


  print("{{Clothing\n|image = File:" + name + ".png\n|imagewidth = 180\n|caption ="
  + caption + "\n|type = "+itemtype + "\n|style = " + styl +
  "\n|attributes = {{A|"+attribute1 + "}} {{A|" + attribute2 +"}}\n|rarity = {{H|"+rarity+ "}}\n|color = "
  + color + "\n|wardrobe # = "+ number + "\n|how to obtain = "+ obt +"\n}}")
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
      print("\nThe original version of the suit contains " + items )
  print("==Attributes==\n{{Attributes" + attributes + "}}")

  print("[[Category:Wardrobe Item]]")
  n = itemtype.split(", ")
  for i in n:
    if i == "Hair":
      print("[[Category:Hair]]")
    elif i == "Dress":
      print("[[Category:Dresses]]")
    elif i == "Coat":
      print("[[Category:Coat]]")
    elif i == "Top":
      print("[[Category:Tops]]")
    elif i == "Bottom":
      print("[[Category:Bottoms]]")
    elif i == "Hosiery":
      print("[[Category:Hosiery]]")
    elif i == "Hosiery (Leglet)" or i == "Leglet":
      print("[[Category:Hosiery (Leglet)]]")
    elif i == "Shoes":
      print("[[Category:Shoes]]")
    elif i == "Accessory":
      print("[[Category:Accessories]]")
    elif i == "Hair Ornament" or i == "Veil" or i == "Hairpin" or i == "Ear":
      print("[[Category:Headwear]]")
      if(i=="Hair Ornament"):
        print("[[Category:Hair Ornaments]]")
      elif (i == "Veil"):
        print("[[Category:Veil]]")
      elif (i == "Hairpin"):
        print("[[Category:Hairpin]]")
      elif i == "Ear":
        print("[[Category:Ears]]")
    elif i == "Earrings":
      print("[[Category:Earrings]]")
    elif i == "Necklace":
      print("[[Category:Necklace]]")
    elif i == "Scarf":
      print("[[Category:Scarf]]")
    elif i == "Bracelet (Left)" or i == "Bracelet (Right)" or i == "Gloves":
      print("[[Category:Bracelets]]")
      if i == "Bracelet (Left)":
        print("[[Category:Bracelets (Left)]]")
      elif i == "Bracelet (Right)":
        print("[[Category:Bracelets (Right)]]")
      elif i == "Gloves":
        print("[[Category:Gloves]]")
    elif i == "Handheld (Left)" or i == "Handheld (Right)" or i == "Handheld (Both)":
      print("[[Category:Handheld]]")
      if i == "Handheld (Left)":
        print("[[Category:Handheld (Left)]]")
      elif i == "Handheld (Right)":
        print("[[Category:Handheld (Right)]]")
      elif i == "Handheld (Both)":
        print("[[Category:Handheld (Both)]]")
    elif i == "Waist":
      print("[[Category:Waist]]")
    elif i == "Face":
      print("[[Category:Special]]")
      print("[[Category:Face]]")
    elif i == "Brooch":
      print("[[Category:Special]]")
      print("[[Category:Brooch]]")
    elif i == "Tattoo":
      print("[[Category:Special]]")
      print("[[Category:Tattoo]]")
    elif i == "Wings":
      print("[[Category:Special]]")
      print("[[Category:Wings]]")
    elif i == "Tail":
      print("[[Category:Special]]")
      print("[[Category:Tail]]")
    elif i == "Foreground":
      print("[[Category:Special]]")
      print("[[Category:Foreground]]")
    elif i == "Background":
      print("[[Category:Special]]")
      print("[[Category:Background]]")
    elif i == "Head Ornament":
      print("[[Category:Special]]")
      print("[[Category:Head Ornaments]]")
    elif i == "Ground":
      print("[[Category:Special]]")
      print("[[Category:Ground]]")

    elif i == "Skin":
      print("[[Category:Skin]]")

    elif i == "Makeup":
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
  if(cust == "y"):
    print("[[Category:Customizable]]")
  if(evolves == "y"):
    print ("[[Category:Evolvable]]")
  if(use == "y"):
    print ("[[Category:Ingredient]]")
  for i in cat:
    print("[[Category:"+ i + "]]")
  if (insuit == "y"):
    print ("[[Category:" + suitname + "]]")

page()