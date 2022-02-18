def generate_hashtag(s):
    words = s.split(" ")
    words = [x.title() for x in words]
    final = f"#{''.join(words)}"
    if len(final)>140:
        return False
    elif len(final)<1 or len(s)<1:
        return False
    else:
        return final
