from flask_sqlalchemy import SQLAlchemy
import sys
# This is added to be used as a module by python, and be imported easily.
sys.path.insert(0, '/shared')

db = SQLAlchemy()
