from fastapi.responses import JSONResponse


class Health:
    @staticmethod
    async def health_check():
        return JSONResponse({"status": "ok"}, status_code=200)
    
