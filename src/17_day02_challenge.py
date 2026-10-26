from pathlib import Path

import cv2
from matplotlib.pyplot import gray


image_path = Path(
    "samples/day02/cap_on.jpg"
)

output_dir = Path(
    "outputs/day02/my_challenge"
)

output_dir.mkdir(
    parents=True,
    exist_ok=True,
)


image = cv2.imread(
    str(image_path)
)

if image is None:
    raise FileNotFoundError(
        f"이미지를 읽지 못했습니다: {image_path}"
    )


# --------------------------------------------------
# TODO
#
# 1. 이미지의 문제를 판단합니다.
#    - 흐림은 없고 대비도 어느 정도 있음
#    - 흰 뚜껑이 255 근처라 대비를 올리면 포화되기 쉬움
#    - 아래 투명 병목, 오른쪽 회색 배경이 뚜껑과 밝기가 비슷함
# 2. 필요한 전처리를 선택합니다.
#    - Contrast, CLAHE, Sharpening (뒤의 두 개는 약하게)
# 3. Parameter를 직접 정합니다.
#    - Contrast : alpha=1.2, beta=-40 (뚜껑 240 → 248, 배경 60 → 32)
#    - CLAHE    : clipLimit=1.5, tileGridSize=(4, 4)
#    - Sharpen  : Unsharp Mask, sigma=1.0, 강도 0.5
# 4. result에 최종 결과를 저장합니다.
# --------------------------------------------------

# Gray 변환 (CLAHE는 1채널 이미지에 적용)
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

# Contrast: 배경은 어둡게, 뚜껑은 255 아래로 유지
contrast = cv2.convertScaleAbs(
    gray,
    alpha=1.2,
    beta=-40,
)

# Gaussian Blur: 세로 홈을 부드럽게 해서 뚜껑 안의 구멍을 막음
blurred = cv2.GaussianBlur(
    contrast,
    (5, 5),
    0,
)

result = blurred

# # CLAHE: 원본이 저대비가 아니므로 약하게
# clahe = cv2.createCLAHE(
#     clipLimit=1.5,
#     tileGridSize=(4, 4),
# )
# clahe_result = clahe.apply(contrast)

# # Sharpening: 결과 = 원본 × 1.5 − 블러 × 0.5
# blur_for_sharpen = cv2.GaussianBlur(
#     clahe_result,
#     (0, 0),
#     1.0,
# )
# sharpened = cv2.addWeighted(
#     clahe_result, 1.5,
#     blur_for_sharpen, -0.5,
#     0,
# )

# # 최종 결과 (Gray 1채널 → 아래 to_gray()가 그대로 통과시킴)
# result = sharpened



# --------------------------------------------------
# 전처리 결과 저장
# --------------------------------------------------

result_path = (
    output_dir
    / "challenge_result.jpg"
)

cv2.imwrite(
    str(result_path),
    result,
)


# --------------------------------------------------
# Gray 변환
# --------------------------------------------------

def to_gray(source):

    if len(source.shape) == 2:
        return source

    return cv2.cvtColor(
        source,
        cv2.COLOR_BGR2GRAY,
    )


original_gray = to_gray(
    image
)

result_gray = to_gray(
    result
)


# --------------------------------------------------
# 전처리 전 Otsu
#
# 이번 Challenge에서는
# 밝은 병뚜껑을 흰색 객체로 확인합니다.
# --------------------------------------------------

_, original_otsu = cv2.threshold(
    original_gray,
    0,
    255,
    cv2.THRESH_BINARY
    + cv2.THRESH_OTSU,
)


# --------------------------------------------------
# 전처리 후 Otsu
# --------------------------------------------------

_, result_otsu = cv2.threshold(
    result_gray,
    0,
    255,
    cv2.THRESH_BINARY
    + cv2.THRESH_OTSU,
)


cv2.imwrite(
    str(
        output_dir
        / "challenge_original_otsu.jpg"
    ),
    original_otsu,
)

cv2.imwrite(
    str(
        output_dir
        / "challenge_result_otsu.jpg"
    ),
    result_otsu,
)


print("입력 :", image_path)
print("결과 :", result_path)
print("Challenge 완료")