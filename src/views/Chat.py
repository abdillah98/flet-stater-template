import flet as ft

from components.ChatItem import ChatItem
from components.CustomAppBar import CustomAppBar
from components.MyButton import MyButton


def ChatView(page: ft.Page, id):
    page.title = "Chat"
    page.bgcolor = "#F6F6F7"

    # def send_message(e):
    #     if user_input.value.strip():
    #         chat.controls.append(
    #             ft.Row(
    #                 [
    #                     ft.Container(
    #                         content=ft.Text(user_input.value, color=ft.Colors.WHITE),
    #                         bgcolor=ft.Colors.BLUE,
    #                         padding=ft.padding.all(10),
    #                         border_radius=10,
    #                     )
    #                 ],
    #                 alignment=ft.MainAxisAlignment.END,
    #             )
    #         )
    #         user_input.value = ""
    #         page.update()

    messages = [
        ("Hello!", False),
        ("Hey, how are you?", True),
        ("I'm good, thanks!", False),
        ("Working on a project.", True),
        ("Nice! What's the project?", False),
        ("A mobile app for tracking tasks.", True),
        ("Hello!", False),
        ("Hey, how are you?", True),
        ("I'm good, thanks!", False),
        ("Working on a project.", True),
        ("Nice! What's the project?", False),
        ("A mobile app for tracking tasks.", True),
    ]

    chat_items = [ChatItem(text, is_sender=sender) for text, sender in messages]

    chat_container = ft.ListView(
        controls=chat_items,
        spacing=10,
        expand=True,  # Mengisi sisa ruang dan bisa scroll
        auto_scroll=True  # Scroll otomatis ke bawah saat ada pesan baru
    )

    container = ft.Container(chat_container, expand=True)

    return ft.View(
        route=f"/chat/{id}",
        controls=[
            CustomAppBar(title="Chat"),
            ft.SafeArea(container)
        ],
        padding=0
    )
