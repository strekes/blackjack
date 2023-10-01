#Blackjack
#Card values
#--randomizer
#--hit/hold
#player info
#house
#bank 
#-- default bank - $100?
#-- add to bank?
#-- always show bank? or keyword used to show bank total?
#-- buy in
#-- double down
#-- split
#current hand
#pot

'''
steps
prompt user for name
display player name and bank
add to bank (?) (and display)
inform user of buy in and ask if they want to play
give player card
    -- remove from card remainder and total card count (with each card given, whether house or player)
if player total below 21, ask if they want to hit or (stay pass?)
on second card, ask if they want to double down, they get dealt one more card
if first two cards match, ask if they want to split
if player total == 21, they win
if player total > 21, they bust
once player stops receiving more cards (assuming not 21 or busted), house plays
-- need house rules for when computer hits (I think its anything under 16?)
whomever has higher count (without bust) wins pot
ask if player wants to play again
'''

#cards
cards_remainder = {'A':4, 'K':4, 'Q':4, 'J':4, '10':4, '9':4, '8':4, '7':4, '6':4, '5':4, '3':4, '2':4}
card_count = 52
cards_points = 