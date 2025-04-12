from views.Product import ProductView
from views.Chat import ChatView
from views.Contact import ContactView

routes = [
    {"path": "/product/:id", "view": lambda page, route: ProductView(page, route.id)},
    {"path": "/chat/:id", "view": lambda page, route: ChatView(page, route.id)},
    {"path": "/contact/:id", "view": lambda page, route: ContactView(page, route.id)},
]
