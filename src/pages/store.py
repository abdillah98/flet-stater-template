import flet as ft

from components.CustomAppBar import CustomAppBar

def store_page(page: ft.Page):
    return ft.View(
        route="/store",
        controls=[
            CustomAppBar(title="Store"),
            ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
        ],
        padding=20
    )
