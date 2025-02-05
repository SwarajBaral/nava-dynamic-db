from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from utils import generate_secure_password
from constants import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from models import Organization, AdminUser
from sqlalchemy.future import select
from config import settings
import asyncpg
from jose import jwt
from datetime import datetime, timedelta, timezone
import bcrypt

async def create_organization_db(org_name: str, password: str):
    """Create a new database dynamically for the organization."""
    db_name = f"{org_name.lower().replace(' ', '_')}_db"
    db_user = f"{org_name.lower().replace(' ', '_')}_user"
    db_password = generate_secure_password(password)

    try:
        conn = await asyncpg.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database="postgres"
        )
        await conn.execute(f"CREATE DATABASE {db_name}")
        await conn.execute(f"CREATE USER {db_user} WITH PASSWORD '{db_password}'")
        await conn.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user}")
        await conn.close()
    except Exception as e:
        return {"error": str(e)}

    return {"db_name": db_name, "db_user": db_user, "db_password": password}

async def save_organization(session: AsyncSession, org_name: str, org_email: EmailStr, db_data: dict):
    """Save organization details in the master database."""
    try:
        new_org = Organization(
            name=org_name,
            db_name=db_data["db_name"],
            db_user=db_data["db_user"],
            db_password=generate_secure_password(db_data["db_password"])
        )
        session.add(new_org)
        await session.commit()
        admin_user = AdminUser(
            org_id=new_org.id,
            username=org_email,
            hashed_password=generate_secure_password(db_data["db_password"])
        )
        session.add(admin_user)
        await session.commit()
        return new_org
    except IntegrityError:
        await session.rollback()
        return None

async def get_organization_by_name(session: AsyncSession, org_name: str):
    """Fetch an organization by name."""
    result = await session.execute(select(Organization).where(Organization.name == org_name))
    org = result.scalars().first()
    return org

async def verify_admin_credentials(session: AsyncSession, username: str, password: str):
    """Verify admin credentials and return JWT token."""
    result = await session.execute(select(AdminUser).where(AdminUser.username == username))
    admin_user = result.scalars().first()
    if not admin_user or not bcrypt.checkpw(password.encode(), admin_user.hashed_password.encode()):
        return None
    
    token_data = {"user": admin_user.username, "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return access_token