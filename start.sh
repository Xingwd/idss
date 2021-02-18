#!/bin/bash

source activate seer
export FLASK_APP=backend/seer.py
export FLASK_ENV=development
flask run

