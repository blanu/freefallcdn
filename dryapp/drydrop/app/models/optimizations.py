# -*- mode: python; coding: utf-8 -*-
import logging
import google.appengine.ext.db as db
from drydrop.app.core.model import Model

class Optimizations(db.Expando, Model):
    minify_html=db.BooleanProperty()
    expires_js=db.BooleanProperty()
    minify_js=db.BooleanProperty()
    expires_css=db.BooleanProperty()
    minify_css=db.BooleanProperty()
    expires_images=db.BooleanProperty()
    smush_png=db.BooleanProperty()
    smush_jpg=db.BooleanProperty()
    version = db.IntegerProperty(default=1)
    domain = db.StringProperty()
    last_updated = db.DateTimeProperty()
