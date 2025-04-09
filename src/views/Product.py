import flet as ft

from components.CustomAppBar import CustomAppBar
from components.MyButton import MyButton
from components.MyButtonV2 import MyButtonV2
from routes import *
def ProductView(page: ft.Page, id):
    
    column = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    # Before
                    # ft.ElevatedButton("Go Home", expand=True, on_click=lambda _: page.go("/")),
                    
                    # after
                    ft.ElevatedButton("Go Home",expand=True,on_click=navigate_to(page,"/")),
                    
                    MyButtonV2(
                        text="Click Me",
                        on_click=lambda e: print("clicked!"),
                        expand=True,
                      
                    ) ,
                ],
                spacing=2
            ),
            ft.Row(
                controls=[
                    MyButton("Go to Chat", expand=True, on_click=navigate_to(page,"/chat/123")),
                    MyButtonV2("Go to Chat (v2)", expand=True, on_click=navigate_to(page,"/chat/123"))
                ]
            )
        ],
        expand=True,
    )

    container = ft.Container(
        content=column,
        expand=True,
        # bgcolor=ft.Colors.YELLOW,
    )

    return ft.View(
        route=f"/product/{id}",
        controls=[
            CustomAppBar(title="Product"),
            ft.SafeArea(container)
        ],
        padding=20,
    )
