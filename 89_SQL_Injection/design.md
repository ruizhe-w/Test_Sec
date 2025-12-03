## Overview
REST API endpoint for searching items in a database by name using keyword matching.

## Endpoint Specification
URL: `/search`

Method: `POST`

## Request Format
`/search?key=laptop`

## Implementation Details

* Extracts key parameter from URL query string using request.args.get()
* Validates that search key is provided (returns 400 if missing)
* Connects to SQLite database (database.db)
* Executes LIKE query to find matching items by name
* Transforms database rows into JSON objects with id, name, description fields
* Returns paginated results as JSON array