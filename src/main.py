import flet as ft

from routes import route_change, view_pop

# warnings.filterwarnings("ignore", category=DeprecationWarning)

def main(page: ft.Page):
    
    page.fonts = {
        "InterRegular": "src/assets/fonts/Inter/used/Inter-Regular.ttf",
        "InterBlack": "src/assets/fonts/Inter/used/Inter-Black.ttf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Routes Example"

    page.padding = 0
    page.spacing = 0
    page.expand = True

    # ✅ Gunakan lambda agar bisa kirim parameter `stack`
    page.on_route_change = lambda _: route_change(page, stack=True)  # ❌ Jangan pakai stack di awal
    page.on_view_pop = lambda _: view_pop(page)

    page.go(page.route)  # ✅ Pastikan home ditampilkan pertama kali

    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)
