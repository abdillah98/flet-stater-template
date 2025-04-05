import flet as ft

def MyButtonV2(text: str, on_click=None, expand=False):
    return ft.ElevatedButton(
        text=text,
        on_click=on_click,
        expand=expand,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE,
            padding=ft.padding.symmetric(vertical=10, horizontal=20),
            text_style=ft.TextStyle(size=14),
        ),
    )
