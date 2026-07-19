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

    # Initial game setup
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
        # Offloads blocking input() function to a separate thread.
        # Yields control back to event loop while waiting for player input.
        choice = await asyncio.to_thread(input, "\nWould you like to Hit or Stand? ")
        
        if choice.lower() == "hit":
            new_draw = playing_deck.draw()
            player_hand.add_card(new_draw)
            print(f"You drew {new_draw}.")
            new_total = player_hand.calculate_value()
            
            if new_total > 21:
                print(f"You busted! Your total was {new_total}. Better luck next time!")
                break # Ends game loop
            print(f"Your total: {new_total}")

        elif choice.lower() == "stand":
            print("\n--- DEALER'S TURN ---")

            # Hidden Card Reveal
            print(f"Dealer reveals their hidden card: {dealer_hand.cards[1]}")
            dealer_score = dealer_hand.calculate_value()
            print(f"Dealer's starting total: {dealer_score}")

            # Dealer AI Loop
            while (dealer_score < 17):
                # Pauses coroutine without blocking the main thread
                # Simulates dealer thinking and drawing a card
                await asyncio.sleep(1.5)
                dealer_draw = playing_deck.draw()
                dealer_hand.add_card(dealer_draw)
                print(f"The Dealer drew {dealer_draw}.")
                dealer_score = dealer_hand.calculate_value()

            # Game resolution
            if (dealer_score > 21):
                print(f"The Dealer busted with {dealer_score}! Congrats, You Win!")
            else:
                print(f"\nFinal Dealer total: {dealer_score}")
                player_score = player_hand.calculate_value()
                print(f"Final Player total: {player_score}")
                if (player_score == dealer_score):
                    print("It's a push (tie).")
                elif (player_score > dealer_score):
                    print("Congrats! You Win!")
                else:
                    print("House Wins! Better luck next time.")
            break # Ends game loop
        
        else:
            print("Invalid choice! Please type Hit or Stand.")


# --- ENTRY POINT ---
if __name__ == "__main__":
    asyncio.run(play_round())


