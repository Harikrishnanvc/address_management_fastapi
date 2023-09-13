
# Address Management Using FastAPI

This is an Address Book Application built with FastAPI and SQLAlchemy that allows API users to create, update, delete, and retrieve addresses. Each address contains coordinates and is stored in an SQLite database. Additionally, the application provides the ability to retrieve addresses within a given distance from specific location coordinates.

## Features

- Create a new address with coordinates.
- Update an existing address.
- Delete an address.
- Retrieve all addresses.
- Retrieve addresses within a given distance from location coordinates.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- SQLite (or any other compatible relational database)



## Installation
Clone the repository:

   ```bash
   git clone https://github.com/Harikrishnanvc/address_management_fastapi.git

Install the requirements

```bash
pip install -r requirements.txt
```

## API Reference

Registers a new address with the provided details.

- **URL**: `/register-address/`
- **Method**: POST
- **Request Body**: `AddressSchema`
- **Response**:
  - Status: 201 Created
  - Message: "Address added successfully"

### Get All Addresses [GET]

Retrieves a list of all addresses stored in the database.

- **URL**: `/get-address/`
- **Method**: GET
- **Response**:
  - Status: 200 OK
  - Data: List of addresses in `Address` format

### Get Address by ID [GET]

Retrieves an address by its unique ID.

- **URL**: `/get-address-by-id/{id}`
- **Method**: GET
- **Path Parameter**: `id` (int) - The ID of the address to retrieve.
- **Response**:
  - Status: 200 OK
  - Data: Address in `Address` format

### Update Address [PATCH]

Updates an existing address with the provided data.

- **URL**: `/update-address/{id}`
- **Method**: PATCH
- **Path Parameter**: `id` (int) - The ID of the address to update.
- **Request Body**: `AddressUpdateSchema`
- **Response**:
  - Status: 200 OK
  - Data: Updated address in `Address` format

### Delete Address [DELETE]

Deletes an address by its unique ID.

- **URL**: `/delete-address/{id}`
- **Method**: DELETE
- **Path Parameter**: `id` (int) - The ID of the address to delete.
- **Response**:
  - Status: 200 OK
  - Message: "Address deleted successfully"

### Get Addresses Nearby [GET]

Retrieves addresses within a given distance from specific location coordinates.

- **URL**: `/addresses/nearby/`
- **Method**: GET
- **Query Parameters**:
  - `latitude` (float) - Latitude of the location.
  - `longitude` (float) - Longitude of the location.
  - `distance` (float) - Distance in kilometers to search within.
- **Response**:
  - Status: 200 OK
  - Data: List of addresses in `Address` format that are within the specified distance from the provided coordinates.