@app.route("/api/review", methods=["POST"])
def review_paper() -> Union[Response, tuple[Response, int]]:
    """Review a paper using the Reviewer class"""
 
    data = request.json
 
    pdf_path = data.get("pdf_path") # checks here omitted
    s2_api_key = data.get("s2_api_key") # checks here omitted
 
    try:
        absolute_pdf_path = os.path.join(project_root, pdf_path) 
        print(f"Reviewing paper at: {absolute_pdf_path}")
 
        # Check if file exists
        if not os.path.exists(absolute_pdf_path):
            return jsonify({"error": f"PDF file not found: {absolute_pdf_path}"}), 404
 
        # Call review() to get a single review
        review_result = reviewer.review(absolute_pdf_path, s2_api_key)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
