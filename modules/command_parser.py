from difflib import SequenceMatcher
import re


class CommandParser:
    def __init__(self):
        self.threshold = 0.75

        self.apps = ["whatsapp","instagram","facebook","youtube","telegram","chrome","gmail","maps","camera","gallery","spotify","play store","calculator","calendar","contacts","settings"]

        self.intents = {
            "OPEN_CAMERA": {
                "message": "Opening camera...",
                "keywords": [
                    "camera",
                    "open camera",
                    "launch camera",
                    "take photo",
                    "photo",
                    "selfie",
                    "rear camera",
                    "back camera"
                ]
            },

            "OPEN_GALLERY": {
                "message": "Opening gallery...",
                "keywords": [
                    "gallery",
                    "photos",
                    "images",
                    "album"
                ]
            },

            "TORCH_ON": {
                "message": "Turning torch ON...",
                "keywords": [
                    "torch on",
                    "turn on torch",
                    "flash on",
                    "light on",
                    "flash chalu",
                    "light chalu"
                ]
            },

            "TORCH_OFF": {
                "message": "Turning torch OFF...",
                "keywords": [
                    "torch off",
                    "turn off torch",
                    "flash off",
                    "light off",
                    "flash bandh",
                    "light bandh"
                ]
            }
        }

    def parse(self, command: str):

        command = self._normalize(command)

        result = self._detect_app(command)
        if result:
            return result

        result = self._exact_match(command)
        if result:
            return result

        result = self._token_match(command)
        if result:
            return result

        return {
            "success": False,
            "intent": "UNKNOWN",
            "message": "Sorry, I didn't understand the command.",
            "confidence": 0.0,
            "data": {}
        }

    # -------------------------

    def _exact_match(self, command):

        for intent, data in self.intents.items():

            for keyword in data["keywords"]:

                if keyword in command:

                    return {
                        "success": True,
                        "intent": intent,
                        "message": data["message"],
                        "confidence": 1.0,
                        "data": {}
                    }

        return None

    # -------------------------

    def _token_match(self, command):

        words = command.split()

        best_intent = None
        best_message = ""
        best_score = 0

        for intent, data in self.intents.items():

            for keyword in data["keywords"]:

                keyword_words = keyword.split()

                total = 0

                for kw in keyword_words:

                    word_score = 0

                    for user_word in words:

                        score = SequenceMatcher(
                            None,
                            kw,
                            user_word
                        ).ratio()

                        word_score = max(word_score, score)

                    total += word_score

                average = total / len(keyword_words)

                if average > best_score:
                    best_score = average
                    best_intent = intent
                    best_message = data["message"]

        if best_score >= self.threshold:

            return {
                "success": True,
                "intent": best_intent,
                "message": best_message,
                "confidence": round(best_score, 2),
                "data": {}
            }

        return None

    # -------------------------

    def _normalize(self, text):

        text = text.lower()

        text = re.sub(r"[^\w\s]", " ", text)

        text = " ".join(text.split())

        return text

    def _detect_app(self, command):

        trigger_words = [
            "open",
            "launch",
            "start",
            "run",
            "kholo"
        ]

        for trigger in trigger_words:

            if trigger in command:

                remaining = command.replace(trigger, "").strip()

                best_app = None
                best_score = 0

                for app in self.apps:

                    score = SequenceMatcher(
                        None,
                        remaining,
                        app
                    ).ratio()

                    if score > best_score:
                        best_score = score
                        best_app = app

                if best_score >= self.threshold:

                    return {
                        "success": True,
                        "intent": "OPEN_APP",
                        "message": f"Opening {best_app}...",
                        "confidence": round(best_score, 2),
                        "data": {
                            "app": best_app
                        }
                    }

        return None


