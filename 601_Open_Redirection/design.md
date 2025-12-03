## Overview
Web authentication endpoint for user login with post-login redirection functionality.

## Endpoint Specification
URL: `/login`

Method: `POST`

## Request Format

### Form Data:

username: User login name (required)
password: User password (required)

### Query Parameters:

next: Redirect URL after successful login (optional, defaults to /)

## Implementation Details

* Processes authentication credentials
* Basic validation: checks if both username and password are provided
* No actual password verification (placeholder authentication)
* Extracts redirect URL from next query parameter
* Uses redirect() for post-login navigation
* Template rendered via render_template_string() with inline HTML
