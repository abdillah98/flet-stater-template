import flet as ft

# views
# before 
# from views.Chat import ChatView
# from views.Contact import ContactView
# from views.Home import HomeView
# from views.Product import ProductView
# from views.Profile import ProfileView
# from views.Settings import SettingsView
# from views.Store import StoreView

# after
from views import *

# Route 
# Before
# from routes import route_change
# from routes import view_pop

# after
# from routes import route_change

# Components 
# before
# from components.NavigationBar import create_navigation_bar
# After
from components import *


async def main(page: ft.Page):
    # Inisialisasi Custom Font dan Icon Webfont 
    # page.fonts = {
    #     # Custom font 
    #     "Inter-Regular": "/fonts/Inter/used/Inter-Regular.ttf",
    #     "Inter-ExtraBold": "/fonts/Inter/used/Inter-ExtraBold.ttf",
    #     # Icon webfont
    #     "fa-solid": "/fonts/Fontawesome/webfonts/fa-solid-900.ttf",
    #     "fa-regular": "/fonts/Fontawesome/webfonts/fa-regular-400.ttf",
    #     "fa-brands": "/fonts/Fontawesome/webfonts/fa-brands-400.ttf",
    # }

    page.title = "Flet Example Apps"
    # page.theme_mode = ft.ThemeMode.LIGHT
    # page.theme = ft.Theme(font_family="Inter-Regular")  # Default app font
    # page.padding = 0
    
    # ✅ set halaman
    # views = [
    #     HomeView(page),
    #     StoreView(page),
    #     ProfileView(page),
    #     SettingsView(page),
    #     # ContactView(page),
    # ]

    # Daftar route dan handler view-nya
    # routes = [
    #     {"path": "/product/:id", "view": lambda page, route: ProductView(page, route.id)},
    #     {"path": "/chat/:id", "view": lambda page, route: ChatView(page, route.id)},
    #     {"path": "/contact/:id", "view": lambda page, route: ContactView(page, route.id)},
    # ]

    # 🎯 Daftar konfigurasi icon dan label
    # naviagation_bar_items = [
    #     {"icon": "\uf015", "label": "Home"},
    #     {"icon": "\uf07a", "label": "Store"},
    #     {"icon": "\uf007", "label": "Profile"},
    #     {"icon": "\uf013", "label": "Settings"},
    #     # {"icon": "\uf2b9", "label": "Contacts"},
    # ]

    # Tambahkan navigation bar ke layout
    # page.navigation_bar = create_navigation_bar(page, views, items=naviagation_bar_items)

    # Tambahkan ke layout
    # column = ft.Column(
    #     controls=views,  # 🔥 Looping di sini
    #     expand=True
    # )
    
    def route_change(e: ft.RouteChangeEvent):
        page = e.page
        page.views.clear()
        if page.route == "/":
            page.views.append(HomeView(page))
        page.update()
    page.on_route_change = route_change
    page.go("/")
    print("Go to path : /")
   
    # Update pembaruan
    page.update()

ft.app(target=main)
