def format_name(name: str):
    word_list = [word.title() for word in name.split(" ") if word != ""]
    return " ".join(word_list)
