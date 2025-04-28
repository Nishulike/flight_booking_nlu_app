# flight_intents.py

def detect_intent(sentence):
    """Detects the intent of the sentence."""
    sentence = sentence.lower()

    if "book" in sentence and "flight" in sentence:
        return "book_flight"
    elif "cancel" in sentence and "flight" in sentence:
        return "cancel_flight"
    elif "price" in sentence or "cost" in sentence:
        return "flight_prices"
    elif "seat" in sentence:
        return "seat_selection"
    elif "status" in sentence:
        return "check_flight_status"
    else:
        return "unknown"
