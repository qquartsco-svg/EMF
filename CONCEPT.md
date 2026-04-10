> **한국어 (정본).** English: [CONCEPT_EN.md](CONCEPT_EN.md)

# Electromagnetic Induction Foundation — 개념

## 위치

파인만 **물리학 강의 2권** 흐름에서 **정전기·대기·유전(초반~9–10장)** 다음에 오는 **유도·기전력(16–17장)** 을 **스크리닝 레이어**로 쌓는다. 맥스웰 전체 수치해석이나 SPICE를 대체하지 않는다.

## Vol.1 vs Vol.2 (00_BRAIN에서의 대략)

- **1권 쪽**: 역학·열·파동 등은 여러 엔진에 흩어져 있고, 예를 들어 `Wave_Propagation_Foundation` 은 1권 파동 서사와 맞닿는다.
- **2권 쪽**: `01_A` 가 정전·경계, `Atmospheric_Electric_Circuit` 이 9–10장, **본 패키지**가 16–17장에 가까운 층을 담당한다.

상세 표: [docs/FEYNMAN_VOL2_LAYER_MAP.md](docs/FEYNMAN_VOL2_LAYER_MAP.md)

## 레이어 (본 패키지)

| 레이어 | 역할 | 파인만 대응(대략) |
|--------|------|-------------------|
| L1 | 정전/스칼라 전위 서사가 얼마나 유효한지 | ∂B/∂t, 운동, 화학 EMF 등 플래그 |
| L2 | 균일 B, 평면 루프 자속 Φ = NBAcosθ | 자속 정의 토이 |
| L3 | ℰ = −N dΦ/dt | 17장 플럭스 법칙 (스크리닝) |
| L4 | 플럭스 규칙 **주의** (슬라이딩 막대·접점 등) | 17–2 예외·역설 교육 |
| L5 | 럼프트 V = −L dI/dt | 변압기·16장 동기 뒤 회로 언어 |

## 브리지

- `01_A_Electromagnetic_Boundary_Foundation`
- `Atmospheric_Electric_Circuit_Foundation`
- Optics (EM boundary 경유, 가능할 때)

## 면책

수치·실험·공학 결론을 대신하지 않는다. Ω·verdict 는 교육·순서 점검용이다.
