import itertools as it
from random import shuffle

def interactiveListSorter(dictionary: dict) -> dict:
    comp_list = list(it.combinations(dictionary, 2))
    shuffle(comp_list)

    for index in range(len(comp_list)):
        while True:
            try:
                pref = int(input(f'Type "1" if you prefer {comp_list[index][0]} or "2" if you prefer {comp_list[index][1]}\n'))
                if pref != 1 and pref != 2:
                    print('Please enter a valid response')
                    continue
                break
            except ValueError:
                print('Please enter a valid response')
                continue

        score = dictionary.get(comp_list[index][pref - 1])
        score += 1
        dictionary.update({comp_list[index][pref - 1]: score})

    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

def manual_list() -> dict:
    things = {}
    user_input = input('Type what you want to put in the list; after one entry, press enter; when you\'re done, press enter without having typed anything:\n')
    while user_input != '':
        things.update({user_input : 0})
        user_input = input()
    return things

def auto_list(filename) -> dict:
    with open(filename, "r") as file:
        text = file.read()
    keys = text.splitlines()
    values = [0] * len(keys)
    return dict(zip(keys, values))

if __name__ == '__main__':
    while True:
            try:
                choice = int(input(f'Type "1" if you want to manually enter a list of items or "2" if you want to get the list of items from an external file\n'))
                if choice != 1 and choice != 2:
                    print('Please enter a valid response')
                    continue
                break
            except ValueError:
                print('Please enter a valid response')
                continue
    
    if choice == 1:
        things = manual_list()
    elif choice == 2:
        while True:
            try:
                filename = str(input('Type the name of the file here (if the file is not in the same directory as this script, then please type the full path):\n')).strip()
                things = auto_list(filename)
                break
            except FileNotFoundError:
                print('Either the path was typed incorrectly or the file cannot be found. Please check the path name and try again.')
                continue
    
    sorted_things = interactiveListSorter(things)
    sorted_things_as_list = list(sorted_things)
    #print(sorted_things)
    #print(sorted_things_as_list)
    print('Here is how your list of items rank according to your preferences:')
    rank = 1
    rankskip = 1
    for j in range(len(sorted_things_as_list)):
        print(f'{rank}. {sorted_things_as_list[j]}')
        try:
            if sorted_things.get(sorted_things_as_list[j]) > sorted_things.get(sorted_things_as_list[j + 1]):
                rank += rankskip
                rankskip = 1
            else:
                rankskip += 1
        except IndexError:
            break
#
