import flet as ft

def settings_page(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Settings Page", size=20, font_family="Inter-ExtraBold"),
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
