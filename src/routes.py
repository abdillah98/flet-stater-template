import flet as ft
from flet import TemplateRoute
from pages.product import product_page
from pages.chat import chat_page

def route_change(page: ft.Page, content):
    print(f"Route berubah: {page.route}")

    troute = TemplateRoute(page.route)  # ✅ Gunakan TemplateRoute

    if troute.match("/product/:id"):
        product_id = troute.id  # ✅ Ambil ID dari URL
        print('product_id', product_id)
        page.views.append(product_page(page, product_id))
    elif troute.match("/chat/:id"):
        chat_id = troute.id  # ✅ Ambil ID dari URL
        print('chat_id', chat_id)
        page.views.append(chat_page(page, chat_id))
    else:
        # ✅ Bersihkan tampilan jika kembali ke menu utama
        page.views.clear()
        page.views.append(
            ft.View("/", [content, page.navigation_bar], padding=0)
        )

    page.update()

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