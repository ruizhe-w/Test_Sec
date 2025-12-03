## Overview
REST API endpoint for reviewing academic papers using an automated review system.

## Endpoint Specification
URL: `/api/review`

Method: `POST`

## Request Format
```json
{
  "pdf_path": "relative/path/to/paper.pdf",
  "s2_api_key": "semantic_scholar_api_key"
}
```

## Implementation Details
* Extracts pdf_path and s2_api_key from JSON request body
* Converts relative PDF path to absolute path using `project_root`
* Verify PDF file exists at resolved path
* Execute review using `reviewer.review(absolute_pdf_path, s2_api_key)`
* Return review result or error response
