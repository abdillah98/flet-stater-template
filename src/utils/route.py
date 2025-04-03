import flet as ft

def navigate(route: str, page: ft.Page, route_callback, stack=True):
    """Navigasi ke halaman dengan opsi stack tanpa circular import"""
    page.route = route
    route_callback(page, stack=stack)  # Gunakan callback dari main.py
    page.update()

def replace_page(page: ft.Page, new_route: str):
    """Mengganti halaman tanpa menumpuk (clear stack)."""
    page.views.clear()  # Hapus semua halaman sebelumnya
    page.go(new_route)  # Pergi ke halaman baru tanpa stack
