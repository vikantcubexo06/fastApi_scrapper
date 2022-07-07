from pydantic import BaseModel


class ScrapperSerializer(BaseModel):
    registration_id: int
    Name: str = None
    Address: str = None
    Correspondence_Address: str = None
    Validity: str = None

