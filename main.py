import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.graph import Graph
from backend.classes.pydantic_models import ShoppingRequest


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)



@app.post("/run_graph")
async def run_graph(request: ShoppingRequest):

    graph = Graph(
        shoe_type=request.shoe_type,
        size=request.size,
        budget=request.budget,
        color=request.color
    )
    print("running graph")
    graph.run()
    print("graph run")

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

