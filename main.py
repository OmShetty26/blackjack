import asyncio
from deck import Deck, Hand

# --- ASYNC GAME LOOP ---
async def play_round():
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


# --- ENTRY POINT ---
if __name__ == "__main__":
    asyncio.run(play_round())

