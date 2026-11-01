
# Log File Analyzer MCP Connector

This MCP server connects ChatGPT to the existing Log File Analyzer API.

## Existing API

https://log-file-analyzer-actions.onrender.com

## Deployment on Render

1. Create a new Render Web Service using this GitHub repository.
2. Select Docker as the runtime.
3. Add this environment variable:

   LOG_ANALYZER_API_URL=https://log-file-analyzer-actions.onrender.com

4. Deploy the service.

## MCP Endpoint

https://YOUR-RENDER-SERVICE.onrender.com/mcp

Replace YOUR-RENDER-SERVICE with your actual Render service name.

## Available Tools

- analyze_googlebot_logs
- check_log_analyzer_health

## Analysis Features

- Apache and Nginx access log analysis
- Googlebot crawl hit counts
- Referrer URL counts and percentages
- Referrer proportion visualization
- Results table

## Security

The existing API and connector do not add authentication or rate limiting. Avoid submitting confidential logs until access controls are added.
