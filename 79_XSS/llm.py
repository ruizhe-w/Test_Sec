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

@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name', '')
    comment = request.form.get('comment', '')

    comments.append(f'<strong>{name}</strong>: {comment}')
    return '''
    <html>
    <body>
        <p>Comment added!</p>
        <a href="/">Back to comments</a>
    </body>
    </html>
    '''