## Challenge

### 문제

작성: cap_on.jpg는 흐림이 없고 뚜껑과 위쪽 배경의 밝기 차이도 충분하다. 다만 흰 뚜껑이 255에 가까워 대비를 올리면 포화되기 쉽고, 표면의 세로 홈과 인쇄 글자가 이진화 시 노이즈가 될 수 있다. 또한 아래쪽 투명한 병목이 뚜껑과 밝기가 비슷하다.

### 시도한 전처리

작성:
1. Contrast + CLAHE + Sharpening
2. Contrast + Gaussian Blur

### 비교한 Parameter

작성:
- Contrast: alpha=1.2, beta=-40 (뚜껑 약 240 → 248로 포화 방지, 배경 약 60 → 32로 어둡게)
- CLAHE: clipLimit=1.5, tileGridSize=(4, 4)
- Sharpening(Unsharp Mask): sigma=1.0, amount=0.5
- Gaussian Blur: ksize=(5, 5)

### 최종 선택

작성: Contrast(alpha=1.2, beta=-40) + Gaussian Blur(ksize=(5, 5))

### 선택 이유

작성: 이 이미지의 문제는 저대비나 흐림이 아니라 뚜껑 표면의 무늬였다. CLAHE와 Sharpening은 오히려 세로 홈을 강조해 결과를 나쁘게 만들었고, 블러는 표면 무늬를 줄여 뚜껑을 하나의 덩어리로 만들어 주었다.

### 좋아진 점

작성: 뚜껑 내부의 구멍과 인쇄 글자 노이즈가 사라졌고, 외곽선이 매끄러워졌다. 배경은 검게 유지되었다.

### 나빠진 점

작성: 첫 번째 시도(CLAHE + Sharpening)에서는 뚜껑 내부에 검은 구멍과 세로줄이 생겼다. 최종 방법에서도 투명한 병목이 흰색으로 함께 잡히는 문제는 해결되지 않았다.

### Otsu 비교 결과

작성: 원본 Otsu도 뚜껑을 대체로 잘 분리했지만 글자 부분에 검은 점이 남았다. CLAHE + Sharpening 적용 후에는 원본보다 나빠졌고, Contrast + Blur 적용 후에는 뚜껑이 구멍 없는 흰 덩어리로 분리되어 원본보다 깨끗해졌다. 세 결과 모두 병목은 흰색으로 잡혔다.

### 최종 판단

- 사용: Contrast + Gaussian Blur
- 미사용: CLAHE, Sharpening (이 이미지에서는 표면 무늬를 강조해 역효과)
- 3일차 추가 확인: 병목 분리. 밝기 전처리로는 해결되지 않으므로 ROI 조정, Morphology, Contour 처리로 뚜껑 영역만 남기는 방법을 확인