# play_hangman이라는 함수를 call1() 유형으로 정의하고, 호출하시오.
import random
from hangman_arts import *
from hangman_word_list import word_list

def play_hangman():
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

play_hangman()