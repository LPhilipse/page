#for instructions on how to use this see https://lovenikki.fandom.com/wiki/User_blog:Lwgph/Updated_version_of_my_page_script!

#change the values of these variables to add suit information 
insuit = 'n'                             # is the item in a suit y/n?
sort = "g"                      #g for gallery, h for hidden, s for story
nation ="Lilith"                          # suit nation
suitname = "Red Hood's Adventure"          # suit name
suit = ["Red Hat-Epic", "Red Vest-Epic", "Red Apron-Epic", "Fairy Tale-Epic", "Leather Shoes-Epic", "Red Cloak-Epic", "Fantasy Shotgun", "Red Hat's Basket"]      # put the other (or all, the current one will be filtered out) items of the suit here
alternative = "n"             #is there an alternative version y/n? You dont have to change it to n if insuit already is n
original = "y"              #is the item part of the original version
altsuit = ["Rapid Short Hair", "Alumni Ace (Dress)|Alumni Ace", "King's Honor",  "Wild Warrior", "Nikki Rugby", "Invincible"]                # list the alternative suit items

from page import page
page(insuit, nation, suitname, sort, suit, alternative, original, altsuit)