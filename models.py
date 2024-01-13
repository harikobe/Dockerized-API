from sqlalchemy import Column,DateTime,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base #used to specify our fields
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func #used for the time updates

Base = declarative_base() #define our tables (eg.onupdate=func.now())


class Book(Base):
     __tablename__="book"
     id = Column(Integer, primary_key=True, index=True)
     title = Column(String)
     rating = Column(Integer)
     time_created = Column(DateTime(timezone=True), server_default=func.now())
     time_updated = Column(DateTime(timezone=True), onupdate=func.now())
     author_id = Column(Integer, ForeignKey("author.id"))

     author = relationship("Author")
  

class Author(Base):
     __tablename__="author"
     id=Column(Integer,primary_key=True)
     name=Column(String)
     age= Column(Integer)
     time_created=Column(DateTime(timezone=True),server_default=func.now())
     time_updated=Column(DateTime(timezone=True),onupdate=func.now())
