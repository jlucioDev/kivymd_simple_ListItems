from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDIcon
from data import data as ListItems
from kivymd.uix.list import OneLineAvatarIconListItem

KV = """

MDBoxLayout:
    orientation: "vertical"
    padding: 20
    MDTextField:
        id: txtSearch
        hint_text: "Pesquisar..."
        on_text: app.filter_text(txtSearch.text)
    ScrollView:
        MDList:
            id: box
                
"""


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.loadItems(ListItems)

    def loadItems(self, lst):
        for it in lst:
            # Criar um elemento da lista
            _it = OneLineAvatarIconListItem(
                text=it["text"],
                theme_text_color="Custom",
                text_color=(0.5, 0.5, 0.5, 1),

            )
            # Criar um ícone esquerdo
            _it.add_widget(MDIcon(
                icon=it["iconLeft"],
                size_hint=(None, None),
                size=(25, 25),
                pos_hint={"center_y": 0.5}
            )
            )
            _it.add_widget(MDIcon(
                icon=it["iconRight"],
                theme_text_color="Custom",
                text_color=(.7, .7, .7, 1),
                md_bg_color=(.95, .95, .95, 1),
                radius=8,
                size_hint=(None, None),
                size=(25, 25),
                pos_hint={"center_y": 0.5, "center_x": 0.95}

            )
            )

            self.root.ids.box.add_widget(_it)

    def filter_text(self, texto):
        ListItems_filter = []
        self.root.ids.box.clear_widgets()

        if texto != "":
            for it in ListItems:
                if texto.upper() in it["text"].upper():
                    ListItems_filter.append(it)
            if len(ListItems_filter) > 0:
                self.loadItems(ListItems_filter)
        else:
            self.loadItems(ListItems)


MainApp().run()
