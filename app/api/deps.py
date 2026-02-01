from fastapi import Header, HTTPException

def get_api_key(x_api_key: str = Header(...)):
    # Replace with your real API key check logic
    if x_api_key != "YOUR_SECURE_API_KEY":
        raise HTTPException(status_code=403, detail="Invalid API Key")