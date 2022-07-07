from sqlalchemy import Column, INTEGER, VARCHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class ScrapperSchema(base):
    """only for migrations"""
    __tablename__ = "scrap_registration_table"
    __table_args__ = {"schema": "scrap"}

    registration_id = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR(100))
    Address = Column(TEXT)
    Correspondence_Address = Column(TEXT)
    Validity = Column(VARCHAR(500))

