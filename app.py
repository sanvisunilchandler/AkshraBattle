from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import uuid
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# -----------------------------
# QUESTIONS
# -----------------------------
QUESTIONS = [
    {
        "id": 1,
        "type": "mcq",
        "question": "Which of these is a swara (vowel)?",
        "options": ["ಕ", "ಅ", "ಗ", "ಟ"],
        "answerIndex": 1
    },
    {
        "id": 2,
        "type": "mcq",
        "question": "Which is a vyanjana (consonant)?",
        "options": ["ಅ", "ಆ", "ಕ", "ಈ"],
        "answerIndex": 2
    },
    {
        "id": 3,
        "type": "mcq",
        "question": "ಮ + ನ +ೆ = ?",
        "options": ["ಮನೆ", "ಮನು", "ಮಿನಿ", "ಮಣಿ"],
        "answerIndex": 0
    },
    {
        "id": 4,
        "type": "mcq",
        "question": "Sound of ಈ is…",
        "options": ["aa", "ee", "u", "ai"],
        "answerIndex": 1
    }
]

SESSIONS = {}

# -----------------------------
# API ROUTES
# -----------------------------

@app.route("/api/questions")
def get_questions():
    return jsonify(QUESTIONS)


@app.route("/api/session", methods=["POST"])
def create_session():
    data = request.json or {}
    mode = data.get("mode", "match")

    session_id = str(uuid.uuid4())[:6].upper()
    SESSIONS[session_id] = {
        "mode": mode,
        "players": {},
        "questions": QUESTIONS,
        "status": "waiting",
        "timeLimit": 30 if mode == "rush" else 60,
        "bossHealth": 200 if mode == "boss" else None
    }
    return jsonify({"sessionId": session_id})


@app.route("/api/session/<session_id>/join", methods=["POST"])
def join_session(session_id):
    data = request.json or {}
    name = data.get("name")
    avatar = data.get("avatar", "parrot")

    session = SESSIONS.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404

    if not name:
        return jsonify({"error": "Name required"}), 400

    player_id = str(uuid.uuid4())

    session["players"][player_id] = {
        "name": name,
        "avatar": avatar,
        "score": 0,
        "streak": 0,
        "coins": 0,
        "powerups": {"double": 1},
        "abilityUsed": False
    }

    return jsonify({"playerId": player_id})


@app.route("/api/session/<session_id>/answer", methods=["POST"])
def submit_answer(session_id):
    data = request.json or {}
    player_id = data.get("playerId")
    question_id = data.get("questionId")
    answer_index = data.get("answerIndex")
    use_double = data.get("useDouble", False)

    session = SESSIONS.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404

    player = session["players"].get(player_id)
    if not player:
        return jsonify({"error": "Player not found"}), 404

    question = next((q for q in session["questions"] if q["id"] == question_id), None)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    correct = (answer_index == question["answerIndex"])
    mode = session["mode"]

    if correct:
        base = 10

        if mode == "word":
            base = 15

        elif mode == "boss":
            base = 10
            session["bossHealth"] -= 10
            if session["bossHealth"] <= 0:
                session["status"] = "victory"

        elif mode == "mystery":
            base = 5
            player["coins"] += 5

        multiplier = 1
        if use_double and player["powerups"]["double"] > 0:
            player["powerups"]["double"] -= 1
            multiplier = 2

        player["streak"] += 1
        player["score"] += base * multiplier

    else:
        player["streak"] = 0

    return jsonify({
        "correct": correct,
        "score": player["score"],
        "streak": player["streak"],
        "coins": player.get("coins", 0),
        "bossHealth": session.get("bossHealth"),
        "mode": mode
    })


@app.route("/api/session/<session_id>/state")
def get_state(session_id):
    session = SESSIONS.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404

    players = [
        {
            "id": pid,
            "name": p["name"],
            "avatar": p["avatar"],
            "score": p["score"],
            "streak": p["streak"],
            "coins": p.get("coins", 0)
        }
        for pid, p in session["players"].items()
    ]
    players.sort(key=lambda x: x["score"], reverse=True)

    return jsonify({
        "mode": session["mode"],
        "players": players,
        "status": session["status"],
        "timeLimit": session["timeLimit"],
        "bossHealth": session.get("bossHealth")
    })


# -----------------------------
# SERVE FRONTEND
# -----------------------------
@app.route("/")
def serve_index():
    return send_from_directory("static", "static/index.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(debug=True)
