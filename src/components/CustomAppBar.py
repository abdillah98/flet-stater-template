import flet as ft


class CustomAppBar(ft.AppBar):
    def __init__(self, title: str, bgcolor=ft.Colors.WHITE):
        super().__init__()
        self.title = ft.Text(
            title, 
            color="#667085", 
            size=18,    
            # font_family="InterRegular"  # Menggunakan Google Fonts Inter
        )
        self.bgcolor = bgcolor
        self.center_title = True
