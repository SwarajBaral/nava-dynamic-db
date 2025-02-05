from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from database import get_master_db
from dtos import AdminLoginRequest
from sqlalchemy.ext.asyncio import AsyncSession

from services import verify_admin_credentials


class Admin:
    @staticmethod
    async def admin_login(payload: AdminLoginRequest, session: AsyncSession = Depends(get_master_db)):
        """Authenticate admin and return JWT token."""
        token = await verify_admin_credentials(session, payload.admin, payload.password)
        if not token:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return JSONResponse({"access_token": token, "token_type": "bearer"}, status_code=200)