import os
import sys

# Template untuk navigasi biasa
NAV_VIEW_TEMPLATE = '''import flet as ft

def {name}View(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("{title} Page", size=20, font_family="Inter-ExtraBold"),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=False,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,
    )
'''

# Template untuk stack view (pakai CustomAppBar, route, SafeArea)
STACK_VIEW_TEMPLATE = '''import flet as ft
from components.CustomAppBar import CustomAppBar

def {name}View(page: ft.Page, id):
    container = ft.Container(
        content=ft.Column(
            [
                ft.Text("{title} Page", size=20, font_family="Inter-ExtraBold"),
            ], 
            scroll=ft.ScrollMode.AUTO, 
            expand=True
        ),
        visible=True,
        expand=True,
        padding=0,
        alignment=ft.alignment.center,
    )

    return ft.View(
        route=f"/{route}/{{id}}",
        controls=[
            CustomAppBar(title="{title}"),
            ft.SafeArea(container)
        ],
        padding=20,
    )
'''

# === COMPONENT TEMPLATES ===
CLASS_COMPONENT_TEMPLATE = '''import flet as ft

class {name}(ft.Text):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
'''

FUNCTION_COMPONENT_TEMPLATE = '''import flet as ft

def {name}(text: str):
    return ft.Text(
        text=text
    )
'''

# === VIEW GENERATOR ===
def create_view(view_name, use_stack=False):
    os.makedirs("src/views", exist_ok=True)

    filename = f"src/views/{view_name}.py"
    title = view_name.replace('_', ' ').title()
    route = view_name.lower()

    template = STACK_VIEW_TEMPLATE if use_stack else NAV_VIEW_TEMPLATE

    with open(filename, "w") as f:
        f.write(template.format(name=view_name, title=title, route=route))

    print(f"✅ View '{filename}' berhasil dibuat.")


# === COMPONENT GENERATOR ===
def create_component(name, use_function=False):
    os.makedirs("src/components", exist_ok=True)
    filename = f"src/components/{name}.py"
    template = FUNCTION_COMPONENT_TEMPLATE if use_function else CLASS_COMPONENT_TEMPLATE

    with open(filename, "w") as f:
        f.write(template.format(name=name))

    tipe = "Function" if use_function else "Class"
    print(f"✅ {tipe} Component '{filename}' berhasil dibuat.")



# === COMMAND PARSER ===
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python fletcli.py make:view ViewName [--stack]")
        print("  python fletcli.py make:component ComponentName [--function]")
        sys.exit()

    command = sys.argv[1]
    name = sys.argv[2]
    is_flagged = "--stack" in sys.argv or "--function" in sys.argv

    if command == "make:view":
        create_view(name, use_stack="--stack" in sys.argv)
    elif command == "make:component":
        create_component(name, use_function="--function" in sys.argv)
    else:
        print("🚫 Unknown command.")
