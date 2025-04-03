import flet as ft
from flet import TemplateRoute
# from repath import TemplateRoute
from pages.home import home_page
from pages.store import store_page
from pages.chat import chat_page

def route_change(page: ft.Page, stack=True):
    """Mengatur navigasi dengan opsi stack (tumpukan halaman)"""
    if not stack:
        page.views.clear()  # ✅ c

    # ✅ Buat routing dinamis
    troute = TemplateRoute(page.route)

    if troute.match("/"):
        page.views.clear() # Hapus semua halaman sebelumnya jika tidak pakai stack 
        page.views.append(home_page(page))
    elif troute.match("/store"):
        page.views.append(store_page(page))
    elif troute.match("/chat/:id"):
        page.views.append(chat_page(page))
        print("Chat ID:", troute.id)
    else:
        print("Unknown route")

    # # ✅ Tambahkan halaman lain sesuai route
    # if page.route == "/":
    #     page.views.clear()
    #     page.views.append(home_page(page))
    # elif page.route == "/store":
    #     page.views.append(store_page(page))
    # elif page.route == "/chat":
    #     page.views.append(chat_page(page))

    page.update()
    

def view_pop(page: ft.Page):
    """Menghapus halaman terakhir jika ada lebih dari satu"""
    if len(page.views) > 1:
        page.views.pop()
        page.go(page.views[-1].route)  # ✅ Navigasi ke halaman sebelumnya
