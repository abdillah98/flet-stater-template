import flet as ft

from components.MyButton import MyButton

def StoreView(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Home Page", size=20, font_family="Inter-ExtraBold"),
                MyButton("Visit Product", on_click=lambda _: page.go("/product/123")),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=False,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,
    )
