import json
import random
from pathlib import Path


def load_vocab():
    vocab_path = Path(__file__).resolve().parent.parent / 'data' / 'vocab.json'
    if not vocab_path.exists():
        raise FileNotFoundError(f"Vocabulary file not found at {vocab_path}")

    with vocab_path.open('r', encoding='utf-8') as f:
        return json.load(f)


def get_random_question():
    vocab = load_vocab()
    word = random.choice(vocab)

    options = [word['kannada']]

    while len(options) < 4:
        opt = random.choice(vocab)['kannada']
        if opt not in options:
            options.append(opt)

    random.shuffle(options)

    return{
        "question": f"What is the Kannada word for '{word['english']}'?",
        "correct":word['kannada'],
        "options": options
    }

