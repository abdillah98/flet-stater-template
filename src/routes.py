import flet as ft
from flet import TemplateRoute
from views.Product import ProductView
from views.Chat import ChatView

# Routing dinamis dengan stack route 
def route_change(page: ft.Page, content, routes):
    print(f"Route berubah: {page.route}")
    matched = False

    for route in routes:
        troute = TemplateRoute(page.route)
        if troute.match(route["path"]):
            print(f"Matched: {route['path']} with params: {troute.__dict__}")
            page.views.append(route["view"](page, troute))
            matched = True
            break

    if not matched:
        # Fallback untuk route tidak dikenal
        page.views.clear()
        page.views.append(
            ft.View("/", [content, page.navigation_bar], padding=0)
        )

    page.update()


# Fungsi untuk menangani route Go Back 
def view_pop(page: ft.Page, content):
    """Menghapus halaman terakhir jika ada lebih dari satu"""
    if len(page.views) > 1:
        page.views.pop()
        prev_route = page.views[-1].route if page.views else "/"
        print(f"Kembali ke: {prev_route}")

        if prev_route != page.route:
            page.go(prev_route)

    # ✅ Bersihkan layout sebelum menambahkan ulang elemen
    page.views.clear()
    print('kedua')
    page.views.append(ft.View("/", [content, page.navigation_bar], padding=0))
    page.update()