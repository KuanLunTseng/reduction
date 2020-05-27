from copy import deepcopy as cpy
import json 
import random

NAME = ["Aaron", "Baldhere", "Camillia", "Dunstin", "Eulalia", "Francisco", "Gregory", "Hinrick", "Irina", "Jovonnah", "Krystiano", "Lucena", "Martha", "Norris", "Owain", "Pyrena", "Quinn", "Renato", "Salomon", "Toynetta", "Una", "Verlin", "Wythe", "Xena", "York", "Zaza"]
NUM = len(NAME)




with open('list.json') as json_file:
    data = json.load(json_file)
    
def rand_friend_list(name):
    friend_list = cpy(NAME)
    
    # yourself cannot be your friend 
    friend_list.remove(name)
    n = random.randint(0, len(friend_list))
    random.shuffle(friend_list)
    
    return sorted([friend_list.pop() for i in range(n)])
    
def create_json_file():
    data = {}
    data['people'] = []
    for n in NAME:
        data['people'].append({
            'Name': n,
            'Friends': rand_friend_list(n)
        })

    with open('data.json', 'w') as outfiles:
        json.dump(data, outfiles)






def main():
    create_json_file()

if __name__ == '__main__':
   main()
