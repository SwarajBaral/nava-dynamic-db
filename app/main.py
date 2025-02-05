from fastapi import FastAPI
from fastapi.responses import JSONResponse
from router import routes



app = FastAPI(
    title="Org dynamic db for navatech",
    docs_url="/docs",
    routes=routes,
    default_response_class=JSONResponse,
)

# TODO: move to separate controller
# @app.get("/health")
# def health_check():
#     return {"status": "ok"}

# @app.post("/org/create")
# async def create_organization(payload: OrganizationCreate, session: AsyncSession = Depends(get_master_db)):
#     """Create a new organization and its corresponding database."""
#     db_data = await create_organization_db(payload.organization_name, payload.password)
#     if "error" in db_data:
#         raise HTTPException(status_code=400, detail=db_data["error"])

#     new_org = await save_organization(session, payload.organization_name, payload.email, db_data)
#     if not new_org:
#         raise HTTPException(status_code=400, detail="Organization already exists")

#     return {"message": "Organization created successfully", "organization": payload.organization_name}

# @app.post("/org/get")
# async def get_organization(payload: OrgGetRequest, session: AsyncSession = Depends(get_master_db)):
#     """Get an organization by name."""
#     org = await get_organization_by_name(session, payload.organization_name)
#     if not org:
#         raise HTTPException(status_code=404, detail="Organization not found")
    
#     return {"id": org.id, "name": org.name, "db_name": org.db_name}


# @app.post("/admin/login", response_model=TokenResponse)
# async def admin_login(payload: AdminLoginRequest, session: AsyncSession = Depends(get_master_db)):
#     """Authenticate admin and return JWT token."""
#     token = await verify_admin_credentials(session, payload.admin, payload.password)
#     if not token:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     return {"access_token": token, "token_type": "bearer"}