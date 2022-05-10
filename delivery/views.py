from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse

from delivery.models import *


def create_diner_view(request):
    if request.method == "POST":
        diner_name = request.POST.get("name")
        new_diner = Diner()
        new_diner.name
        new_diner.save()
        return redirect("/")
    return render(request, "temp.html")


def test(request):
    diner_info = create_diner("test_diner")
    menu_info = create_menu("test_menu_1", 500, diner_info.get("id"))
    menu_info = create_menu("test_menu_2", 1000, diner_info.get("id"))
    menu_info = create_menu("test_menu_3", 1500, diner_info.get("id"))
    get_menu_diner(menu_info.get("id"))
    get_diner_menus(diner_info.get("id"))
    return JsonResponse({
        "status": "success"
    })


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


def get_menu_diner(menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    diner = menu.diner
    print(f"this menu is for: {diner.name}")


def get_diner_menus(diner_id):
    diner = get_object_or_404(Diner, id=diner_id)
    menu_list = diner.diner_menus.all()
    for menu in menu_list:
        print(f"this diner has menu: {menu.name}")
