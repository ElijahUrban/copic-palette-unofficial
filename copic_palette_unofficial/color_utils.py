
def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return (r, g, b)


def hex_to_hsl(hex_color: str) -> tuple[int, int, int]:
    R, G, B = hex_to_rgb(hex_color)
    r = R / 255
    g = G / 255
    b = B / 255
    mx = max(r, g, b)
    mn = min(r, g, b)

    L = (mx + mn) / 2
    H = 0
    if mx == mn:
        S = 0
    else:
        delta = mx - mn
        S = delta / (2 - mx - mn) if L > 0.5 else delta / (mx + mn)
        if mx == r:
            H = (g - b) / delta
        elif mx == g:
            H = 2 + (b - r) / delta
        else:
            H = 4 + (r - g) / delta
        H *= 60
        if H < 0:
            H += 360
    return round(H), round(S * 100), round(L * 100)
