

from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from controller.health import Health as HealthController
from controller.organization import Organization as OrganizationController
from controller.admin import Admin as AdminController

routes: list[APIRoute] = [
        # Health Check
        APIRoute(
            "/health",
            methods=["GET"],
            endpoint=HealthController.health_check,
            response_class=JSONResponse,
            summary="Check if the API is running",
            description="Simple health check endpoint to verify that the API is operational.",
        ),

        # Organization Routes
        APIRoute(
            "/org/create",
            methods=["POST"],
            endpoint=OrganizationController.create_organization,
            response_class=JSONResponse,
            summary="Create a new organization",
            description="Creates a new organization, sets up a database, and stores organization metadata.",
        ),
        APIRoute(
            "/org/get",
            methods=["POST"],
            endpoint=OrganizationController.get_organization_by_name,
            response_class=JSONResponse,
            summary="Retrieve an organization by name",
            description="Fetch an organization's details using its name.",
        ),

        # Admin Routes
        APIRoute(
            "/admin/login",
            methods=["POST"],
            endpoint=AdminController.admin_login,
            response_class=JSONResponse,
            summary="Admin login",
            description="Authenticate an admin user and return a JWT token.",
        ),
    ]