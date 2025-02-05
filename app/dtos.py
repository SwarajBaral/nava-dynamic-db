from pydantic import BaseModel, EmailStr

class OrganizationCreate(BaseModel):
    email: EmailStr
    password: str
    organization_name: str

class OrgGetRequest(BaseModel):
    organization_name: str

class AdminLoginRequest(BaseModel):
    admin: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str