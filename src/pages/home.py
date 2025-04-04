import flet as ft

def home_page(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Home Page", size=20, font_family="Inter-ExtraBold"),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=True,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,  # ✅ Rapi di tengah
        # width=float("inf"),  # ✅ Lebar penuh
        # bgcolor=ft.colors.YELLOW
    )
