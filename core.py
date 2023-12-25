from databse import engine, async_engine
from models import authors, books, readers
from sqlalchemy import insert, select, update, text
from models import meta

class SyncCore:

    @staticmethod
    def create_tables():
        meta.drop_all(engine)
        meta.create_all(engine)

    @staticmethod
    def insert_authors():
        with engine.connect() as conn:
            stmt = insert(authors).values(
                [
                    {'name': 'Dima'},
                    {'name': 'Mark'}
                ]
            )
            conn.execute(stmt)
            conn.commit()

            
    @staticmethod   
    def select_authors():
        with engine.connect() as conn:
            query = select(authors) # SELECT * FROM authors
            result = conn.execute(query)
            # workers = result.scalars().all() # return only first object in list
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    def update_authors(author_id: int = 2, new_author: str = 'Dima'):
        with engine.connect() as conn:
            # stmt = text('UPDATE authors SET name=:name WHERE id_authors=:id')
            # stmt = stmt.bindparams(name=new_author, id=author_id)
            stmt = update(authors).values(name=new_author).filter_by(id_authors=author_id)  # where(authors.c.id==author_id)
            conn.execute(stmt)
            conn.commit()
    
    @staticmethod
    def insert_books():
        with engine.connect() as conn:
            stmt = insert(books).values([
                {'title': 'TEST2', 'pages': 327, 'genre': 'crime', 'author_id': 2}
            ])
            conn.execute(stmt)
            conn.commit()


    @staticmethod
    def create_reader():
        with engine.connect() as conn:
            stmt = insert(readers).values([
                {'name': 'Dima', 'books_have_been_read': 2}
            ])
            conn.execute(stmt)
            conn.commit()