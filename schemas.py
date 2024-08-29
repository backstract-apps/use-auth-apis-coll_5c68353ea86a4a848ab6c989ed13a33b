from pydantic import BaseModel

class CreatePersonsSchema(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str


class ReadPersonsSchema(BaseModel):
    rollnumber: int
    fullname: str
    age: int
    profession: str
    class Config:
        from_attributes = True


