from uno import UnoPlayer, Color, CardType, Card

class Group33AI (UnoPlayer):

    def __init__ (self, name):
        self.name= name
        UnoPlayer.__init__(self, self.name)

    def choose_card (self, state):
        
        #display the top card on the discard
        topcard= state.get_top_card()
        
        
        #gets info about top card
        topcardcolor= Card.get_color(topcard)
        topcardtype= Card.get_type(topcard)
        topcardnum= Card.get_number(topcard)

        #infoaboutoponent
        
        opponentsize= int(state.get_hand_sizes()[0])
        

        #action to take if the top card is wild
        if Card.is_wild(topcard):

            #getcalledcolor
            calledcolor= state.get_called_color()
            

            #displays what card user has
            for cardz in self.hand:
                if Card.get_color(cardz) == calledcolor:
                    return cardz
            for cardz in self.hand:
                if Card.is_wild(cardz):
                    return cardz
            return None
             
                
        #action to take if top card is not wild       
        else:
            #plays the exact same card if its available
            if topcard in self.hand:
                return self.hand.index(topcard)

            #plays wild and draw two if opponent is close to winning
       
            for cardz in self.hand:
                if opponentsize <= 4:
                    if Card.get_type(cardz) == CardType.WILD_DRAW_FOUR:
                        #print('Danger so played', cardz)
                        return cardz
                    
            for cardz in self.hand:
                if opponentsize <= 4:        
                    if Card.get_type(cardz)== CardType.DRAW_TWO and ((Card.get_type(cardz)== topcardtype) or (Card.get_color(cardz) == topcardcolor)):
                        #print('Danger so played', cardz)
                        return cardz

            #play the same number if available   
            for cardz in self.hand:
                
                if topcardtype == CardType.NUMBER:
                    if Card.get_number(cardz) == topcardnum:
                        #print(cardz)
                        return cardz

                    
            #play the same color if available       
            for cardz in self.hand:
                
                if Card.get_color(cardz) == topcardcolor:
                    for cardz in self.hand:
                        if Card.get_color(cardz) == topcardcolor and (Card.get_type(cardz)==CardType.SKIP or Card.get_type(cardz)==CardType.REVERSE or Card.get_type(cardz)==CardType.DRAW_TWO):
                            #print(cardz)
                            return cardz
                    else:
                        for cardz in self.hand:
                            if Card.get_color(cardz) == topcardcolor:
                                #print(cardz)
                                return cardz


            #plays special card top card is also special   
            for cardz in self.hand:
                
                if topcardtype == CardType.SKIP or topcardtype == CardType.REVERSE or topcardtype == CardType.DRAW_TWO:
                    if Card.get_type(cardz) == topcardtype:
                        #print(cardz)
                        return cardz

            
            
                                                  
            #plays WILD card as last resort       
            for cardz in self.hand:
                
                if Card.get_type(cardz) == CardType.WILD or (Card.get_type(cardz) == CardType.WILD_DRAW_FOUR):
                    #print(cardz)
                    return cardz

            #if nothing is there, skip and draw
            cardz= None
            #print('skipped and drew')
            return cardz
                    
            
                
    def call_color(self,state):
        colorcounts=[]
        
        for cardz in self.hand:
            colorz=Card.get_color(cardz)
            if colorz == Color.NONE:
                continue
            colorcounts.append(colorz)
            
        if len(colorcounts)>=1:
            maximum=max(colorcounts, key= colorcounts.count)
            if maximum== Color.NONE:
                for cardz in self.hand:
                    color= Card.get_color(cardz).name
                    if color in ['RED', 'GREEN', 'YELLOW', 'BLUE']:
                        return Color[color]
            else:
                return maximum
        else:
            for cardz in self.hand:
                color= Card.get_color(cardz).name
                if color in ['RED', 'GREEN', 'YELLOW', 'BLUE']:
                    return Color[color]
                
    


            
        

            
        
        

    
                
        
        
        
