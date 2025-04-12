import flet as ft

from configs.fonts import fonts

def configure_page(page: ft.Page):
    page.fonts = fonts
    page.title = "Flet Example Apps"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(font_family="Inter-Regular")  # Default app font
    page.padding = 0
