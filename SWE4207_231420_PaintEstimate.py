'''
name - precious osamuyimen
ID - 231420
date - 26th oct 2023

'''


#task 1 - this allows the user to quit when they like

def quitA():
    global height, length, width, area, formatted_area, surfacearea
    quitA = str(input('do you want to go futher (yes) or (no)')) # this
    if quitA == 'yes' or quitA == 'Yes':
        return()
    elif quitA == 'no' or quitA == 'No':
        quit()
    else:
        print ('Invalid input, please enter yes or no ')
        quitA()
        # this is the option for the user to quit


while True:

    #task 2
    height = int(input('please insert the height of the walls: \n'))
    length = int(input('please insert the length of the walls: \n'))
    width = int(input('please insert the width of the walls: \n'))
    # the user will need to insert these  measurements for the area to be calculated
    area = (2*(width*length) + 2*(height*width))# the formula for rectangular prism
    formatted_area = '{:.2f}'.format(area)
    print(formatted_area) # the area to 2 decimal places
    quitA()

    # task 3 the options for the wallpaper are listed below
    print(""" Choose from the following wallpaper to buy
                (l) linear
                (p) printed
                (v) vinyl
                (fo) foil
                (fl) flock
                (m) mylar      
            """)
    wallpaper_choice = input().lower()
    while wallpaper_choice not in ['l', 'p', 'v', 'fo', 'fl', 'm']:
        print('error')
        wallpaper_choice = input("Error invalid choice").lower()

    #task 4 and 5
    if wallpaper_choice == 'l':
        print('linear wallpaper is £10.05 per meteres squared ')
        total = area * 10.05
        formatted_area = '{:.2f}'.format(area)
        print(f'your total cost for linear wallpaper is £{formatted_area} ')

    elif wallpaper_choice == 'p':
        print('printed wallpaper is £20.20 per meteres squared ')
        total = area * 20.20
        formatted_area = '{:.2f}'.format(area)
        print(f'your total for printed wallpaper is £{formatted_area}')

    elif wallpaper_choice == 'v':
        print('vinyl wallpaper is £40.60 per meteres squared')
        total = area * 40.60
        formatted_area = '{:.2f}'.format(area)
        print(f'your total for vinyl wallper is £{formatted_area}')

    elif wallpaper_choice == 'fo':
        print('foil wallpaper is £75.50 per meteres squared')
        total = area * 10.05 * 75.50
        formatted_area = '{:.2f}'.format(area)
        print(f'your total for foil wallpaper is £{formatted_area}')

    elif wallpaper_choice == 'fl':
        print('flock wallpaper is £85.70 per meters squared')
        total = area * 85.70
        formatted_area = '{:.2f}'.format(area)
        print(f'your total for flock wallpaper is £{formatted_area}')

    elif wallpaper_choice == 'm':
        print('mylar wallpaper is £90.30 per meters squared')
        total = area * 90.30 * 10.05
        formatted_area = '{:.2f}'.format(area)
        print(f'your total for mylar wallpaper is £{formatted_area}')
    
    more_choice = input("Do you want to look for more wallpaper ? (yes/no): ").lower()
    if more_choice == 'yes':
        # this allows the user to start again
        continue
    else:
        break
    





