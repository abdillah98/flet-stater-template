import flet as ft

def create_navigation_bar(page: ft.Page, pages):
    def change_page(e):
        selected_index = e.control.selected_index  # Ambil index yang dipilih
        print(f"Tab yang dipilih: {selected_index}")

        # ✅ Set semua halaman tidak terlihat
        for index in range(len(pages)):  
            pages[index].visible = False  

        # ✅ Tampilkan halaman yang dipilih
        pages[selected_index].visible = True

        page.update()
    
    # Set Icon 
    iconHome = ft.Text("\uf015", font_family="fa-solid", size=14)
    iconStore = ft.Text("\uf07a", font_family="fa-solid", size=14)
    iconProfile = ft.Text("\uf007", font_family="fa-solid", size=14)
    iconSettings = ft.Text("\uf013", font_family="fa-solid", size=14)
    iconHomeActive = ft.Text("\uf015", font_family="fa-solid", size=14, color=ft.Colors.BLUE)
    iconStoreActive = ft.Text("\uf07a", font_family="fa-solid", size=14, color=ft.Colors.BLUE)
    iconProfileActive = ft.Text("\uf007", font_family="fa-solid", size=14, color=ft.Colors.BLUE)
    iconSettingsActive = ft.Text("\uf013", font_family="fa-solid", size=14, color=ft.Colors.BLUE)

    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=iconHome, label="Home", selected_icon=iconHomeActive),
            ft.NavigationBarDestination(icon=iconStore, label="Store", selected_icon=iconStoreActive),
            ft.NavigationBarDestination(icon=iconProfile, label="Profile", selected_icon=iconProfileActive),
            ft.NavigationBarDestination(icon=iconSettings, label="Settings", selected_icon=iconSettingsActive),
            # ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            # ft.NavigationBarDestination(icon=ft.icons.STORE, label="Store"),
            # ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Profile"),
            # ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ],
        selected_index=0,  # Default ke Home
        on_change=change_page,  # Panggil saat navigasi berubah
        bgcolor=ft.Colors.WHITE,
        elevation=65,
        indicator_color=ft.Colors.TRANSPARENT,
        # indicator_shape=ft.RoundedRectangleBorder(radius=50),
        # shadow_color=ft.Colors.BLUE
    )
