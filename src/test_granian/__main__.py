from fastapi import FastAPI

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(docs_url="/")

instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app)
