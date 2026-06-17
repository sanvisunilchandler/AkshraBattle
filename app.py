from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import uuid
import random


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
    },

    # ---- NEW QUESTIONS START HERE ----

    {
        "id": 5,
        "type": "mcq",
        "question": "Which of these is a swara?",
        "options": ["ಇ", "ಕ", "ಗ", "ಚ"],
        "answerIndex": 0
    },
    {
        "id": 6,
        "type": "mcq",
        "question": "Which of these is a vyanjana?",
        "options": ["ಅ", "ಓ", "ಟ", "ಊ"],
        "answerIndex": 2
    },
    {
        "id": 7,
        "type": "mcq",
        "question": "Which is the first swara in Kannada?",
        "options": ["ಆ", "ಅ", "ಇ", "ಊ"],
        "answerIndex": 1
    },
    {
        "id": 8,
        "type": "mcq",
        "question": "Which is the last swara in Kannada?",
        "options": ["ಔ", "ಓ", "ಅಂ", "ಅಃ"],
        "answerIndex": 0
    },
    {
        "id": 9,
        "type": "mcq",
        "question": "How many basic swaras (vowels) are there in Kannada?",
        "options": ["10", "12", "14", "16"],
        "answerIndex": 1
    },
    {
        "id": 10,
        "type": "mcq",
        "question": "Which of these is NOT a swara?",
        "options": ["ಎ", "ಐ", "ಝ", "ಓ"],
        "answerIndex": 2
    },
    {
        "id": 11,
        "type": "mcq",
        "question": "Which of these is a vyanjana?",
        "options": ["ಏ", "ಓ", "ಗ", "ಐ"],
        "answerIndex": 2
    },
    {
        "id": 12,
        "type": "mcq",
        "question": "Which letter represents the sound 'ka'?",
        "options": ["ಕ", "ಗ", "ಚ", "ಟ"],
        "answerIndex": 0
    },
    {
        "id": 13,
        "type": "mcq",
        "question": "Which letter represents the sound 'ga'?",
        "options": ["ಕ", "ಗ", "ಝ", "ತ"],
        "answerIndex": 1
    },
    {
        "id": 14,
        "type": "mcq",
        "question": "Which letter represents the sound 'cha'?",
        "options": ["ಚ", "ಜ", "ಟ", "ಪ"],
        "answerIndex": 0
    },
    {
        "id": 15,
        "type": "mcq",
        "question": "Which letter represents the sound 'ta' (dental)?",
        "options": ["ಟ", "ತ", "ಡ", "ದ"],
        "answerIndex": 1
    },
    {
        "id": 16,
        "type": "mcq",
        "question": "Which letter represents the sound 'pa'?",
        "options": ["ಬ", "ಪ", "ಮ", "ವ"],
        "answerIndex": 1
    },
    {
        "id": 17,
        "type": "mcq",
        "question": "Which letter represents the sound 'ma'?",
        "options": ["ನ", "ಮ", "ಣ", "ಙ"],
        "answerIndex": 1
    },
    {
        "id": 18,
        "type": "mcq",
        "question": "Which letter represents the sound 'na' (dental)?",
        "options": ["ಣ", "ನ", "ಙ", "ಞ"],
        "answerIndex": 1
    },
    {
        "id": 19,
        "type": "mcq",
        "question": "Which letter represents the sound 'la'?",
        "options": ["ಲ", "ಳ", "ವ", "ರ"],
        "answerIndex": 0
    },
    {
        "id": 20,
        "type": "mcq",
        "question": "Which letter represents the sound 'ra'?",
        "options": ["ಲ", "ರ", "ವ", "ಯ"],
        "answerIndex": 1
    },
    {
        "id": 21,
        "type": "mcq",
        "question": "Which letter represents the sound 'ya'?",
        "options": ["ಯ", "ವ", "ರ", "ಲ"],
        "answerIndex": 0
    },
    {
        "id": 22,
        "type": "mcq",
        "question": "Which letter represents the sound 'va'?",
        "options": ["ಯ", "ವ", "ರ", "ಲ"],
        "answerIndex": 1
    },
    {
        "id": 23,
        "type": "mcq",
        "question": "Which of these is a combination of consonant + 'aa' sound?",
        "options": ["ಕ", "ಕಾ", "ಅ", "ಆ"],
        "answerIndex": 1
    },
    {
        "id": 24,
        "type": "mcq",
        "question": "Which of these is a combination of consonant + 'ee' sound?",
        "options": ["ಕಿ", "ಕೀ", "ಕು", "ಕೆ"],
        "answerIndex": 1
    },
    {
        "id": 25,
        "type": "mcq",
        "question": "Which of these is a combination of consonant + 'u' sound?",
        "options": ["ಕಾ", "ಕಿ", "ಕು", "ಕೆ"],
        "answerIndex": 2
    },
    {
        "id": 26,
        "type": "mcq",
        "question": "Which of these is a combination of consonant + 'e' sound?",
        "options": ["ಕೆ", "ಕೀ", "ಕು", "ಕೋ"],
        "answerIndex": 0
    },
    {
        "id": 27,
        "type": "mcq",
        "question": "Which of these is a combination of consonant + 'o' sound?",
        "options": ["ಕಿ", "ಕು", "ಕೆ", "ಕೋ"],
        "answerIndex": 3
    },
    {
        "id": 28,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕಿ'?",
        "options": ["ಕ + ಇ", "ಕ + ಈ", "ಕ + ಉ", "ಕ + ಎ"],
        "answerIndex": 0
    },
    {
        "id": 29,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೀ'?",
        "options": ["ಕ + ಇ", "ಕ + ಈ", "ಕ + ಉ", "ಕ + ಎ"],
        "answerIndex": 1
    },
    {
        "id": 30,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕು'?",
        "options": ["ಕ + ಉ", "ಕ + ಊ", "ಕ + ಇ", "ಕ + ಓ"],
        "answerIndex": 0
    },
    {
        "id": 31,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೂ'?",
        "options": ["ಕ + ಉ", "ಕ + ಊ", "ಕ + ಇ", "ಕ + ಓ"],
        "answerIndex": 1
    },
    {
        "id": 32,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೆ'?",
        "options": ["ಕ + ಎ", "ಕ + ಏ", "ಕ + ಐ", "ಕ + ಅ"],
        "answerIndex": 0
    },
    {
        "id": 33,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೇ'?",
        "options": ["ಕ + ಎ", "ಕ + ಏ", "ಕ + ಐ", "ಕ + ಅ"],
        "answerIndex": 1
    },
    {
        "id": 34,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೈ'?",
        "options": ["ಕ + ಎ", "ಕ + ಏ", "ಕ + ಐ", "ಕ + ಅ"],
        "answerIndex": 2
    },
    {
        "id": 35,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೊ'?",
        "options": ["ಕ + ಒ", "ಕ + ಓ", "ಕ + ಉ", "ಕ + ಎ"],
        "answerIndex": 0
    },
    {
        "id": 36,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೋ'?",
        "options": ["ಕ + ಒ", "ಕ + ಓ", "ಕ + ಉ", "ಕ + ಎ"],
        "answerIndex": 1
    },
    {
        "id": 37,
        "type": "mcq",
        "question": "What is the correct combination for 'ಕೌ'?",
        "options": ["ಕ + ಒ", "ಕ + ಓ", "ಕ + ಔ", "ಕ + ಐ"],
        "answerIndex": 2
    },
    {
        "id": 38,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಮನೆ", "ಮನಾ", "ಮಿನ", "ಮುನಿ"],
        "answerIndex": 0
    },
    {
        "id": 39,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಕವಿ", "ಕವಾ", "ಕುವಿ", "ಕೋವಿ"],
        "answerIndex": 0
    },
    {
        "id": 40,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಹಣ್ಣು", "ಹನು", "ಹಿನು", "ಹನ್ನ"],
        "answerIndex": 0
    },
    {
        "id": 41,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ನದಿ", "ನದಾ", "ನುದಿ", "ನುದಾ"],
        "answerIndex": 0
    },
    {
        "id": 42,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಮಗು", "ಮಗಾ", "ಮಗಿ", "ಮಗೀ"],
        "answerIndex": 0
    },
    {
        "id": 43,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಹೂವು", "ಹುವು", "ಹೋವು", "ಹಾವು"],
        "answerIndex": 0
    },
    {
        "id": 44,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಕಾಯಿ", "ಕಾವಿ", "ಕೋಯಿ", "ಕೂಯಿ"],
        "answerIndex": 0
    },
    {
        "id": 45,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಬೆಳ್ಳಿ", "ಬೆಲಿ", "ಬಳ್ಳಿ", "ಬಿಲಿ"],
        "answerIndex": 0
    },
    {
        "id": 46,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಮಣ್ಣು", "ಮನೂ", "ಮಿನು", "ಮನ್ನ"],
        "answerIndex": 0
    },
    {
        "id": 47,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಅಕ್ಕಿ", "ಅಕಿ", "ಅಕ್ಕು", "ಅಕ್ಕಾ"],
        "answerIndex": 0
    },
    {
        "id": 48,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಹಳ್ಳಿ", "ಹಲಿ", "ಹಲ್ಲು", "ಹಲ್ಲೀ"],
        "answerIndex": 0
    },
    {
        "id": 49,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಕುದುರೆ", "ಕುದರೆ", "ಕುದರಿ", "ಕುದರಿ"],
        "answerIndex": 0
    },
    {
        "id": 50,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಮರ", "ಮರಾ", "ಮರಿ", "ಮರೀ"],
        "answerIndex": 0
    },
    {
        "id": 51,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಹಸು", "ಹಸಾ", "ಹಸಿ", "ಹಸೀ"],
        "answerIndex": 0
    },
    {
        "id": 52,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ನಾಯಿ", "ನಾವಿ", "ನೋಯಿ", "ನೂಯಿ"],
        "answerIndex": 0
    },
    {
        "id": 53,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಬೆಕ್ಕು", "ಬಿಕ್ಕು", "ಬಿಕ್ಕು", "ಬಿಕ್ಕು"],
        "answerIndex": 0
    },
    {
        "id": 54,
        "type": "mcq",
        "question": "Which of these is a correct Kannada word?",
        "options": ["ಹಕ್ಕಿ", "ಹಕಿ", "ಹಕ್ಕು", "ಹಕ್ಕಾ"],
        "answerIndex": 0
    },
    {
        "id": 55,
        "type": "mcq",
        "question": "Which of these is a swara?",
        "options": ["ಊ", "ಧ", "ಭ", "ಝ"],
        "answerIndex": 0
    },
    {
        "id": 56,
        "type": "mcq",
        "question": "Which of these is a vyanjana?",
        "options": ["ಏ", "ಐ", "ಘ", "ಓ"],
        "answerIndex": 2
    },
    {
        "id": 57,
        "type": "mcq",
        "question": "Which letter makes the sound 'tha' (retroflex)?",
        "options": ["ತ", "ಥ", "ಟ", "ಠ"],
        "answerIndex": 3
    },
    {
        "id": 58,
        "type": "mcq",
        "question": "Which letter makes the sound 'bha'?",
        "options": ["ಭ", "ಬ", "ಪ", "ಫ"],
        "answerIndex": 0
    },
    {
        "id": 59,
        "type": "mcq",
        "question": "Which letter makes the sound 'sha'?",
        "options": ["ಶ", "ಸ", "ಷ", "ಹ"],
        "answerIndex": 0
    },
    {
        "id": 60,
        "type": "mcq",
        "question": "Which letter makes the sound 'ksha'?",
        "options": ["ಕ್ಷ", "ಛ", "ಝ", "ಞ"],
        "answerIndex": 0
    },
    {
        "id": 61,
        "type": "mcq",
        "question": "Which of these is a Kannada word?",
        "options": ["ಮರಿ", "ಮರೀ", "ಮರಾ", "ಮರೋ"],
        "answerIndex": 0
    },
    {
        "id": 62,
        "type": "mcq",
        "question": "Which of these is a Kannada word?",
        "options": ["ಹಣ್ಣು", "ಹನು", "ಹನ್ನಾ", "ಹನ್ನಿ"],
        "answerIndex": 0
    },
    {
        "id": 63,
        "type": "mcq",
        "question": "Which of these is a Kannada word?",
        "options": ["ಕಾಗೆ", "ಕಾಗಾ", "ಕಾಗೋ", "ಕಾಗೀ"],
        "answerIndex": 0
    },
    {
        "id": 64,
        "type": "mcq",
        "question": "Which of these is a Kannada word?",
        "options": ["ಹೂ", "ಹೋ", "ಹೂಂ", "ಹೂಃ"],
        "answerIndex": 0
    },
    {
        "id": 65,
        "type": "mcq",
        "question": "Which of these is a Kannada word?",
        "options": ["ಮನೆ", "ಮನೋ", "ಮನೀ", "ಮನಾ"],
        "answerIndex": 0
    },
    {
        "id": 66,
        "type": "mcq",
        "question": "Which matra creates the sound 'aa'?",
        "options": ["ಾ", "ಿ", "ೀ", "ು"],
        "answerIndex": 0
    },
    {
        "id": 67,
        "type": "mcq",
        "question": "Which matra creates the sound 'ee'?",
        "options": ["ಾ", "ಿ", "ೀ", "ು"],
        "answerIndex": 2
    },
    {
        "id": 68,
        "type": "mcq",
        "question": "Which matra creates the sound 'u'?",
        "options": ["ಾ", "ಿ", "ೀ", "ು"],
        "answerIndex": 3
    },
    {
        "id": 69,
        "type": "mcq",
        "question": "Which matra creates the sound 'e'?",
        "options": ["ೆ", "ೇ", "ೈ", "ೊ"],
        "answerIndex": 0
    },
    {
        "id": 70,
        "type": "mcq",
        "question": "Which matra creates the sound 'o'?",
        "options": ["ೊ", "ೋ", "ೌ", "ೆ"],
        "answerIndex": 0
    },
    {
        "id": 71,
        "type": "mcq",
        "question": "What is ಕ + ಾ ?",
        "options": ["ಕಾ", "ಕಿ", "ಕು", "ಕೆ"],
        "answerIndex": 0
    },
    {
        "id": 72,
        "type": "mcq",
        "question": "What is ಗ + ೀ ?",
        "options": ["ಗಿ", "ಗೀ", "ಗು", "ಗೆ"],
        "answerIndex": 1
    },
    {
        "id": 73,
        "type": "mcq",
        "question": "What is ಚ + ು ?",
        "options": ["ಚು", "ಚೂ", "ಚೆ", "ಚೋ"],
        "answerIndex": 0
    },
    {
        "id": 74,
        "type": "mcq",
        "question": "What is ಟ + ೆ ?",
        "options": ["ಟೆ", "ಟೇ", "ಟೈ", "ಟೋ"],
        "answerIndex": 0
    },
    {
        "id": 75,
        "type": "mcq",
        "question": "What is ದ + ೋ ?",
        "options": ["ದೊ", "ದೋ", "ದೌ", "ದಾ"],
        "answerIndex": 1
    },
    {
        "id": 76,
        "type": "mcq",
        "question": "Which of these is a correct combination?",
        "options": ["ಪ + ೆ = ಪೆ", "ಪ + ೆ = ಪೇ", "ಪ + ೆ = ಪೈ", "ಪ + ೆ = ಪೋ"],
        "answerIndex": 0
    },
    {
        "id": 77,
        "type": "mcq",
        "question": "Which of these is a correct combination?",
        "options": ["ಬ + ೋ = ಬೋ", "ಬ + ೋ = ಬೈ", "ಬ + ೋ = ಬೌ", "ಬ + ೋ = ಬಾ"],
        "answerIndex": 0
    },
    {
        "id": 78,
        "type": "mcq",
        "question": "Which of these is a correct combination?",
        "options": ["ಮ + ೈ = ಮೈ", "ಮ + ೈ = ಮೇ", "ಮ + ೈ = ಮಾ", "ಮ + ೈ = ಮೌ"],
        "answerIndex": 0
    },
    {
        "id": 79,
        "type": "mcq",
        "question": "Which of these is a correct combination?",
        "options": ["ರ + ೂ = ರೂ", "ರ + ೂ = ರು", "ರ + ೂ = ರಾ", "ರ + ೂ = ರೆ"],
        "answerIndex": 0
    },
    {
        "id": 80,
        "type": "mcq",
        "question": "Which of these is a correct combination?",
        "options": ["ಲ + ೀ = ಲೀ", "ಲ + ೀ = ಲಿ", "ಲ + ೀ = ಲು", "ಲ + ೀ = ಲೋ"],
        "answerIndex": 0
    },
    {
        "id": 81,
        "type": "mcq",
        "question": "Which word means 'water'?",
        "options": ["ನೀರು", "ಮಣ್ಣು", "ಮನೆ", "ಕಾಯಿ"],
        "answerIndex": 0
    },
    {
        "id": 82,
        "type": "mcq",
        "question": "Which word means 'fruit'?",
        "options": ["ಹಣ್ಣು", "ಮಣ್ಣು", "ಮರಿ", "ಕಾಗೆ"],
        "answerIndex": 0
    },
    {
        "id": 83,
        "type": "mcq",
        "question": "Which word means 'bird'?",
        "options": ["ಹಕ್ಕಿ", "ಮರಿ", "ಮನೆ", "ಹೂ"],
        "answerIndex": 0
    },
    {
        "id": 84,
        "type": "mcq",
        "question": "Which word means 'flower'?",
        "options": ["ಹೂ", "ಹಣ್ಣು", "ಮರಿ", "ಮನೆ"],
        "answerIndex": 0
    },
    {
        "id": 85,
        "type": "mcq",
        "question": "Which word means 'child'?",
        "options": ["ಮಗು", "ಮರಿ", "ಮನೆ", "ಮಣ್ಣು"],
        "answerIndex": 0
    },
    {
        "id": 86,
        "type": "mcq",
        "question": "Which word means 'cow'?",
        "options": ["ಹಸು", "ಕುದುರೆ", "ನಾಯಿ", "ಮರಿ"],
        "answerIndex": 0
    },
    {
        "id": 87,
        "type": "mcq",
        "question": "Which word means 'dog'?",
        "options": ["ನಾಯಿ", "ಹಸು", "ಮರಿ", "ಕಾಗೆ"],
        "answerIndex": 0
    },
    {
        "id": 88,
        "type": "mcq",
        "question": "Which word means 'horse'?",
        "options": ["ಕುದುರೆ", "ಹಸು", "ಮರಿ", "ಮನೆ"],
        "answerIndex": 0
    },
    {
        "id": 89,
        "type": "mcq",
        "question": "Which word means 'tree'?",
        "options": ["ಮರ", "ಮರಿ", "ಮನೆ", "ಮಣ್ಣು"],
        "answerIndex": 0
    },
    {
        "id": 90,
        "type": "mcq",
        "question": "Which word means 'soil'?",
        "options": ["ಮಣ್ಣು", "ಮರಿ", "ಮನೆ", "ಮರ"],
        "answerIndex": 0
    },
    {
        "id": 91,
        "type": "mcq",
        "question": "Which word means 'crow'?",
        "options": ["ಕಾಗೆ", "ಹಕ್ಕಿ", "ಮರಿ", "ಮನೆ"],
        "answerIndex": 0
    },
    {
        "id": 92,
        "type": "mcq",
        "question": "Which word means 'milk'?",
        "options": ["ಹಾಲು", "ನೀರು", "ಹಣ್ಣು", "ಮಣ್ಣು"],
        "answerIndex": 0
    },
    {
        "id": 93,
        "type": "mcq",
        "question": "Which word means 'rice'?",
        "options": ["ಅಕ್ಕಿ", "ಅಕ್ಕು", "ಅಕಿ", "ಅಕ್ಕಾ"],
        "answerIndex": 0
    },
    {
        "id": 94,
        "type": "mcq",
        "question": "Which word means 'sugar'?",
        "options": ["ಸಕ್ಕರೆ", "ಸಕ್ಕಿ", "ಸಕ್ಕು", "ಸಕ್ಕಾ"],
        "answerIndex": 0
    },
    {
        "id": 95,
        "type": "mcq",
        "question": "Which word means 'banana'?",
        "options": ["ಬಾಳೆ", "ಬಾಲೆ", "ಬಾಲಿ", "ಬಾಲೋ"],
        "answerIndex": 0
    },
    {
        "id": 96,
        "type": "mcq",
        "question": "Which word means 'leaf'?",
        "options": ["ಎಲೆ", "ಎಲಾ", "ಎಲೋ", "ಎಲೂ"],
        "answerIndex": 0
    },
    {
        "id": 97,
        "type": "mcq",
        "question": "Which word means 'sun'?",
        "options": ["ಸೂರ್ಯ", "ಚಂದ್ರ", "ನಕ್ಷತ್ರ", "ಬೆಳಕು"],
        "answerIndex": 0
    },
    {
        "id": 98,
        "type": "mcq",
        "question": "Which word means 'moon'?",
        "options": ["ಚಂದ್ರ", "ಸೂರ್ಯ", "ನಕ್ಷತ್ರ", "ಬೆಳಕು"],
        "answerIndex": 0
    },
    {
        "id": 99,
        "type": "mcq",
        "question": "Which word means 'star'?",
        "options": ["ನಕ್ಷತ್ರ", "ಚಂದ್ರ", "ಸೂರ್ಯ", "ಬೆಳಕು"],
        "answerIndex": 0
    },
    {
        "id": 100,
        "type": "mcq",
        "question": "Which word means 'light'?",
        "options": ["ಬೆಳಕು", "ಕತ್ತಲೆ", "ಮಣ್ಣು", "ಮನೆ"],
        "answerIndex": 0
    },
    {
        "id": 101,
        "type": "mcq",
        "question": "Which word means 'darkness'?",
        "options": ["ಕತ್ತಲೆ", "ಬೆಳಕು", "ಮಣ್ಣು", "ಮನೆ"],
        "answerIndex": 0
    },
    {
        "id": 102,
        "type": "mcq",
        "question": "Which word means 'flower garden'?",
        "options": ["ಹೂವನ", "ಹೂವನಿ", "ಹೂವನಂ", "ಹೂವನಾ"],
        "answerIndex": 0
    },
    {
        "id": 103,
        "type": "mcq",
        "question": "Which word means 'forest'?",
        "options": ["ಕಾಡು", "ಕಾಡಿ", "ಕಾಡಾ", "ಕಾಡೋ"],
        "answerIndex": 0
    },
    {
        "id": 104,
        "type": "mcq",
        "question": "Which word means 'rain'?",
        "options": ["ಮಳೆ", "ಮಲಾ", "ಮಲೋ", "ಮಲೂ"],
        "answerIndex": 0
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
        "questions": random.sample(QUESTIONS, len(QUESTIONS)),  # SHUFFLED
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
