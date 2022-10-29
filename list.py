import time

thislist = []

thislist.append(input('What is the first item you would like to add to your list?\n'))

time.sleep(.5)

while thislist:
    listedit = input('\nWould like to:\n1. Add another item\n2. Print curent items in the list\n3. Exit\n')
    time.sleep(.5)

    if listedit == '1':
        thislist.append(input('\nWhat would you like to add? '))
        time.sleep(.5)

    if listedit == '2':
        print('\nCurrently these items are in your list: ', *thislist, sep='\n')
        time.sleep(.5)
    
    if listedit ==  '3':
        print('Exiting list!')
        break

exit

