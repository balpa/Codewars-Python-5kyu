def hex_string_to_RGB(hex_string): 
    h = hex_string.lstrip('#')
    a = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    final = {"r":a[0], "g": a[1], "b": a[2] }
    return final
