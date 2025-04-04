import flet as ft

# Pages
from pages.chat import chat_page
from pages.home import home_page
from pages.product import product_page
from pages.profile import profile_page
from pages.settings import settings_page
from pages.store import store_page

# Route 
from routes import route_change
from routes import view_pop

# Components 
from components.NavigationBar import create_navigation_bar


def main(page: ft.Page):
    page.fonts = {
        "Inter-Regular": "/fonts/Inter/used/Inter-Regular.ttf",
        "Inter-ExtraBold": "/fonts/Inter/used/Inter-ExtraBold.ttf",
        "fa-solid": "/fonts/Fontawesome/webfonts/fa-solid-900.ttf",
        "fa-regular": "/fonts/Fontawesome/webfonts/fa-regular-400.ttf",
        "fa-brands": "/fonts/Fontawesome/webfonts/fa-brands-400.ttf",
    }

    page.title = "Flet Example Apps"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(font_family="Inter-Regular")  # Default app font
    page.padding = 0
    
    # ✅ set halaman
    pages = [
        home_page(page),
        store_page(page),
        profile_page(page),
        settings_page(page),
    ]

    column = ft.Column(
        controls=pages,  # 🔥 Looping di sini
        expand=True
    )

    container = ft.Container(
        content=column,
        # bgcolor=ft.Colors.YELLOW
    )

    safe_area = ft.SafeArea(
        content=container,  # Default Home Page
        expand=True,
    )


    # Tambahkan navigation bar ke layout
    page.navigation_bar = create_navigation_bar(page, pages)

    # Tambahkan ke layout
    page.views.clear()
    page.views.append(ft.View("/", [safe_area, page.navigation_bar], padding=0))
    page.update()

    # ✅ Set event listener untuk perubahan rute
    page.on_route_change = lambda _: route_change(page, content=safe_area)
    page.on_view_pop = lambda _: view_pop(page, content=safe_area)

    # Update pembaruan
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)
