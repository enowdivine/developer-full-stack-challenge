from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///db.sqlite3")
meta = MetaData()
meta.create_all(engine)

connection = engine.raw_connection()
