import flet as ft
from components.CustomAppBar import CustomAppBar

def ContactView(page: ft.Page, id):
    container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Contact Page", size=20, font_family="Inter-ExtraBold"),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=True,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,
    )

    return ft.View(
        route=f"/contact/{id}",
        controls=[
            CustomAppBar(title="Contact"),
            ft.SafeArea(container)
        ],
        padding=20,
    )
