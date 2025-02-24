import os
import json
import uuid
import asyncio
import redis
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends, Header, status, Form
from fastapi.security import OAuth2PasswordBearer
import jwt  # PyJWT for JWT handling


# Load environment variables
load_dotenv()

# Firebase credentials setup (only initialized if needed later)
# cred = credentials.Certificate("firebase.json")  # Replace with actual path
# firebase_admin.initialize_app(cred)

# JWT Secret Key
SECRET_KEY = os.getenv("JWT_SECRET", "tgp-paynet")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Redis connection
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

TOPICS = json.loads(os.getenv("TOPICS_JSON", "{}"))

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True
)

# Initialize FastAPI app
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")


def create_jwt_token(data: dict):
    """Generate JWT token with expiration."""
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


# def verify_firebase_token(id_token: str): # No longer used
#     """Verify Firebase ID Token."""
#     try:
#         decoded_token = auth.verify_id_token(id_token)
#         return decoded_token
#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid Firebase ID Token")


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


# ✅ Simplified Login API - Hardcoded Validation
@app.post("/api/login")
async def login(email: str = Form(...), password: str = Form(...)):
    """Hardcoded validation for test user. Returns JWT on success."""
    if email == "test@mail.com" and password == "password":
        user_id = "testuser"  # Assign a user ID (can be anything for now)
        jwt_token = create_jwt_token({"sub": user_id})
        return {"access_token": jwt_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )


# ✅ Middleware to Guard Routes
def get_current_user(token: str = Depends(oauth2_scheme)):
    """Verify JWT Token from request header."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# ✅ Secured API Routes
@app.get("/api/financial-inclusion")
async def call_service1(country: str, start_year: int, end_year: int, user: str = Depends(get_current_user)):
    return await publish_and_wait("ms1", {"country": country, "start_year": start_year, "end_year": end_year})


@app.get("/api/digital-payments")
async def call_service2(country: str, start_year: int, end_year: int, user: str = Depends(get_current_user)):
    return await publish_and_wait("ms2", {"country": country, "start_year": start_year, "end_year": end_year})


@app.get("/api/money-laundering-risk")
async def call_service3(country: str, start_year: int, end_year: int, user: str = Depends(get_current_user)):
    return await publish_and_wait("ms3", {"country": country, "start_year": start_year, "end_year": end_year})


@app.get("/api/unemployment-rate")
async def call_service4(country: str, start_year: int, end_year: int, user: str = Depends(get_current_user)):
    return await publish_and_wait("ms4", {"country": country, "start_year": start_year, "end_year": end_year})


@app.get("/api/gdp-growth")
async def call_service5(country: str, start_year: int, end_year: int):
    return await publish_and_wait("ms5", {"country": country, "start_year": start_year, "end_year": end_year})


@app.get("/health")
async def health_check():
  """
  Health check endpoint.

  Returns:
      dict: A dictionary containing the status of the application.
  """
  return {"status": "ok"}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
=======
async def call_service5(country: str, start_year: int, end_year: int, user: str = Depends(get_current_user)):
    return await publish_and_wait("ms5", {"country": country, "start_year": start_year, "end_year": end_year})
