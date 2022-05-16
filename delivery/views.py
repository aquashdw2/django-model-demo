import datetime

from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.db.models import Q, F

from delivery.models import *


def diner_query(request):
    queryset = Diner.objects.all()

    return JsonResponse({
        "results": list(queryset.values())
    }, json_dumps_params={"ensure_ascii": False})


def test(request):
    category_han = create_category("한식")
    category_bun = create_category("중식")
    category_pun = create_category("일식")

    area_sun = create_area("선릉")
    area_sam = create_area("삼성")
    area_seo = create_area("서초")

    diner_info = create_diner("test_diner_1")
    menu_info = create_menu("test_menu_1", 500, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    menu_info = create_menu("test_menu_2", 1000, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    menu_info = create_menu("test_menu_3", 1500, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    set_diner_category(diner_info.get("id"), category_han.get("id"))
    set_diner_category(diner_info.get("id"), category_bun.get("id"))
    set_diner_delivery_area_1(diner_info.get("id"), area_sun.get("id"), fee=5000)
    set_diner_delivery_area_2(diner_info.get("id"), area_sam.get("id"), fee=6000)

    get_menu_diner(menu_info.get("id"))
    get_diner_menus(diner_info.get("id"))
    get_diner_categories(diner_info.get("id"))
    get_diner_delivery_fees_per_area(diner_info.get("id"))

    diner_info = create_diner("test_diner_2")
    menu_info = create_menu("test_menu_4", 500, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    menu_info = create_menu("test_menu_5", 1000, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    menu_info = create_menu("test_menu_6", 1500, diner_info.get("id"))
    create_menu_option_group("size", True, menu_info.get("id"))
    create_menu_option_group("sari", False, menu_info.get("id"), select_max=10)
    set_diner_category(diner_info.get("id"), category_han.get("id"))
    set_diner_category(diner_info.get("id"), category_pun.get("id"))
    set_diner_delivery_area_1(diner_info.get("id"), area_sun.get("id"), fee=5000)
    set_diner_delivery_area_2(diner_info.get("id"), area_seo.get("id"), fee=10000)
    
    get_menu_diner(menu_info.get("id"))
    get_diner_menus(diner_info.get("id"))
    get_diner_categories(diner_info.get("id"))
    get_diner_delivery_fees_per_area(diner_info.get("id"))

    return JsonResponse({
        "status": "success"
    })


def prepare_test_data():
    category_korea = create_category("한식")
    category_china = create_category("중식")
    category_chicken = create_category("치킨")

    area_yeoksam = create_area("역삼동", 37.4999, 127.0374)
    area_samsung = create_area("삼성동", 37.5140, 127.0565)
    area_daechi = create_area("대치동", 37.4995, 127.0611)
    area_dogok = create_area("도곡동", 37.4898, 127.0438)

    diner_y_1 = create_diner("봄날 역삼")
    set_diner_category(diner_y_1.get("id"), category_korea.get("id"))
    set_diner_delivery_area_1(diner_y_1.get("id"), area_yeoksam.get("id"))
    set_diner_delivery_area_1(diner_y_1.get("id"), area_samsung.get("id"), 2000)
    set_diner_delivery_area_1(diner_y_1.get("id"), area_dogok.get("id"), 2000)
    diner_y_2 = create_diner("홍콩반점 역삼", close=datetime.time(23, 00))
    set_diner_category(diner_y_2.get("id"), category_china.get("id"))
    set_diner_delivery_area_1(diner_y_2.get("id"), area_yeoksam.get("id"))
    set_diner_delivery_area_1(diner_y_2.get("id"), area_samsung.get("id"), 2000)
    set_diner_delivery_area_1(diner_y_2.get("id"), area_daechi.get("id"), 2000)
    set_diner_delivery_area_1(diner_y_2.get("id"), area_dogok.get("id"), 2000)
    diner_y_3 = create_diner("교촌치킨 역삼", opens=datetime.time(15, 00), close=datetime.time(00, 00))
    set_diner_category(diner_y_3.get("id"), category_chicken.get("id"))
    set_diner_delivery_area_1(diner_y_3.get("id"), area_yeoksam.get("id"))
    set_diner_delivery_area_1(diner_y_3.get("id"), area_samsung.get("id"), 2000)
    set_diner_delivery_area_1(diner_y_3.get("id"), area_daechi.get("id"), 2000)
    set_diner_delivery_area_1(diner_y_3.get("id"), area_dogok.get("id"), 2000)

    diner_s_1 = create_diner("남도구한들정식", opens=datetime.time(9, 00), close=datetime.time(19, 00))
    set_diner_category(diner_s_1.get("id"), category_korea.get("id"))
    set_diner_delivery_area_1(diner_s_1.get("id"), area_samsung.get("id"), 5000)
    diner_s_2 = create_diner("홍콩반점 삼성", close=datetime.time(23, 00))
    set_diner_category(diner_s_2.get("id"), category_china.get("id"))
    set_diner_delivery_area_1(diner_s_2.get("id"), area_yeoksam.get("id"), 2000)
    set_diner_delivery_area_1(diner_s_2.get("id"), area_samsung.get("id"))
    set_diner_delivery_area_1(diner_s_2.get("id"), area_daechi.get("id"), 2000)
    set_diner_delivery_area_1(diner_s_2.get("id"), area_dogok.get("id"), 2000)
    diner_s_3 = create_diner("BHC 삼성동", close=datetime.time(23, 00))
    set_diner_category(diner_s_3.get("id"), category_chicken.get("id"))
    set_diner_delivery_area_1(diner_s_3.get("id"), area_yeoksam.get("id"), 3000)
    set_diner_delivery_area_1(diner_s_3.get("id"), area_samsung.get("id"), 3000)
    set_diner_delivery_area_1(diner_s_3.get("id"), area_daechi.get("id"), 3000)
    set_diner_delivery_area_1(diner_s_3.get("id"), area_dogok.get("id"), 3000)

    diner_da1 = create_diner("채근담 대치", close=datetime.time(23, 00))
    set_diner_category(diner_da1.get("id"), category_korea.get("id"))
    set_diner_delivery_area_1(diner_da1.get("id"), area_daechi.get("id"))
    set_diner_delivery_area_1(diner_da1.get("id"), area_dogok.get("id"))
    diner_da2 = create_diner("미래향", close=datetime.time(23, 30))
    set_diner_category(diner_da1.get("id"), category_china.get("id"))
    set_diner_delivery_area_1(diner_da2.get("id"), area_yeoksam.get("id"))
    set_diner_delivery_area_1(diner_da2.get("id"), area_samsung.get("id"))
    set_diner_delivery_area_1(diner_da2.get("id"), area_daechi.get("id"))
    set_diner_delivery_area_1(diner_da2.get("id"), area_dogok.get("id"))
    diner_da3 = create_diner("굽네치킨 대치동", close=datetime.time(1, 00))
    set_diner_category(diner_da3.get("id"), category_chicken.get("id"))
    set_diner_delivery_area_1(diner_da3.get("id"), area_yeoksam.get("id"), 2000)
    set_diner_delivery_area_1(diner_da3.get("id"), area_samsung.get("id"), 2000)
    set_diner_delivery_area_1(diner_da3.get("id"), area_daechi.get("id"), 2000)
    set_diner_delivery_area_1(diner_da3.get("id"), area_dogok.get("id"), 2000)

    diner_do1 = create_diner("경복궁 도곡")
    set_diner_category(diner_do1.get("id"), category_korea.get("id"))
    set_diner_delivery_area_1(diner_do1.get("id"), area_daechi.get("id"), 3999)
    set_diner_delivery_area_1(diner_do1.get("id"), area_dogok.get("id"), 4999)
    diner_do2 = create_diner("홀리차우 도곡점", close=datetime.time(23, 00))
    set_diner_category(diner_do2.get("id"), category_china.get("id"))
    set_diner_delivery_area_1(diner_do2.get("id"), area_yeoksam.get("id"), 500)
    set_diner_delivery_area_1(diner_do2.get("id"), area_samsung.get("id"), 500)
    set_diner_delivery_area_1(diner_do2.get("id"), area_daechi.get("id"), 500)
    set_diner_delivery_area_1(diner_do2.get("id"), area_dogok.get("id"), 500)
    diner_do3 = create_diner("교촌치킨 도곡", close=datetime.time(0, 00))
    set_diner_category(diner_do3.get("id"), category_chicken.get("id"))
    set_diner_delivery_area_1(diner_do3.get("id"), area_yeoksam.get("id"), 2000)
    set_diner_delivery_area_1(diner_do3.get("id"), area_samsung.get("id"), 2000)
    set_diner_delivery_area_1(diner_do3.get("id"), area_daechi.get("id"), 2000)
    set_diner_delivery_area_1(diner_do3.get("id"), area_dogok.get("id"), 2000)


def create_diner(name, opens=datetime.time(11, 00), close=datetime.time(21, 00)):
    new_diner = Diner()
    new_diner.name = name
    if opens and close:
        new_diner.opens = opens
        new_diner.closes = close
    new_diner.save()
    return {
        "id": new_diner.id,
        "name": new_diner.name,
    }


def create_menu(name, price, diner_id):
    new_menu = Menu()
    new_menu.name = name
    new_menu.price = price

    new_menu.diner = get_object_or_404(Diner, id=diner_id)
    new_menu.save()
    return {
        "id": new_menu.id,
        "name": new_menu.name,
        "price": new_menu.price,
    }


def create_menu_option_group(name, mandatory, menu_id, select_min=0, select_max=1):
    new_menu_option_group = MenuOptionGroup()
    new_menu_option_group.name = name
    new_menu_option_group.mandatory = mandatory
    new_menu_option_group.for_menu = get_object_or_404(Menu, pk=menu_id)
    new_menu_option_group.select_min = select_min
    new_menu_option_group.select_max = select_max
    new_menu_option_group.save()


def create_category(name):
    new_category = FoodCategory()
    new_category.name = name
    new_category.save()
    return { "id": new_category.id }


def create_area(name, lat=None, long=None):
    new_area = Area()
    new_area.name = name
    if lat and long:
        new_area.latitude = lat
        new_area.longitude = long
    new_area.save()

    return { "id": new_area.id }


def get_menu_diner(menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    diner = menu.diner
    print(f"this menu is for: {diner.name}")


def get_diner_menus(diner_id):
    diner = get_object_or_404(Diner, id=diner_id)
    menu_list = diner.diner_menus.all()
    for menu in menu_list:
        print(f"this diner has menu: {menu.name}")


def get_diner_categories(diner_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    diner_categories = target_diner.diner_categories.all()
    for category in diner_categories:
        print(f"the category of this diner: {category.name}")


def get_category_diners(category_id):
    target_category = get_object_or_404(FoodCategory, id=category_id)
    category_diners = target_category.category_diners.all()
    for diner in category_diners:
        print(f"diners under this category: {diner.name}")


def get_diner_delivery_area(diner_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    diner_delivery_area = target_diner.deliver_area.all()
    for area in diner_delivery_area:
        print(f"this diner delivers to: {area.name}")


def get_area_delivering_diners(area_id):
    target_area = get_object_or_404(Area, id=area_id)
    diners_in_area = target_area.diners.all()
    for diner in diners_in_area:
        print(f"this area has diner: {diner.name}")


def get_diner_delivery_fees_per_area(diner_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    diner_delivery_area = get_list_or_404(DeliveryArea, diner=target_diner)
    for delivery_area in diner_delivery_area:
        print(f"to deliver to: {(delivery_area.area).name}, costs: {delivery_area.fee}")


def set_diner_category(diner_id, category_id):
    target_diner = get_object_or_404(Diner, id=diner_id)
    target_category = get_object_or_404(FoodCategory, id=category_id)
    target_category.category_diners.add(target_diner)
    target_category.save()


def set_diner_delivery_area_1(diner_id, area_id, fee=1000):
    target_diner = get_object_or_404(Diner, id=diner_id)
    target_area = get_object_or_404(Area, id=area_id)
    new_delivery_area = DeliveryArea()
    new_delivery_area.diner = target_diner
    new_delivery_area.area = target_area
    new_delivery_area.fee = fee
    new_delivery_area.save()


def set_diner_delivery_area_2(diner_id, area_id, fee=1000):
    target_diner = get_object_or_404(Diner, id=diner_id)
    target_area = get_object_or_404(Area, id=area_id)
    target_diner.deliver_area.add(target_area, through_defaults={
        "fee": fee,
    })
    target_diner.save()
