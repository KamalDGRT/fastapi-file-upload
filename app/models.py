# Every model represents a table in our database.


from app.database import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


from app.database import Base

class FileDetail(Base):
    __tablename__ = "file_detail"

    file_id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(length=200), index=True, nullable=False)
    uploaded_at = Column(TIMESTAMP(
        timezone=True),
        nullable=False,
        server_default=text('now()')
    )
