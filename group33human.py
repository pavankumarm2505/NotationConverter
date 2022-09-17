from uno import UnoPlayer, Color, CardType, Card


class Group33Human (UnoPlayer):

    def __init__(self, name):
        self.name = input("Player name:")
        UnoPlayer.__init__(self, self.name)
        

    def choose_card (self, state):
        
        #display the top card on the discard
        topcard= state.get_top_card()
        print(f"Top Card: {topcard}")
        
        #gets info about top card
        topcardcolor= Card.get_color(topcard)
        topcardtype= Card.get_type(topcard)
        topcardnum= Card.get_number(topcard)
        
       
        #condition for if the top card is wild
        if Card.is_wild(topcard):

            #getcalledcolor
            calledcolor= state.get_called_color()

            print(f"Called Color: {calledcolor.name}")

            #displays what card user has
            print("Your hand: ")
            for i in range(0,len(self.hand)):
                print(f"{i}. {self.hand[i]}")
            else:
                print(f"{i+1}. Draw a card and skip your turn")
                

            #prompts the user to pick an option
            while True:
                try:
                    inp= int(input("Which one will you pick? "))
                    break
                except Exception:
                    print("That's not an integer!")
            
            #repeats if invalid
            while inp not in range (0, len(self.hand)+1):
                while True:
                    try:
                        inp= int(input("Which one will you pick? "))
                        break
                    except Exception:
                        print("That's not an integer!")
                    
            #returns None if user draws a card
            if inp == len(self.hand):
                return None

            else:
                choosencard = self.hand[inp]
            
            if Card.is_wild(choosencard):
                return choosencard
            
            choosencardcolor= Card.get_color(choosencard)
  
            
            #repeat until color choosen is the same as called color
            while choosencardcolor != calledcolor:
                choosencard= None
                print("Illegal Move")
                while True:
                    try:
                        inp= int(input("Which one will you pick? "))
                        break
                    except Exception:
                        print("That's not an integer!")
            
                #repeat if invalid input
                while inp not in range (0, len(self.hand)+1):
                    while True:
                        try:
                            inp= int(input("Which one will you pick? "))
                            break
                        except Exception:
                            print("That's not an integer!")
                            
                
                if inp == len(self.hand):
                    choosencard= None
                    return choosencard
                
                else:
                    choosencard = self.hand[inp]
                 
                if Card.is_wild(choosencard):
                    return choosencard
            
                choosencardcolor= Card.get_color(choosencard)

                
            return choosencard
                
            
                
        #condition for if the top card is not wild        
        else:
            #prints what the Human has on his hands
            print("Your hand: ")
            for i in range(0,len(self.hand)):
                print(f"{i}. {self.hand[i]}")
            else:
                print(f"{i+1}.  Draw a card and skip your turn")

            #prompts the user to pick an option
            while True:
                try:
                    inp= int(input("Which one will you pick? "))
                    break
                except Exception:
                    print("That's not an integer!")

            #repeats if invalid
            while inp not in range (0, len(self.hand)+1):
                while True:
                    try:
                        inp= int(input("Which one will you pick? "))
                        break
                    except Exception:
                        print("That's not an integer!")
                
            #returns none if they pass
            if inp == len(self.hand):
                choosencard= None
                return choosencard
            
            #else selects the choosen option
            else:
                choosencard = self.hand[inp]
            #gets card info
            choosencardcolor= Card.get_color(choosencard)
            choosencardtype= Card.get_type(choosencard)
            choosencardnum= Card.get_number(choosencard)

            
            #print(choosencard, choosencardcolor, choosencardtype, choosencardnum)


            #returns card choosen if card is wild
            if choosencardtype == CardType.WILD or choosencardtype == CardType.WILD_DRAW_FOUR:
                choosencard = self.hand[inp]
                return choosencard
                
            
            # checks whether it is an illegal move
            while choosencardcolor != topcardcolor:
                if choosencardnum == topcardnum:
                        break
                if choosencardtype != CardType.NUMBER and topcardtype != CardType.NUMBER:
                    if choosencardtype == topcardtype:
                        break
                    

                choosencard = None
                print("Illegal Move!")
                while True:
                    try:
                        inp= int(input("Which one will you pick? "))
                        break
                    except Exception:
                        print("That's not an integer!")
        
                while inp not in range (0, len(self.hand)+1):
                    while True:
                        try:
                            inp= int(input("Which one will you pick? "))
                            break
                        except Exception:
                            print("That's not an integer!")
                   

                if inp == len(self.hand):
                    choosencard = None
                    return choosencard
                     
                else:
                    choosencard = self.hand[inp]
                    
                choosencardcolor= Card.get_color(choosencard)
                choosencardtype= Card.get_type(choosencard)
                choosencardnum= Card.get_number(choosencard)

                #print(choosencard, choosencardcolor, choosencardtype, choosencardnum)
                if choosencardtype == CardType.WILD or choosencardtype == CardType.WILD_DRAW_FOUR:
                    choosencard = self.hand[inp]
                    return choosencard
                 
                
            return choosencard
        
                 
                        
                                               
                
    def call_color(self,state):

        called_color=input("What color do you want to call?: ").upper()
        while called_color not in ['RED', 'YELLOW', 'GREEN', 'BLUE']:
            print("Pick a valid color")
            called_color=input("What color do you want to call?: ").upper()
        
        return Color[called_color]

 
            
        

            
        
        

    
                
        
        
        
