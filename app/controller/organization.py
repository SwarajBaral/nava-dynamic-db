from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from database import get_master_db
from dtos import OrgGetRequest, OrganizationCreate
from services import create_organization_db, get_organization_by_name, save_organization
from sqlalchemy.ext.asyncio import AsyncSession


class Organization:
    @staticmethod
    async def get_organization_by_name(payload: OrgGetRequest, session: AsyncSession = Depends(get_master_db)):
        """Get an organization by name."""
        org = await get_organization_by_name(session, payload.organization_name)
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
        
        return JSONResponse({"id": org.id, "name": org.name, "db_name": org.db_name}, status_code=200)
    
    @staticmethod
    async def create_organization(payload: OrganizationCreate, session: AsyncSession = Depends(get_master_db)):
        """Create a new organization and its corresponding database."""
        db_data = await create_organization_db(payload.organization_name, payload.password)
        if "error" in db_data:
            raise HTTPException(status_code=400, detail=db_data["error"])

        new_org = await save_organization(session, payload.organization_name, payload.email, db_data)
        if not new_org:
            raise HTTPException(status_code=400, detail="Organization already exists")

        return JSONResponse({"message": "Organization created successfully", "organization": payload.organization_name}, status_code=200)