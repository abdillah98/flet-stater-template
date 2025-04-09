import flet as ft

def MyButtonV2(**kwargs):
    # Default style bisa tetap kamu definisikan
    default_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        padding=ft.padding.symmetric(vertical=10, horizontal=20),
        text_style=ft.TextStyle(size=14),
    )

    # Kalau user kasih style custom, gabungkan
    kwargs.setdefault("style", default_style)

    return ft.ElevatedButton(**kwargs)
