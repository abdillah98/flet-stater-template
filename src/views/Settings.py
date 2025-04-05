import flet as ft

def SettingsView(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Settings Page", size=20, font_family="Inter-ExtraBold"),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=False,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,  # ✅ Rapi di tengah
    )
