from flask import request
from app import db, app
from app.database import Message


@app.route("/")
def show_msg():
    message = "<h1>Test</h1>"
    return message

@app.post("/messages")
def create_message():
    msg_data = request.json
    title = msg_data.get("title")   # Because we're using get, if the key isn't found
    body = msg_data.get("body")     # ... we'll get a NoneType as a result
    if not title or not body:
        return "<h1>Invalid Syntact</h1>", 400
    message = Message(title=title, body=body)
    db.session.add(message)
    db.session.commit()

@app.get("/messages")
def read_all_messages():
    return Message.query.all()
