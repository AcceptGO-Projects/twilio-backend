from fastapi.openapi.utils import get_openapi
from app.main import app
import json

with open('openapi.json', 'w') as f:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
        ),
        f
    )
