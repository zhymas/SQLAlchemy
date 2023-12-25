from models import AuthorORM, BooksORM, Genre
from session import sync_session, async_session, Base
from sqlalchemy import select, and_
from databse import engine

class SyncORM:

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_data():
        with sync_session() as session: # session - work with ORM for insert data for BD
            author = AuthorORM(name='Dima')
            author1 = AuthorORM(name='Mark')
            session.add_all([author, author1])
            session.commit()

    @staticmethod
    async def insert_data_async():
        async with async_session() as session:
            worker = AuthorORM(name='Mark')
            session.add(worker)
            await session.commit()

    @staticmethod
    def select_author():
        with sync_session() as session:
            # author_id = 1
            # author = session.get(AuthorORM, author_id)
            query = select(AuthorORM)
            result = session.execute(query)
            authors = result.scalars().all()
            print(f'{authors=}')
            
    @staticmethod
    def update_author(author_id: int = 2, new_author: str = 'Mark'):
        with sync_session() as session:
            author = session.get(AuthorORM, author_id)
            author.name = new_author
            session.expire_all()
            session.refresh(author)
            session.commit()
    
    @staticmethod
    def insert_books():
        with sync_session() as session:
            book1 = BooksORM(title='Книга 1', pages=300, genre=Genre.mystery, author_id=1)
            book2 = BooksORM(title='Книга 2', pages=523, genre=Genre.crime, author_id=2)
            book3 = BooksORM(title='Книга 3', pages=127, genre=Genre.mystery, author_id=1)
            session.add_all([book1, book2, book3])
            session.commit()
    
    @staticmethod
    def select_books():
        with sync_session() as session: 
            query = (
                select(
                    BooksORM.title)
                    .filter(and_
                            (BooksORM.title.contains('1'), 
                             BooksORM.pages > 100, 
                             BooksORM.genre == Genre.mystery)) # contains = LIKE in sql language but without %
            )
            # print(query.compile(compile_kwargs={'literal_binds': True})) # return beatiuful request
            res = session.execute(query)
            print(res.all())
    
    