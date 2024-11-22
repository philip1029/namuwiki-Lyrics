import clipboard

def hex_to_rgb(hex_str):
    """헥스 값을 RGB 값으로 변환하는 함수

    Args:
    hex_str: 변환할 헥스 값 (예: #FFFFFF)

    Returns:
    RGB 값을 담은 튜플 (R, G, B)
    """

    # '#' 제거
    hex_str = hex_str.lstrip('#')

    # 16진수 문자열을 정수로 변환
    rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4)) + (1,)

    return "rgba" + str(rgb)
# hex_to_rgb("#FF00FF") => rgba(255, 0, 255, 1)

clipboard.copy(hex_to_rgb("##703536"))
print("복사 되었습니다!")