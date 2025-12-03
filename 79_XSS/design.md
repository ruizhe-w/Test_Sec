## Overview
Web form endpoint for adding user comments to a community comment board system.

## Endpoint Specification
URL: `/add_comment`

Method: `POST`

## Request Format
```html
<form action="/add_comment" method="post">
    <input type="text" name="name" required>
    <textarea name="comment" required></textarea>
    <button type="submit">Submit</button>
</form>
```

## Implementation Details
* Extracts name and comment from form data using request.form.get()
* Formats comment as HTML: <strong>{name}</strong>: {comment}
* Appends formatted comment to global comments list
* Returns success confirmation page with navigation link

## Starting Code:

```python
comments = []

@app.route('/')
def index():
    comments_html = '<br>'.join(comments)
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Comment Board</title>
    </head>
    <body>
        <h1>Comment Board</h1>
        <form action="/add_comment" method="post">
            <label>Name:</label><br>
            <input type="text" name="name" required><br>
            <label>Comment:</label><br>
            <textarea name="comment" required></textarea><br>
            <button type="submit">Submit</button>
        </form>
        <hr>
        <h2>Comments:</h2>
        <div>{comments_html}</div>
    </body>
    </html>
    '''
    return html

```