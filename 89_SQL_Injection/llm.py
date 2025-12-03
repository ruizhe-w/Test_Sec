@app.route('/search', methods=['GET'])
def search():
    key = request.args.get('key', '')
    
    if not key:
        return jsonify({'error': 'No search key provided'}), 400
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Search for items matching the key
    query = f"SELECT * FROM items WHERE name LIKE {key}"
    c.execute(query)
    
    results = c.fetchall()
    conn.close()
    
    items = [{'id': row[0], 'name': row[1], 'description': row[2]} for row in results]
    
    return jsonify({'results': items})

