import random

def get_user_choice():
    user_choice = input("Choose Cheeseburger, Hamburger, or Burger: ").lower()
    while user_choice not in ['Cheeseburger', 'Hamburger', 'Burger']:
        print("Invalid choice. Please choose Cheeseburger, Hamburger, or Burger.")
        user_choice = input("Choose Cheeseburger, Hamburger, or Burger: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['Cheeseburger', 'Hamburger', 'Burger']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's the best!"
    elif (user == 'Cheeseburger' and computer == 'Burger') or (user == 'Hamburger' and computer == 'Cheeseburger') or (user == 'Burger' and computer == 'Hamburger'):
        return "Its undiced!"
    else:
        return "still unclear!"

def main():
    print("Today we will find out which burger is the best!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
  
