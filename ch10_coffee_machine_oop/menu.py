class MenuItem:
    """각 메뉴 아이템들을 모델링합니다."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,

            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """음료 메뉴를 모델링합니다."""
    def __init__(self):
        self.menu = [
            MenuItem(name="라떼", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="에스프레소", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="카푸치노", water=250, milk=50, coffee=24, cost=3),
            MenuItem(name="카라멜마키아토", water=200, milk=60, coffee=26, cost=4),
            MenuItem(name="아이스아메리카노", water=200, milk=0, coffee=26, cost=1),
            MenuItem(name="바닐라라떼", water=200, milk=150, coffee=24, cost=3.5),
            MenuItem(name="헤이즐넛라떼", water=200, milk=150, coffee=24, cost=3.5),
            MenuItem(name="카페모카", water=200, milk=120, coffee=24, cost=4),
            MenuItem(name="화이트모카", water=200, milk=120, coffee=24, cost=4),
            MenuItem(name="돌체라떼", water=200, milk=170, coffee=24, cost=4.5),
            MenuItem(name="아포가토", water=50, milk=100, coffee=24, cost=4),
            MenuItem(name="콜드브루", water=250, milk=0, coffee=30, cost=3),
            MenuItem(name="아이스라떼", water=200, milk=150, coffee=24, cost=3),
            MenuItem(name="플랫화이트", water=150, milk=120, coffee=24, cost=3.5),
            MenuItem(name="롱블랙", water=180, milk=0, coffee=24, cost=2),
        ]

    def get_items(self):
        """이용 가능한 모든 메뉴 아이템의 이름을 반환합니다."""
        options = ""
        for item in self.menu:
            options += f" {item.name} /"
        return options

    def find_drink(self, order_name):
        """특정 음료를 이름으로 메뉴에서 검색합니다. 해당 아이템이 존재하면 반환하고, 그렇지 않으면 None을 반환합니다."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("죄송합니다. 해당 아이템은 이용할 수 없습니다.")