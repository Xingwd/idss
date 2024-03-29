# -*- coding: UTF-8 -*-
from main import create_app, db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
