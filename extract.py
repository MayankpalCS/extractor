import re
from colorama import init, Fore

init()
red=Fore.RED
green=Fore.GREEN
yellow=Fore.YELLOW
reset=Fore.RESET
def banner():
    print(f"""%s{green}
             |------ \   / --------- |-----| |------| |--------- --------- |-------| |-----|
             |        \ /      |     |     | |      | |              |     |       | |     | 
             |------   /       |     |-----| |------| |              |     |       | |-----|
             |        / \      |     |\      |      | |              |     |       | ||
             |------ /    \    |     | \     |      | |              |     |       | | |
             @Developed by - Mayank Pal  \   |      | |---------     |     |-------| |  |
                           """)
banner()
print("1:Email scanner")
print('2:phone no. scanner ')
print('3:webpage scanner')
a=int(input("Enter"))
if a == 1:
    word = re.compile(r'.........................................@....................|...........................@.................|......................@.........|....................@....................|...................@..................|..................@.................|.................@................|................@...............|...............@..............|..............@............|............@............|............@...........|..........@..........|.........@.........|........@........|.......@.......|......@......|.....@.....|....@....|...@...|.................................@..............|.......................@..............|.........................@....................|......................................@..................|.@.................|..@..................|...@...............|....@................|......@...............')
    file = open('input.txt','r')
    for i in file:
        stri=str(i)
        match = word.finditer(stri)
        for matches in match:
            print(f'{green}here is the string which might contain info related email')
            print('-' * 100)
            print(f'{red}{matches.string}')
            print(matches)

elif a == 2:

    word = re.compile(r'\d{10}|\D\D\D\D\d{10}|\D\D\D\d{10}|\D\D\d{10}')
    file = open('input.txt','r')
    for i in file:
        stri=str(i)
        match = word.finditer(stri)
        for matches in match:
            print('-'*100)
            print(f"{green}Here is the string which might contain info related phone no.")
            print(f'{red}{matches.string}')
            print(matches)

elif a == 3:
    word = re.compile(r'http.........................................................................|http.......................................................................|http.....................................................................|http...................................................................|http.................................................................|http...............................................................|http.............................................................|http...........................................................|http.........................................................|http.......................................................|http.....................................................|http...................................................|http.................................................|http...............................................|http...........................................|http.........................................|http.....................................|http..................................|http...............................|http..............................|http............................|http........................|http.....................|http...............|http..........|http......| http......')
    file=open('input.txt','r')
    for i in file:
        stri=str(i)
        match = word.finditer(stri)
        for matches in match:
            print(f"{green}Here is the string where webpage related info might be")
            print('-' * 80)
            print(f'{red}{matches.string}')
            print(matches)
