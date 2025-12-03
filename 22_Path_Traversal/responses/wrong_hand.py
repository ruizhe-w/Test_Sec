@app.route("/api/review", methods=["POST"])
def review_paper():
    pdf_path = request.json.get("pdf_path") # checks here omitted
    s2_api_key = request.json.get("s2_api_key") # checks here omitted

    path = os.path.join(project_root, pdf_path)

    review_result = reviewer.review(path, request.json.get("s2_api_key"))
    return jsonify({"review": review_result}), 200
