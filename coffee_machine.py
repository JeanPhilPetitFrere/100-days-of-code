MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
def money_check(beverage:str,MENU:dict,resources:dict)->str:
    """checks if there if the clients is putting enough coins

    Args:
        beverage (str): name of the coffee the client wants
        MENU (dict) : list of ingredients and cost of each beverage
        resources (dict) : remaining ressources int the machine
        money (float) : money in the machine

    Returns:
        str: _description_
    """
    
    #inputing the number of coins put in the machine
    try:
        quarter = int(input('how many quarters?'))
    except ValueError:
        print("Please input numbers only...")
        quarter = int(input('how many quarters?'))
    try:   
        dime = int(input('how many dimes?'))
    except ValueError:
        print("Please input numbers only...")
        dime = int(input('how many dimes?'))
    try:
        nickel = int(input('how many nickels?'))
    except ValueError:
        print("Please input numbers only...")
        nickel = int(input('how many nickels?'))
    try:
        pennies = int(input('how many pennies?'))
    except ValueError:
        print("Please input numbers only...")
        pennies = int(input('how many pennies?'))

    total_coins = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01

    if total_coins > MENU[beverage]['cost'] and beverage == 'latte':
        x = total_coins - MENU[beverage]['cost']
        print(f'your change is {x}$')
        return resources['water'] - MENU[beverage]['ingredients']['water'],resources['milk'] - MENU[beverage]['ingredients']['milk'],resources['coffee'] - MENU[beverage]['ingredients']['coffee'],total_coins
    
    elif total_coins > MENU[beverage]['cost'] and beverage == 'cappucino':
        x = total_coins - MENU[beverage]['cost']
        print(f'your change is {x}$')
        return resources['water'] - MENU[beverage]['ingredients']['water'],resources['milk'] - MENU[beverage]['ingredients']['milk'],resources['coffee'] - MENU[beverage]['ingredients']['coffee'],total_coins
    
    elif total_coins > MENU[beverage]['cost'] and beverage == 'espresso':
        x = total_coins - MENU[beverage]['cost']
        print(f'your change is {x}$')
        return resources['water'] - MENU[beverage]['ingredients']['water'],resources['milk'] - 0,resources['coffee'] - MENU[beverage]['ingredients']['coffee'],total_coins
    else:
        return f'not enough money'

def get_ressources_check(beverage:str,MENU:dict,resources:dict,money:float)->str:
    """ This function checks if theresources are enough ressources to make the coffee and if there is makes it

    Args:
        beverage (str) : the clients choice of coffee
        MENU (dict): list of ingredients and cost of each beverage
        resources (dict): remaining ressources int the machine
        money (float) : money in the machine

    Returns:
        str: will return a str saresourcesing if we have enough ressources
    """
    if beverage == 'report':
        return resources,money
    elif beverage == 'espresso' and resources['water'] - MENU[beverage]['ingredients']['water'] > 0 and  resources['coffee'] - MENU[beverage]['ingredients']['coffee'] > 0:
        return money_check(beverage,MENU,resources)

    elif beverage == 'latte' and resources['water'] - MENU[beverage]['ingredients']['water'] > 0 and  resources['milk'] - MENU[beverage]['ingredients']['milk'] > 0 and  resources['coffee'] - MENU[beverage]['ingredients']['coffee'] > 0:
        return money_check(beverage,MENU,resources)

    elif beverage == 'cappuccino' and resources['water'] - MENU[beverage]['ingredients']['water'] > 0 and  resources['milk'] - MENU[beverage]['ingredients']['milk'] > 0 and  resources['coffee'] - MENU[beverage]['ingredients']['coffee'] > 0:
        return money_check(beverage,MENU,resources)
    else:
        return f'Not enough ingredients'

get_ressources_check(input("which coffee?"),MENU,resources,money)