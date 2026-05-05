
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def obs(request:Request, call_next):
    start=time.time()
    res=await call_next(request)
    print({"latency":time.time()-start})
    return res

@app.get("/query")
def query(q:str):
    if "hack" in q:
        return {"fallback":"unsafe"}

    start=time.time()
    response = f"context answer for {q}"
    latency = time.time()-start

    return {"answer":response,"latency":latency}
