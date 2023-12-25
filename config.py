# from databse import engine, async_engine
# from session import Base
# from core import meta

# meta = MetaData() # Base class for control BD

# def create_tables():
#     meta.drop_all(engine)
#     meta.create_all(engine)



# def insert_data():
#     with engine.connect() as conn:
#         # stmt = """INSERT INTO authors (id_authors, name) VALUES ('1', 'Dima');"""
#         stmt = insert(authors).values([
#             {'name': 'Mark'},
#             {'name': 'Pasha '}
#         ])
#         conn.execute(stmt)
#         conn.commit()