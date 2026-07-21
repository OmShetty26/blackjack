# Async Blackjack

A terminal-based Blackjack game built with Python to demonstrate Object-Oriented
programming and Asynchronous coroutines.

## How to Run
- Ensure you have python 3.7+ installed.
- Run the following command in your terminal: `python main.py`

## Core concepts demonstrated

### 1. Object-Oriented Programming (OOP)
The game logic is completely encapsulated into classes in `deck.py`:
* **Card:** Represents individual playing cards.
* **Deck:** Handles the generation, state, and shuffling of a standard 52-card deck.
* **Hand:** Manages the player's and dealer's current cards and calculates scores dynamically (including handling the special case of Aces).

### 2. Asynchronous Programming (Coroutines)
The main game loop runs asynchronously using the `asyncio` library to prevent thread-blocking:
* **Non-blocking I/O:** Standard `input()` blocks the main thread. This project uses `await asyncio.to_thread(input, ...)` to offload the I/O wait to a background thread, yielding control back to the event loop.
* **Simulated Delays:** The dealer's AI uses `await asyncio.sleep()` to simulate the physical drawing of cards without freezing the application thread.

### 3. Version Control (Git Flow)
This project was built using a professional Git workflow. Features (like the OOP classes and the async game loop) were developed on independent branches, tracked via GitHub Issues, and merged into `main` using Pull Requests.