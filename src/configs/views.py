from views.Home import HomeView
from views.Store import StoreView
from views.Profile import ProfileView
from views.Settings import SettingsView
# from views.Contact import ContactView

def get_views(page):
    return [
        HomeView(page),
        StoreView(page),
        ProfileView(page),
        SettingsView(page),
        # ContactView(page),
    ]
