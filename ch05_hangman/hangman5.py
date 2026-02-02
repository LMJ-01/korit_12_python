import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _     ____  _      _____ _      ____  _     
/ \ /|/  _ \/ \  /|/  __// \__/|/  _ \/ \  /|
| |_||| / \|| |\ ||| |  _| |\/||| / \|| |\ ||
| | ||| |-||| | \||| |_//| |  ||| |-||| | \||
\_/ \|\_/ \|\_/  \|\____\\_/  \|\_/ \|\_/  \|
                                             
'''

print(len(stages))
word_list = [
    "apple","banana","camel","dog","cat","lion","tiger","mouse","horse","sheep",
    "goat","cow","pig","chicken","duck","eagle","shark","whale","dolphin","snake",
    "lizard","turtle","rabbit","monkey","panda","zebra","giraffe","elephant","bear","fox",
    "wolf","deer","frog","toad","ant","bee","wasp","spider","butterfly","dragonfly",
    "car","bus","truck","train","plane","ship","boat","bicycle","motorcycle","scooter",
    "road","bridge","tunnel","station","airport","harbor","garage","engine","wheel","brake",
    "house","home","room","kitchen","bathroom","bedroom","window","door","floor","ceiling",
    "table","chair","sofa","bed","pillow","blanket","lamp","mirror","clock","shelf",
    "phone","laptop","tablet","keyboard","mouse","screen","camera","speaker","printer","router",
    "book","paper","pen","pencil","eraser","notebook","marker","crayon","ruler","scissors",
    "school","teacher","student","class","lesson","exam","study","homework","library","college",
    "music","song","piano","guitar","violin","drum","flute","trumpet","radio","concert",
    "movie","film","actor","actress","director","scene","screen","camera","ticket","theater",
    "game","player","score","level","enemy","winner","loser","match","puzzle","quest",
    "food","bread","rice","noodle","pizza","burger","sandwich","salad","soup","steak",
    "fruit","grape","orange","lemon","peach","pear","plum","melon","berry","mango",
    "drink","water","juice","coffee","tea","milk","soda","cola","smoothie","shake",
    "city","village","town","street","market","store","shop","mall","bank","office",
    "money","coin","price","value","budget","salary","income","tax","wallet","credit",
    "weather","sun","moon","star","cloud","rain","snow","wind","storm","thunder",
    "season","spring","summer","autumn","winter","holiday","vacation","travel","trip","journey",
    "country","nation","state","capital","border","island","mountain","river","ocean","forest",
    "color","red","blue","green","yellow","orange","purple","black","white","brown",
    "shape","circle","square","triangle","rectangle","diamond","heart","star","line","curve",
    "emotion","happy","sad","angry","excited","bored","tired","nervous","proud","calm",
    "family","father","mother","parent","brother","sister","uncle","aunt","cousin","grandparent",
    "friend","enemy","partner","neighbor","guest","leader","member","team","group","crowd",
    "job","work","career","office","company","factory","store","market","service","worker",
    "doctor","nurse","teacher","engineer","artist","writer","player","driver","pilot","chef",
    "time","day","night","week","month","year","hour","minute","second","moment",
    "action","run","walk","jump","sit","stand","sleep","eat","drink","think",
    "mind","brain","memory","idea","dream","thought","focus","logic","reason","belief",
    "body","head","face","eye","ear","nose","mouth","hand","arm","leg",
    "health","sick","pain","fever","cold","virus","medicine","doctor","hospital","clinic",
    "science","physics","chemistry","biology","math","algebra","geometry","theory","experiment","data",
    "nature","plant","tree","flower","grass","leaf","root","seed","branch","bush",
    "tool","hammer","nail","screw","wrench","saw","knife","drill","rope","ladder",
    "sport","soccer","baseball","tennis","golf","boxing","ski","skate","surf","swim"
]

chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6

end_of_game = False
print(logo)
while not end_of_game:
    print(stages[lives])
    guess = input('알파벳 입력 >>> ').lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f'기회가 {lives} 번 남았습니다.')
        if lives == 0:
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')
    if '_' not in display:
        print(f'정답입니다 !! 😺😺')
        end_of_game = True

    print(' '.join(display))

