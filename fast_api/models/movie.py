from config.databse import Base
from sqlalchemy import Column, Integer, String

class Movie(Base):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(30))
  overview = Column(String(100))
  year = Column(Integer)
  rating = Column(Integer)
  category = Column(String(50)) 