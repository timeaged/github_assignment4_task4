from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["todo_database"]
collection = db["todos"]


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form["itemName"]
    item_description = request.form["itemDescription"]

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return "To-Do item submitted successfully"


if __name__ == "__main__":
    app.run()