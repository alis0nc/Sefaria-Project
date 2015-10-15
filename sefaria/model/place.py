
import geojson
from . import abstract as abst
from . import schema


import logging
logger = logging.getLogger(__name__)

class Place(abst.AbstractMongoRecord):
    """
    Homo Sapiens
    """
    collection = 'place'
    track_pkeys = True
    pkeys = ["key"]

    required_attrs = [
        "key"
        "names"
        "loc"
    ]
    optional_attrs = []

    # Names
    # This is the same as on TimePeriod, and very similar to Terms & Person - abstract out
    def _init_defaults(self):
        self.name_group = None

    def _set_derived_attributes(self):
        self.name_group = schema.TitleGroup(getattr(self, "names", None))

    def all_names(self, lang=None):
        return self.name_group.all_titles(lang)

    def primary_name(self, lang=None):
        return self.name_group.primary_title(lang)

    def secondary_names(self, lang=None):
        return self.name_group.secondary_titles(lang)

    def set_location(self, lat, lon):
        # Currently assuming point location
        self.loc = geojson.Point((lat, lon))