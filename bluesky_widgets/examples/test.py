import napari
from qtpy.QtWidgets import QPushButton, QWidget, QVBoxLayout
from bluesky_widgets.components.search.searches import SearchList, Search
from bluesky_widgets.qt.searches import QtSearches
from bluesky_widgets.examples.utils.add_search_mixin import headings, extract_results_row_from_run
from bluesky_widgets.examples.utils.generate_msgpack_data import get_catalog

class ThingModel:
    def __init__(self, search_list_model, button_text):
        self.button_text = "hello"
        self.search_list_model = search_list_model

class QThing(QWidget):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.setLayout(layout)
        button = QPushButton(model.button_text)
        button.clicked.connect(lambda: print(model.button_text))
        layout.addWidget(QtSearches(model.search_list_model))
        layout.addWidget(button)




def add_search(searches, catalog):
    """
    Add a new Search form.
    """
    search = Search(catalog, columns=(headings, extract_results_row_from_run))
    searches.append(search)
with napari.gui_qt():
    viewer = napari.Viewer()
    search_list_model = SearchList()
    add_search(search_list_model, get_catalog())
    model = ThingModel(search_list_model, "hello")
    viewer.window.add_dock_widget(QThing(model))
