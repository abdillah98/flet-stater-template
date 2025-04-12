import flet as ft

# views
from configs.pages import configure_page

# Route 
from routes import route_change
from routes import view_pop

# Components 
from components.NavigationBar import create_navigation_bar

# Configs (yang kita buat)
from configs.views import get_views
from configs.routes import routes
from configs.navigation_bar import navigation_bar_items
from configs.fonts import fonts


def main(page: ft.Page):
    # Inisialisasi Custom Font dan Icon Webfont 
    configure_page(page)
    
    # ✅ Ambil views & items dari config
    views = get_views(page)
    page.navigation_bar = create_navigation_bar(page, views, items=navigation_bar_items)

    column = ft.Column(controls=views, expand=True)
    container = ft.Container(content=column)
    safe_area = ft.SafeArea(content=container, expand=True)

    page.views.clear()
    page.views.append(ft.View("/", [safe_area, page.navigation_bar], padding=0))
    page.update()

    # ✅ Set event listener untuk perubahan rute
    page.on_route_change = lambda _: route_change(page, content=safe_area, routes=routes)
    page.on_view_pop = lambda _: view_pop(page, content=safe_area)

    # Update pembaruan
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)
