import flet as ft
import datetime

class ChatItem(ft.Column):
    def __init__(self, text: str, is_sender: bool = False, timestamp: str = None, prev_sender: bool = None):
        super().__init__()

        self.alignment = ft.alignment.top_right if is_sender else ft.alignment.top_left  # ✅ FIX: Posisi pengirim di kanan
        
        if timestamp is None:
            timestamp = datetime.datetime.now().strftime("%H:%M")  # ⏳ Format HH:MM

        # Chat bubble
        bubble = ft.Container(
            content=ft.Row(
                [
                    ft.Text(
                        text,
                        color=ft.Colors.WHITE if is_sender else ft.Colors.BLACK,
                        text_align=ft.TextAlign.RIGHT if is_sender else ft.TextAlign.LEFT,  # 🔥 Align kanan untuk pengirim
                        expand=True,
                        no_wrap=False,
                        # font_family="InterReguler"
                    ),
                    ft.Icon(ft.icons.DONE_ALL, size=10, color=ft.Colors.WHITE) if is_sender else ft.Container()
                ],
                alignment=ft.MainAxisAlignment.END if is_sender else ft.MainAxisAlignment.START,  # ✅ FIX: Pastikan ikon tetap kanan
                spacing=5
            ),
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.BLUE if is_sender else ft.Colors.WHITE,
            border=ft.border.all(0.5, "#E3E3E3") if not is_sender else None,  # ✅ Border hanya untuk pengirim
            border_radius=10,
            width=min(600 * 0.7, len(text) * 8 + 20),  # ✅ Bubble maksimal 70%, minimal sesuai teks
        )

        # Timestamp (Jam chat)
         # **Tampilkan jam hanya jika pengirim berbeda dari sebelumnya**
        time_label = None
        if prev_sender is None or prev_sender != is_sender:
            time_label = ft.Container(
                content=ft.Text(
                    timestamp,
                    size=10,
                    color=ft.Colors.GREY,
                ),
                alignment=ft.alignment.center_right if is_sender else ft.alignment.center_left,  # ✅ Pastikan jam tetap kanan/kiri
                width=min(600 * 0.5, len(text) * 8 + 20),  # ✅ Bubble maksimal 70%, minimal sesuai teks
            )

        # **FIX**: Gunakan Row agar pengirim tetap kanan & penerima tetap kiri
        self.controls.append(
            ft.Container(
                content= ft.Row(
                    [
                        ft.Column(
                            [bubble] + ([time_label] if time_label else []),  # ✅ Tambahkan timestamp jika perlu
                            spacing=4, alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END if is_sender else ft.MainAxisAlignment.START,  # ✅ Fix posisi
                ),
                padding=20
            ),
        )
