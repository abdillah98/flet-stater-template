import flet as ft

def create_navigation_bar(page: ft.Page, pages, items):

    # Menangani pergantian tab 
    def change_page(e):
        selected_index = e.control.selected_index
        print(f"Tab yang dipilih: {selected_index}")

        for index in range(len(pages)):  
            pages[index].visible = False  
        pages[selected_index].visible = True
        page.update()

    # 🧠 Mapping ke NavigationBarDestination
    destinations = []
    for item in items:
        destinations.append(
            ft.NavigationBarDestination(
                icon=ft.Text(item["icon"], font_family="fa-solid", size=14),
                selected_icon=ft.Text(item["icon"], font_family="fa-solid", size=14, color=ft.colors.BLUE),
                label=item["label"]
            )
        )

    return ft.NavigationBar(
        destinations=destinations,
        selected_index=0,
        on_change=change_page,
        bgcolor=ft.colors.WHITE,
        elevation=65,
        indicator_color=ft.colors.TRANSPARENT,
    )
