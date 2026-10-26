# Bottle Cap Inspection

OpenCV 기반으로 **병뚜껑 체결 여부를 자동 판정하는 머신비전 검사 프로젝트**입니다.
카메라 영상에서 검사 영역(ROI)을 정하고, 전처리와 이진화로 뚜껑을 분리한 뒤,
측정한 특징을 기준으로 OK / NG를 판정하는 과정을 단계적으로 구현합니다.

<!-- TODO: 대시보드 / 검사 결과 이미지 추가 -->

## 검사 파이프라인

```text
영상 입력 (이미지 / 동영상 / 스마트폰 실시간)
    ↓
ROI 설정
    ↓
전처리 (Contrast, Blur 등)
    ↓
이진화 (Threshold / Otsu)
    ↓
Morphology / Contour
    ↓
특징 측정 (면적 · 개수 · 위치)
    ↓
Rule 기반 OK / NG 판정
```

## 진행 현황

| 단계 | 내용 | 상태 | 기록 |
|---|---|---|---|
| Day 01 | 검사 문제 설계와 ROI 설정 | 완료 | [day01.md](docs/day01.md) |
| Day 02 | 전처리와 이진화로 검사 영상 품질 개선 | 완료 | [day02.md](docs/day02.md) |
| Day 03 | Morphology · Contour와 Rule 기반 OK / NG 판정 | 예정 | |

## 기술 스택

- Python
- OpenCV
- NumPy
- WSL Ubuntu 22.04

## 폴더 구조

```text
bottle_cap/
├── docs/              # 날짜별 학습 일지
├── outputs/           # 실행 결과 이미지
├── reports/           # 분석 리포트, Parameter 기록
├── samples/           # 입력 샘플 이미지
├── src/               # 단계별 실습 코드 (번호 순서대로 실행)
├── requirements.txt
└── README.md
```

## 실행 방법

```bash
git clone https://github.com/yonghoonchoi88/bottle_cap.git
cd bottle_cap

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/00_check_env.py
```

코드는 상대 경로를 사용하므로 **프로젝트 최상위 폴더에서 실행**해야 합니다.
