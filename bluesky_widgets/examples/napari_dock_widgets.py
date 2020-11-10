import napari
import numpy as np

from bluesky_widgets.components.search.searches import SearchList
from bluesky_widgets.qt.searches import QtSearches
from bluesky_widgets.examples.utils.add_search_mixin import AddSearchMixin
from bluesky_widgets.examples.utils.generate_msgpack_data import get_catalog
from bluesky_widgets.examples.qt_search import Searches, SearchesWidget
from qtpy.QtWidgets import QPushButton, QWidget, QVBoxLayout
from bluesky_widgets.utils.event import EmitterGroup, Event

class Viewer(napari.Viewer, AddSearchMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.searches = SearchList()
        # Add a button that does something with the currently-selected Runs
        # when you click it.
        #self.go_button = QPushButton("LOAD RANDOM IMAGE", self.window.qt_viewer)
        #self.go_button.clicked.connect(self.on_process)
        #self.window.add_dock_widget(self.go_button, area="left")
        #self.events.add(process=Event)
        #self.model.events.process.connect(lambda e: go_button.setVisible(False))
    
    def on_process(self):
        image = np.random.rand(200, 200)
        self.add_image(image)

with napari.gui_qt():
    viewer = Viewer()
    viewer.grid_view()  # Place images side by side, not stacked.
    viewer.window.add_dock_widget(SearchesWidget((Searches())), area="right")
    viewer.add_search(get_catalog())
    # ...and one listing any and all catalogs discovered on the system.
    from databroker import catalog
    viewer.add_search(catalog)
    #viewer.add_image(np.random.rand(100,100))
