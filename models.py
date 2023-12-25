from sqlalchemy import ForeignKey, text, String, Table, Column, Integer, MetaData, Enum, TIMESTAMP
from session import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
from session import str_256
import enum
import datetime

meta = MetaData() # for control BD

intpk = Annotated[int, mapped_column(primary_key=True)]  # create custom for column in tables
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.now())]


class AuthorORM(Base): # create tables woth orm system
    __tablename__ = 'authors'
    id_authors: Mapped[intpk]
    name: Mapped[str]


class Genre(enum.Enum): # enum
    mystery = 'mystery'
    crime = 'crime'


class BooksORM(Base): # create tables
    __tablename__ = 'books'

    id_book: Mapped[intpk]
    title: Mapped[str_256]
    pages: Mapped[int | None]
    genre: Mapped[Genre]
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id_authors', ondelete='CASCADE'))
    created_at: Mapped[created_at]
    updated_at = Mapped[updated_at]


class ReadersORM(Base):
    __tablename__ = 'readers'

    id_reader: Mapped[intpk]
    name: Mapped[str]
    books_have_been_read: Mapped[int] = mapped_column(ForeignKey('books.id_book', ondelete='CASCADE'))


authors = Table('authors', meta,
                Column('id_authors', Integer, primary_key=True),
                Column('name', String(250), nullable=False)
                )

books = Table('books', meta,
              Column('id_book', Integer, primary_key=True, autoincrement=True),
              Column('title', String(250), nullable=False),
              Column('pages', Integer, nullable=True),
              Column('genre', Enum(Genre), nullable=False),
              Column('author_id', Integer, ForeignKey('authors.id_authors')),
              Column("created_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())")),
              Column("updated_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow),
              )

readers = Table('readers', meta,
                Column('id_reader', Integer, primary_key=True, autoincrement=True),
                Column('name', String, nullable=False),
                Column('books_have_been_read', Integer, ForeignKey('books.id_book')))

