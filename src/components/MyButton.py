import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text: str, on_click=None, expand=False): # paramters (props)
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.expand = expand  # ✅ Memperbaiki kesalahan sintaksis
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),  # ✅ Membuat sudut membulat
            bgcolor=ft.colors.BLUE,  # ✅ Warna tombol
            color=ft.colors.WHITE,  # ✅ Warna teks
            padding=ft.padding.symmetric(vertical=10, horizontal=20),  # ✅ Padding tombol
            text_style = ft.TextStyle(size=14)
        )
