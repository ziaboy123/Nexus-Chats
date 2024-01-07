from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase

main = Flask(__name__)
main.config["SECRET_KEY"] = "jhowqfljnh"
socketio = SocketIO(main)

rooms={
    "General": {"members": 0, "messages": []},
    "Sports": {"members": 0, "messages": []},
    "Music": {"members": 0, "messages": []},
    "Tech": {"members": 0, "messages": []},
    "Programming": {"members": 0, "messages": []},
    "Gaming": {"members": 0, "messages": []},
    "Development": {"members": 0, "messages": []}
    }

@main.route("/", methods=["POST", "GET"])
def decide():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("decide.html", error="Please enter a name.", code=code, name=name)

        if join != False and not code:
            return render_template("decide.html", error="Please enter a room code.", code=code, name=name)

        room=code
        if create != False:
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("decide.html", error="Room does not exist.", code=code, name=name)

        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template("decide.html")

@main.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("decide"))

    return render_template("space.html", code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return

    join_room(room)
    send({"name": name, "message": "has entered the space"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1


    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")

if __name__ == "__main__":
    socketio.run(main, debug=True, port=3485)
