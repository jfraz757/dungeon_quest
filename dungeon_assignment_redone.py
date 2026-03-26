import random

def setup_player():
    """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
    player_name = str(input("Enter your character's name:  "))

    player_stats = {"name": player_name,
                    "health": 10,
                    "inventory": []}
    return player_stats


def create_treasures():
    """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
    treasures = {"Gold": 10,
                 "Ruby": 20,
                 "Sapphire": 15,
                 "Stones": 1}
    return treasures

def display_options(room_number):
    """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
    print(f'You are in Room number {room_number}.')
    


def search_room(player, treasures):
    """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """

    outcome = random.choice(["treasure" , "trap"])
    if outcome == "treasure":
        item_name, item_value = random.choice(list(treasures.items()))

        player["inventory"].append((item_name, item_value))
        print(f'You found a {item_name}! worth {item_value}, it has been added to your inventory')
    else:
        player["health"] -= 2
        print(f"{outcome}! You lost -2hp")
    
    return player, treasures

def check_status(player):
    """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”

    print(f"\nHealth: {player['health']}")

    if len(player["inventory"]) == 0:
        print("Inventory: You have no items yet.")
    else:
        item_names = [item[0] for item in player["inventory"]]
        print(f"Inventory: {', '.join(item_names)}")



def end_game(player, treasures):
    """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
    """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."
    
    total_score = 0
    for item in player["inventory"]:
        total_score += item[1]

    final_health = player["health"]

    print(f'\nYour final health is {final_health}')

    if len(player["inventory"]) > 0:
        print("Items in inventory:")
        for item in player["inventory"]:
            print(f"- {item[0]} (Value: {item[1]})")
    else:
        print("Items in inventory: None")
        
    print(f'Total score: {total_score}')
    print("Game Over! Thanks for playing.")

def run_game_loop(player, treasures):
    """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
    """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

    
    for room in range(1, 6):
        while True:
            display_options(room)
            user_choice = int(input("What would you like to do? \n1. Search for treasure \n2. Move to the next room \n3. Check health and inventory \n4. Quit the game\n  "))
            if user_choice == 1:
                search_room(player, treasures)
                if player["health"] <= 0:
                    print("You died")
                    end_game(player, treasures)
                    return
            elif user_choice == 2:
                break
            elif user_choice == 3:
                check_status(player)
            elif user_choice == 4:
                end_game(player, treasures)
                return
            else:
                print("Input invalid, please try again")
                return

    print("\nYou survived the dungeon!")    
    end_game(player, treasures)
    
# -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------

def main():
    print("--- WELCOME TO THE DUNGEON ---")
    my_player = setup_player()
    game_treasures = create_treasures()

    run_game_loop(my_player, game_treasures)

if __name__ == "__main__":
    main()




        
