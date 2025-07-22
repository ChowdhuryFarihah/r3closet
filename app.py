from flask import Flask, render_template, request, jsonify
from closet_prototype_implementation import add_to_closet, hard_search_closet
import json
app = Flask(__name__)

@app.route('/submitTags', methods=['POST'])
def search_for_tags():
    closet = {}
    tags = request.get_json()
    return hard_search_closet(closet, tags)