from sqlalchemy import Column, DateTime, Integer, String, func

from database import Base


class Question(Base):
    __tablename__ = "entity"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, unique=True)
    text = Column(String(500))
    answer = Column(String(250))
    publish_date = Column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )

    def __repr__(self):
        return "<Question('%d', '%s', '%s')>" % (
            self.question_id,
            self.text,
            self.answer,
        )
