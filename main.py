from flask import Flask, request, jsonify
from tempfile import NamedTemporaryFile
from generate_recipe import generate_recipe_from_image, generate_recipe_description_from_search, \
    generate_random_recipe_description

app = Flask(__name__)

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

@app.route('/recipe/from_image', methods=['POST'])
def generate_recipe_from_image_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    with NamedTemporaryFile(delete=False) as temp_file:
        image.save(temp_file.name)
        recipe = generate_recipe_from_image(image_path=temp_file.name, safety_settings=safety_settings)
    return jsonify(recipe)

@app.route('/recipe/from_search', methods=['POST'])
def generate_recipe_from_search_route():
    search_query = request.form.get('search_query')
    if not search_query:
        return jsonify({'error': 'No search query provided'}), 400

    recipe = generate_recipe_description_from_search(search_query=search_query, safety_settings=safety_settings)
    return jsonify(recipe)

@app.route('/recipe/random', methods=['GET'])
def generate_random_recipe_route():
    try:
        recipe = generate_random_recipe_description(safety_settings)  # This function needs to be defined to return a random recipe
        return jsonify(recipe)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# if __name__ == '__main__':
#     app.run(debug=True)
