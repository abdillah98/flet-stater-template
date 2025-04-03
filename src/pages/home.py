import flet as ft

from components.CustomAppBar import CustomAppBar
from components.MyButton import MyButton
from utils.route import navigate, replace_page

def home_page(page: ft.Page):
    def on_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Hello from MyButton!"))
        page.overlay.append(page.snack_bar)  # Tambahkan snack bar ke overlay
        page.snack_bar.open = True
        page.update()  # Pastikan update dipanggil

    button_custom = ft.Container(
        content=ft.Row(
            [
                MyButton("Click Me", expand=True, on_click=on_click)
            ],
        ),
    )

    def create_icon():
        return ft.ElevatedButton(
            text="😀",  # ✅ Menggunakan `text` karena `content` tidak valid
            height=50,
            width=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),  # ✅ Border radius custom
                side=ft.BorderSide(0.5, "#E3E3E3"),  # ✅ Border custom
                elevation=0,  # ✅ Menghilangkan shadow
                # bgcolor={"": "white"},  # ✅ Warna latar belakang tetap putih
                # overlay_color={"": "transparent"},  # ✅ Hilangkan efek klik
            ),
        )

    menu = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Row(
                    controls=[create_icon() for _ in range(5)],  # 4 item per row
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ) for _ in range(3)  # Jumlah baris (misal: 3 baris)
            ],
        ),
    )

    view = ft.Container(
        content=ft.Column(
            [
                menu,
                button_custom,
                MyButton("Click Me", on_click=on_click),
                ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ft.ElevatedButton("Visit Chat", on_click=lambda _: page.go("/chat/123")),
            ],
            spacing=20
        ),
    )
    
    return ft.View(
        route="/",
        controls=[
            CustomAppBar("Home Page"),
            view
        ],
        padding=20
    )
