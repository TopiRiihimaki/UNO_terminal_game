import random
from colorama import Fore, Style, init
init()

# -------- CARD --------
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        if self.color == "Red":
            return Fore.RED + f"{self.color} {self.value}" + Style.RESET_ALL
        elif self.color == "Blue":
            return Fore.BLUE + f"{self.color} {self.value}" + Style.RESET_ALL
        elif self.color == "Green":
            return Fore.GREEN + f"{self.color} {self.value}" + Style.RESET_ALL
        elif self.color == "Yellow":
            return Fore.YELLOW + f"{self.color} {self.value}" + Style.RESET_ALL
        else:
            return f"{self.color} {self.value}"


# -------- DECK --------
class Deck:
    def __init__(self):
        self.cards = []
        colors = ["Red", "Blue", "Green", "Yellow"]
        values = list(range(10))

        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


# -------- PLAYER --------
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def show_hand(self):
        print("\nYour hand:")
        for i, card in enumerate(self.hand):
            print(f"{i}: {card}")


# -------- GAME LOGIC --------
def can_play(card, top_card):
    return card.color == top_card.color or card.value == top_card.value


# -------- MAIN GAME --------
def main():
    deck = Deck()
    deck.shuffle()

    player = Player("You")

    # Draw starting hand
    for _ in range(5):
        player.draw_card(deck)

    top_card = deck.draw()

    while True:
        print("\n-------------------")
        print(f"Top card: {top_card}")

        player.show_hand()

        choice = input("Pick a card index or 'd' to draw: ")

        if choice == 'd':
            player.draw_card(deck)
            continue

        if not choice.isdigit():
            print("Invalid input!")
            continue

        choice = int(choice)

        if choice < 0 or choice >= len(player.hand):
            print("Invalid index!")
            continue

        selected = player.hand[choice]

        if can_play(selected, top_card):
            top_card = selected
            player.hand.pop(choice)
            print(f"You played: {selected}")
        else:
            print("You can't play that card!")

        if len(player.hand) == 0:
            print("🎉 You win!")
            break


if __name__ == "__main__":
    main()