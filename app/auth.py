from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

API_KEY_HEADER = APIKeyHeader(name="X-API-KEY", auto_error=False)


async def get_api_key(api_key_header: str = Security(API_KEY_HEADER)):
    if api_key_header == 'InnoSZTEch':
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )
