from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy import func
from database import Base


class Question(Base):
    __tablename__ = 'entity'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, unique=True)
    text = Column(String(500))
    answer = Column(String(50))
    publish_date = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    def __repr__(self):
        return "<Question('%d', '%s', '%s')>" % (self.question_id,
                                                 self.text,
                                                 self.answer)