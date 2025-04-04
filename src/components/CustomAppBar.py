import flet as ft


class CustomAppBar(ft.AppBar):
    def __init__(self, title: str, bgcolor=ft.Colors.WHITE):
        super().__init__()
        self.title = ft.Text(
            title, 
            color=ft.Colors.BLACK, 
            size=16,    
            font_family="Inter-ExtraBold"  # Menggunakan Google Fonts Inter
        )
        self.bgcolor = bgcolor
        self.center_title = True
