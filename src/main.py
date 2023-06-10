from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from src.auth.router import router as user_router
from src.record.router import router as audio_converter_router
from src.utils import create_folder

app = FastAPI(
    title='Test 2',
)

app.include_router(user_router)
app.include_router(audio_converter_router)


@app.on_event("startup")
async def startup_event():
    await create_folder()


@app.get('/', include_in_schema=False)
def read_root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get('/{path:path}', include_in_schema=False)
async def get_any(path: str):
    raise HTTPException(status_code=404, detail='Страница не найдена')
