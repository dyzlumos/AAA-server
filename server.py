from flask import Flask, request, jsonify

app = Flask(__name__)

rooms = {}

@app.route("/create_room")
def create_room():
    room_id = str(len(rooms)+1)
    rooms[room_id] = {
        "players": [],
        "status": "waiting"
    }
    return jsonify({"room_id":room_id})

@app.route("/join_room")
def join_room():
    room_id = request.args.get("room_id")
    name = request.args.get("name")

    if room_id not in rooms:
        return jsonify({"msg":"room not exist"})

    # 如果已存在，不重复加入
    if name not in rooms[room_id]["players"]:
        rooms[room_id]["players"].append(name)

    return jsonify({"msg":"joined"})


@app.route("/room_info")
def room_info():
    room_id = request.args.get("room_id")
    return jsonify(rooms.get(room_id))

if __name__ == "__main__":
    print("服务器启动中...")
    app.run(host="0.0.0.0",port=5000)







