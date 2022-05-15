from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.http import JsonResponse

from delivery.models import *


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
    category_japan = create_category("일식")
    category_west = create_category("양식")

    area_sun = create_area("선릉")
    area_sam = create_area("삼성")
    area_seo = create_area("서초")


def create_diner(name):
    new_diner = Diner()
    new_diner.name = name
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


def create_area(name):
    new_area = Area()
    new_area.name = name
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
