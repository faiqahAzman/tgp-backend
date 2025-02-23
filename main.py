import os
import json
import uuid
import asyncio
import redis
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

# Load topics from ENV (JSON format)
TOPICS = json.loads(os.getenv("TOPICS_JSON", "{}"))

# Initialize Redis connection
redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True
)

# Initialize FastAPI app
app = FastAPI()


async def wait_for_response(request_id: str, timeout: int = 5):
    """Wait asynchronously for a response from Redis."""
    start_time = asyncio.get_event_loop().time()
    response_key = f"response:{request_id}"

    while asyncio.get_event_loop().time() - start_time < timeout:
        response = redis_client.get(response_key)
        if response:
            redis_client.delete(response_key)  # Cleanup after reading
            return json.loads(response)
        await asyncio.sleep(0.1)  # Non-blocking wait

    raise HTTPException(status_code=504, detail="Timeout waiting for response")


async def publish_and_wait(service_name: str, payload: dict):
    """Publish request to a microservice and wait for a response."""
    if service_name not in TOPICS:
        raise HTTPException(status_code=400, detail=f"Service {service_name} not found")

    request_id = str(uuid.uuid4())
    payload["request_id"] = request_id

    request_topic = TOPICS[service_name]["request"]
    redis_client.publish(request_topic, json.dumps(payload))

    return await wait_for_response(request_id)


# TODO: Implement API routes to call microservices
@app.get("/api/ms1")
async def call_service1(param1: str):
    return await publish_and_wait("ms1", {"param1": param1})


# TODO: Implement API routes to call microservices
@app.get("/api/ms2")
async def call_service2(param1: str, param2: str):
    return await publish_and_wait("ms2", {"param1": param1, "param2": param2})


# TODO: Implement API routes to call microservices
@app.get("/api/ms3")
async def call_service3(param1: str, param2: int, param3: bool):
    return await publish_and_wait("ms3", {"param1": param1, "param2": param2, "param3": param3})


# TODO: Implement API routes to call microservices
@app.get("/api/ms4")
async def call_service4(param1: str, param2: str, param3: str):
    return await publish_and_wait("ms4", {"param1": param1, "param2": param2, "param3": param3})


# TODO: Implement API routes to call microservices
@app.get("/api/ms5")
async def call_service5(param1: str):
    return await publish_and_wait("ms5", {"param1": param1})
