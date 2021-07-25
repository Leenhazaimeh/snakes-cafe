menue = {"Appetizers":["Wings","Cookies","Spring Rolls"],
"Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
"Desserts":["Ice Cream","Cake","Pie"],
"Drinks":["Coffee","Tea","Unicorn Tears"],
}



def printMenueIntro():
    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Please see our menu below.    **')
    print('**')
    print('** To quit at any time, type "quit" **')
    print('**************************************\n')
    print('')
    categories = menue.items()
    print(categories)
    for key, value in categories:
      print(key)
      print('-'*len(key))
      print(value)
      for dish in value:
        print(dish)
      print('\n')


def enterOrder():
    count=0
    count_2=0
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************\n')
    order = input('> ')
    print('\n')
    dish = order
    while order:
      if order == 'quit':
        exitProgram()
      else:
        if dish == order:
            count+=1
            print(f'** {count} order of {order} have been added to your meal **\n')
        else:
            dish_2=order
            count_2+=1
            print(f'** {count_2} order of {order} have been added to your meal **\n')
        order=''
        order = input('> ')
        print('\n')
          
          
def exitProgram():
    exitInput=input('Would you like to exit the program?quit(y/n) \n> ')
    if exitInput=='y':
        exit()
    else:
        enterOrder()


printMenueIntro()
enterOrder()