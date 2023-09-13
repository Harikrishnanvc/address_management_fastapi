from pydantic import BaseModel


class AddressSchema(BaseModel):
    country: str
    state: str
    city: str
    postal_code: int
    latitude: float
    longitude: float


class AddressUpdateSchema(BaseModel):
    country: str = None
    state: str = None
    city: str = None
    postal_code: int = None
    latitude: float = None
    longitude: float = None
