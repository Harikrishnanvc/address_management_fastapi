import sqlalchemy.exc
from fastapi import FastAPI, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session

from database_connection import get_db, db
from models import Address
from schemas import AddressSchema, AddressUpdateSchema
from geopy.distance import geodesic
app = FastAPI()


@app.post("/register-address/")
async def register_address(address: AddressSchema, db: Session = Depends(get_db)):
    db_address = Address(country=address.country, state=address.state, city=address.city,
                         postal_code=address.postal_code, latitude=address.latitude,
                         longitude=address.longitude)
    db.add(db_address)
    db.commit()
    response = {'status': status.HTTP_201_CREATED,
                'message': 'Address added successfully'}
    return response


@app.get("/get-address/")
async def get_address(db: Session = Depends(get_db)):
    address_data = db.query(Address).all()
    db.close()
    response = {'status': status.HTTP_201_CREATED,
                'data': address_data}
    return response


@app.get("/get-address-by-id/")
async def get_address_by_id(id: int):
    try:
        address_data = db.query(Address).filter(Address.id == id).first()
        db.close()
        response = {'status': status.HTTP_201_CREATED,
                    'data': address_data}
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Address not found")


@app.patch("/update-address/{id}")
async def update_address(id: int, update_address: AddressUpdateSchema):
    try:
        address_data = db.query(Address).filter(Address.id == id).first()
        for field, value in update_address.dict().items():
            if value is not None:
                setattr(address_data, field, value)
            else:
                setattr(address_data, field, getattr(address_data, field))
        db.commit()
        db.refresh(address_data)
        db.close()
        response = {'status': status.HTTP_201_CREATED,
                    'data': address_data}
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Address not found")


@app.delete("/delete-address/{id}")
async def delete_address(id: int):
    try:
        address_data = db.query(Address).filter(Address.id == id).first()
        db.delete(address_data)
        db.commit()
        db.close()
        response = {'status': status.HTTP_200_OK,
                    'message': 'Address deleted successfully'}
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Address not found")


@app.get("/addresses/nearby/")
async def get_addresses_nearby(
    latitude: float = Query(..., title="Latitude of the location"),
    longitude: float = Query(..., title="Longitude of the location"),
    distance: float = Query(..., title="Distance in kilometers")
):
    try:
        coordinates = (latitude, longitude)
        max_coordinates = geodesic(kilometers=distance).destination(coordinates, 45)
        max_lat = max(coordinates[0], max_coordinates[0])
        max_lon = max(coordinates[1], max_coordinates[1])

        # Calculate the minimum latitude and longitude values
        min_coordinates = geodesic(kilometers=distance).destination(coordinates, 225)
        min_lat = min(coordinates[0], min_coordinates[0])
        min_lon = min(coordinates[1], min_coordinates[1])

        nearby_addresses = (
            db.query(Address)
            .filter(Address.latitude >= min_lat, Address.latitude <= max_lat)
            .filter(Address.longitude >= min_lon, Address.longitude <= max_lon)
            .all()
        )
        return nearby_addresses
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving nearby addresses")
