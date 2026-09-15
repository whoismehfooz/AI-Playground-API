from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import (
                                            AIServiceError,
                                            AIServiceTimeoutError,
                                            AIServiceConnectionError,AIServiceProviderError,AIServiceRateLimitError)



def register_exception_handlers(app:FastAPI):

    @app.exception_handler(AIServiceTimeoutError)
    async def ai_timeout_handler(
        req:Request,
        exc:AIServiceTimeoutError):

        return JSONResponse(
            status_code=504,
            content={"detail":exc.message}
        )

    @app.exception_handler(AIServiceRateLimitError)
    async def ai_rate_limit_handler(
        req:Request,
        exc:AIServiceRateLimitError):

        return JSONResponse(
            status_code=429,
            content={"detail":exc.message}
        )

    @app.exception_handler(AIServiceConnectionError)
    async def ai_connection_handler(
        req:Request,
        exc:AIServiceConnectionError):

        return JSONResponse(
            status_code=502,
            content={"detail":exc.message}
        )

    @app.exception_handler(AIServiceProviderError)
    async def ai_provider_handler(
        req:Request,
        exc:AIServiceProviderError):

        return JSONResponse(
            status_code=502,
            content={"detail":exc.message}
        )