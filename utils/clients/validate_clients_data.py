from fastapi import HTTPException
def validate_clients_data(clients: list):
    if clients is None:
        raise HTTPException(400, detail='Clients should be defined')
    for client in clients:
        if client.get('longitude') is None or client.get('latitude') is None:
            raise HTTPException(400, detail='latitude and longitude on clients should be defined')
        