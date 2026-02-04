from menu import *
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffeMaker = CoffeeMaker()
monyMachine = MoneyMachine()

is_on = True
# print(menu.menu[1].ingredients['coffee'])

# 현재 상황에서 menu.menu를 활용하여 espresso라는 str을 추출하려면 어떡해야 하나요?

while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ')

    if choice == 'report':
        coffeMaker.report()
        monyMachine.report()

    elif choice == 'off':
        print('커피 머신을 종료합니다.')
        is_on = False

    # elif choice in menu.get_items():
    #     drink = menu.find_drink(choice)
    #     if coffeMaker.is_resource_sufficient(drink):
    #         if monyMachine.make_payment(drink.cost):
    #             coffeMaker.make_coffee(drink)

    # else:
    #     drink = menu.find_drink(choice)
    #     if drink is not None:
    #         if coffeMaker.is_resource_sufficient(drink):
    #             if monyMachine.make_payment(drink.cost):
    #                 coffeMaker.make_coffee(drink)

    else:
        drink = menu.find_drink(choice)
        if drink == None:
            continue
        elif coffeMaker.is_resource_sufficient(drink):
                if monyMachine.make_payment(drink.cost):
                    coffeMaker.make_coffee(drink)







