> **한국어 (정본).** English: [FEYNMAN_VOL2_LAYER_MAP_EN.md](FEYNMAN_VOL2_LAYER_MAP_EN.md)

# 파인만 강의 흐름 vs 00_BRAIN `_staging` (요약)

이 표는 **완전한 목차 복제가 아니라**, 레포에 쌓인 것과 **비어 있는 큰 구멍**을 한눈에 보기 위한 것이다.

## 물리학 강의 1권 쪽 (참고)

| 대략적 주제 | `_staging` 예시 | 비고 |
|-------------|-----------------|------|
| 파동·진동 | `Wave_Propagation_Foundation` | Vol.1 파동 서사와 정합 지향 |
| 역학·에너지(다수) | ENGINE_HUB / 여러 applied | 1권 전체를 한 패키지로 묶지는 않음 |

## 물리학 강의 2권 — 전자기

| Feynman Vol.II (대략) | 레이어 / 패키지 | 이 패키지(`em_induction`) 내 축 |
|----------------------|-----------------|--------------------------------|
| 초반: 벡터 미적분, 정전기 | `01_A_Electromagnetic_Boundary_Foundation` | 브리지로 연결 (L1 정전 서사) |
| 대기 전기, 유전 분극 | `Atmospheric_Electric_Circuit_Foundation` (Ch.9–10) | 브리지 |
| **유도 전류 (Ch.16)** | **`Electromagnetic_Induction_Foundation`** | 동기 + Faraday 전제 |
| **유도의 법칙 (Ch.17)** | **동 패키지 L3–L4** | EMF, 플럭스 규칙, 예외 교육 |
| 럼프트 L, 상호인덕턴스 | **동 패키지 L5** | 얇은 proxy |
| 맥스웰 전방정, 파동 | (별도 FDTD급 없음) | 스크리닝 범위 밖 |

## 빠진 것(의도적 또는 미구현)

- **3D 맥스웰 수치해석** (FDTD, 유한요소)
- **완전한 자기정역학** (Biot–Savart 수치, 자석 재료)
- **SPICE급 회로 해석**

이들은 “파운데이션 스크리닝”과 목적이 다르다.

## 정합성 체크리스트

1. 정전기만으로 충분한가? → `em_induction` L1 + `01_A`
2. 자속·루프가 정의되는가? → L2
3. ℰ = −N dΦ/dt 쓸 자격이 있는가? → L3
4. 슬라이딩 막대·접점 등 **플럭스 규칙 주의**가 필요한가? → L4
5. 코일·dI/dt만 묻는가? → L5
