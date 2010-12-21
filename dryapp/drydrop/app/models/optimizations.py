# -*- mode: python; coding: utf-8 -*-
import logging
import google.appengine.ext.db as db
from drydrop.app.core.model import Model

class Optimizations(db.Expando, Model):
    expires_js=db.BooleanProperty()
    expires_css=db.BooleanProperty()
    version = db.IntegerProperty(default=1)
    domain = db.StringProperty()
    last_updated = db.DateTimeProperty()
