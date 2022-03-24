from flask import Flask, jsonify
from app import boards, cards, statuses


app = Flask(__name__)


@app.get("/")
def index():
    bs = boards.get_all()
    for i, b in enumerate(bs):
        bs[i]["statuses"] = statuses.get_all()
        for j, s in enumerate(bs[i]["statuses"]):
            bs[i]["statuses"][j]["cards"] = cards.get_by_board_and_status(
                b.get("id"), s.get("id")
            )
    return jsonify(bs)
