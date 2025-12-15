def validate_generate_request(data):
    if not data:
        return False, "Request body required"

    if "text" not in data:
        return False, "Field 'text' is required"

    text = data["text"].strip()

    if len(text) < 10:
        return False, "Enter at least 10 characters"

    if len(text) > 20000:
        return False, "Text too long"

    return True, ""
