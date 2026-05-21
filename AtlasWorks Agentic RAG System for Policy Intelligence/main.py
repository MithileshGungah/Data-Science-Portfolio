from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI(name="langgraph-ai-agent")

# Health check endpoint for service monitoring
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Application entry function
def main():
    print("Hello from rag-ai-agent!")

# Script execution entry point
if __name__ == "__main__":
    main()
