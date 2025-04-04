import flet as ft

from components.MyButton import MyButton

def profile_page(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Profile Page", size=20, font_family="Inter-ExtraBold"),
                MyButton("Go to Product", expand=True, on_click= lambda _: page.go('/product/123')),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=False,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,
        # width=float("inf"),
        # bgcolor=ft.colors.BLUE
    )
