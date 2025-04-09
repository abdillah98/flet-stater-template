import flet as ft
from routes import *
from components import *
def HomeView(page: ft.Page):
   return ft.View(
        route="/",
        controls=
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("oke 2 Home Page", size=20, font_family="Inter-ExtraBold"),
                        MyButtonV2(
                        text="navigate to",
                        on_click=navigate_to(page,"/testing"),
                        expand=True,
                   
                    )
                    ], 
                    scroll=ft.ScrollMode.AUTO, 
                    expand=True
                ),
                visible=True,
                expand=True,
                padding=0,
                alignment=ft.alignment.center,  # ✅ Rapi di tengah
                )
        ]
        )
