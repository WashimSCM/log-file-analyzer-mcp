
import os
import httpx
from mcp.server.fastmcp import FastMCP
app = mcp.streamable_http_app(     host="0.0.0.0" )

API_BASE_URL = os.getenv(
    "LOG_ANALYZER_API_URL",
    "https://log-file-analyzer-actions.onrender.com"
).rstrip("/")

mcp = FastMCP("Log File Analyzer")


@mcp.tool()
async def analyze_googlebot_logs(
    log_content: str,
    filename: str = "uploaded.log",
    verify_googlebot_dns: bool = False,
    top_n: int = 100
) -> dict:
    """Analyze Apache/Nginx combined access logs and report Googlebot crawl hits grouped by HTTP referrer URL, with counts and percentages."""
    if not log_content.strip():
        raise ValueError("log_content must not be empty")
    if not 1 <= top_n <= 1000:
        raise ValueError("top_n must be between 1 and 1000")

    payload = {
        "log_content": log_content,
        "filename": filename,
        "verify_googlebot_dns": verify_googlebot_dns,
        "top_n": top_n
    }

    async with httpx.AsyncClient(timeout=180.0) as client:
        response = await client.post(
            f"{API_BASE_URL}/analyze-logs",
            json=payload
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def check_log_analyzer_health() -> dict:
    """Check whether the Log File Analyzer backend is available."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.get(f"{API_BASE_URL}/health")
        response.raise_for_status()
        return response.json()


security = TransportSecuritySettings(
    allowed_hosts=[
        "log-file-analyzer-mcp.onrender.com",
        "log-file-analyzer-mcp.onrender.com:*"
    ]
)

app = mcp.streamable_http_app(
    transport_security=security
)
