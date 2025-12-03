@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple authentication check (replace with real authentication)
        if username and password:
            next_url = request.args.get('next', '/')
            return redirect(next_url)
    
    return 'Logged in successfully!'