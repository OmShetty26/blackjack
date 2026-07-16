import asyncio
from deck import Deck, Hand

# --- ASYNC GAME LOOP ---
async def play_round():
    """
    Simulates a single round of Blackjack between the Dealer and Player
    """
    print("Welcome to Blackjack!\n")
    
    playing_deck = Deck()
    dealer_hand = Hand()
    player_hand = Hand()

    playing_deck.shuffle()
    dealer_hand.add_card(playing_deck.draw())
    dealer_hand.add_card(playing_deck.draw())
    player_hand.add_card(playing_deck.draw())
    player_hand.add_card(playing_deck.draw())

    print("--- DEALER'S HAND ---")
    print(dealer_hand.cards[0])
    print("[Hidden Card]")

    print("\n--- YOUR HAND ---")
    for card in player_hand.cards:
        print(card)
    print(f"Current total: {player_hand.calculate_value()}")

    while True:
        choice = await asyncio.to_thread(input, "\nWould you like to Hit or Stand? ")
        
        if choice.lower() == "hit":
            new_draw = playing_deck.draw()
            player_hand.add_card(new_draw)
            print(f"You drew {new_draw}.")
            new_total = player_hand.calculate_value()
            
            if new_total > 21:
                print(f"You busted! Your total was {new_total}. Better luck next time!")
                break
            print(f"Current total: {new_total}")

        elif choice.lower() == "stand":
            print("Player has decided to stand.")
            break
        
        else:
            print("Invalid choice! Please type Hit or Stand.")


# --- ENTRY POINT ---
if __name__ == "__main__":
    asyncio.run(play_round())


