#https://en.wikibooks.org/wiki/Python_Programming

def room2 ():
    Answer = (input("vilken vapen tar du?\nA) pistolen\nB) pilbågen \nSkriv vilken du vill ha:")) 
    if(Answer == "höger"): 
        print("Du tar upp föremålet och forsätter framåt")
        väg1()
    else: 
        print("Du tar upp föremålet och forsätter framåt")  
        väg1()    


def bakom ():
    Answer = (input("snabbt! skjuter du eller slår du zombien?\nskjuter)\nslår):")) 
    if(Answer == "skjuter"): 
        print("zombien dog, du rör dig sakta framåt")
        
    else: 
        spelare_död()  

def spelare_död():
  print("du dog, zombiesen åt dig..")
  Answer = (input("Noob!\nSkriv 1)för att komma tillbaka där du dog\nskriv gg) för att avsvluta:"))
  if Answer == ("1"): 
    bakom()
  else: 
    print("Game over!")

def väg2 ():
    Answer = (input("du ser en stor dörr som är låst med en knapp brevid, men det kanske finns en annnan väg bakom slottet.\n A ) tryck på knappen\n B ) gå runt huset:"))
    if(Answer == "tryck på knappen"): 
        print("du trycker på knappen men inget händer")
        väg2()
    else: 
        print("du går runt huset och ser en zombie springa mot dig")  
        bakom()    


def väg1():
    Answer = input("du har två vägar framför dig, vilken tar du? \n A) Höger\n B) vänster: ")
    if (Answer == "höger"):
        print ("du kommer fram till slottet")
        väg2()
    else: 
      print("du ser en båt med nycklar i. du går tillbaka till vägen")
      väg1()

def room1():
    Answer = input("du har 2 vägar att välja, vilken tar du?\n A) höger\n B) vänster \nSkriv höger): eller vänster):") 
    if(Answer == "höger"):
        print("du hittar 2 föremål, en pistol och en pilbåge")
        room2()
    else:

        print("Dörren är låst..")
        room1()
        #print("du kommer fram till en dörr som är låst men kan bara öppna med hjälp av en knapp")


print("du har fått ett samtal att åka till ett slott som är inne i en skog, du kommer fram till skogen")
room1()

          