from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///db.sqlite3")
meta = MetaData()

connection = engine.connect()
