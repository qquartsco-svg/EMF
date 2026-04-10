> **한국어 (정본).** English: [README_EN.md](README_EN.md)

# EMF — Electromagnetic Induction Foundation `v0.1.0`

| 항목 | 내용 |
|------|------|
| 버전 | `v0.1.0` |
| 테스트 | 현재 기준: `pytest` **5 passed** |
| Python | `>=3.10` |
| 의존성 | 런타임: 표준 라이브러리 위주 · dev: `pytest>=8.0` |
| 라이선스 | MIT |

**기전력(EMF)·자기유도**를 파인만 **물리학 강의 2권** 흐름(대략 **16–17장**)에 맞춰 **L1–L5 스크리닝 레이어**로 쌓은 패키지다. GitHub 공개명 **EMF** 는 이 주제를 짧게 가리킨다.

**핵심:** 유도 기전력의 대표식 **ℰ = − N dΦ/dt** (SI) 와, 회로 언어 **V = −L dI/dt** 를 **교육·검증용 proxy**로 다룬다. **FDTD·SPICE·완전 맥스웰 수치해석**을 대체하지 않는다.

**영문 동반본:** [README_EN.md](README_EN.md) · 강의 흐름 표: [docs/FEYNMAN_VOL2_LAYER_MAP.md](docs/FEYNMAN_VOL2_LAYER_MAP.md) · 정전기·경계 상류(00_BRAIN): `_staging/01_A_Electromagnetic_Boundary_Foundation`

---

## 목차

| 절 | 내용 |
|----|------|
| [개념](#1-개념-emf와-레이어) | EMF, 자속, Faraday, 플럭스 규칙 주의 |
| [레이어](#2-레이어-l1l5) | L1–L5 한 줄 보강 |
| [omega_em · verdict](#3-omega_em과-verdict) | 통합 Ω와 판정 구간 |
| [확장·활용](#4-확장성-및-활용) | 브리지, 00_BRAIN 내 위치 |
| [보안·무결성](#5-보안-및-무결성) | SHA-256 매니페스트, 한계 |
| [후속 방향](#6-후속-방향-로드맵) | 가능한 확장 vs 범위 밖 |
| [Quick start](#7-quick-start) | 설치·테스트·예제 |

---

## 1. 개념 (EMF와 레이어)

- **EMF(기전력):** 도선 루프를 따라 단위 전하가 받는 **접선 힘의 적분**에 해당하는 양으로 이해하는 것이 파인만 17장 서술에 가깝다. **정전기만** 있을 때는 보통 **보수장**이라 ∮**E**·d**l**=0 에 가깝고, **변자속·운동·화학원** 등이 있으면 **비보수** 성분과 **유도 EMF** 이야기가 필요해진다.
- **자속 Φ:** 이 코드의 L2는 **균일 B·평면 루프** 토이 **Φ = NBAcosθ** 로 자속을 잡는다.
- **Faraday:** L3에서 **ℰ = −N dΦ/dt** 로 스크리닝한다.
- **플럭스 규칙 주의:** L4는 슬라이딩 막대·접점 등 **면·경로 정의**가 까다로운 경우(파인만 §17–2 톤)를 **교육용**으로 짚는다.

상세 정본: [CONCEPT.md](CONCEPT.md)

---

## 2. 레이어 (L1–L5)

| 레이어 | 한 줄 | 역할(조금 더 풀어서) |
|--------|------|----------------------|
| **L1** | 정전 서사가 깨지는 조건을 스크리닝 | ∂B/∂t, 루프 면적·형상 변화, 화학 EMF, 변위전류 등 플래그로 **보수장 전기장만으로 충분한지**·**유도가 얼마나 관련되는지** proxy |
| **L2** | 자속 정의와 기하 | 균일 **B**, 평면 루프, **N** 권수, **θ** 로 **Φ** 계산 (고급 기하·비균일장은 범위 밖) |
| **L3** | Faraday 유도 EMF | **ℰ = −N dΦ/dt** 또는 두 시각의 Φ 차이로 **dΦ/dt** 근사 |
| **L4** | 플럭스 규칙 주의 사례 | 슬라이딩 막대·이동 접점·(표시용) 가속기 류 **서술 난점**을 올려 **교육용 주의 깊음** 점수화 |
| **L5** | lumped inductor 회로 proxy | **V = −L dI/dt** 로 코일·리액턴스 **회로 언어** 한 조각만 |

---

## 3. `omega_em`과 `verdict`

통합 **`omega_em`** 은 실행된 레이어들의 **Ω 평균**에 가깝다. **`verdict`** 는 그 값을 구간에 넣은 **스크리닝 라벨**이다 (실험·설계 최종 판정 아님).

| `omega_em` 구간 | `verdict` |
|-----------------|-----------|
| **≥ 0.78** | `operational` |
| **≥ 0.52** | `feasible` |
| **≥ 0.28** | `experimental` |
| **&lt; 0.28** | `not_feasible` |

---

## 4. 확장성 및 활용

- **`ecosystem_bridges`:** `_staging` 동위에 있을 때 `01_A`(정전·ε₀·μ₀), `Atmospheric_Electric_Circuit`(파인만 9–10장), Optics(EM 경유)를 **얕게** 조회한다.
- **상류:** 정전·경계는 **`Electromagnetic_Boundary_Foundation`** 에서 쌓는 편이 정합적이다(해당 README에 본 패키지 안내 링크 있음).
- **연관 서사(브리지 코드 없을 수 있음):** 나노 스케일에서 길이·시간에 따른 **유도 민감도** 서사는 **`Nano_Scale_Foundation`** 과 개념적으로 이어 읽을 수 있다.
- **하류(이 패키지 밖):** 다상 매질, 변압기 상세, **상호인덕턴스 행렬**, FDTD — 별도 엔진·도구를 전제로 한다.
- **교육·시나리오:** `omega_em`, `verdict` 는 **정답 선언이 아니라** 입력이 물리 서사와 얼마나 맞물리는지 보는 **observer 스타일** 지표다.

---

## 5. 보안 및 무결성

- **`SIGNATURE.sha256`:** 릴리스 파일들의 **SHA-256 목록**이다. **암호화폐 체인이 아니다.**
- **역할:** 클론·배포본이 **의도한 트리와 같은지** 빠르게 확인.
- **한계:** 물리 정확도·실험 재현·**런타임 악성 코드**를 보증하지 않는다. **서명 커밋·CI·출처 검증**과 병행하는 것이 좋다.

```bash
python3 scripts/generate_signature.py
python3 scripts/verify_signature.py
python3 scripts/verify_package_identity.py
python3 scripts/release_check.py
```

자세한 설명: [BLOCKCHAIN_INFO.md](BLOCKCHAIN_INFO.md) · [BLOCKCHAIN_INFO_EN.md](BLOCKCHAIN_INFO_EN.md)

---

## 6. 후속 방향 (로드맵)

**가능한 확장(이 레포 안에서):**

- 운동기전력·**v×B** 와 플럭스 규칙을 **같은 입력에서 병치**하는 얇은 모듈
- 상호인덕턴스 **1쌍 코일** 토이
- 브리지 강화(자기 공명·주파수 코어 등)

**범위 밖(별도 프로젝트로 두는 편이 좋음):**

- 맥스웰 **FDTD/FEM**, **SPICE** 수준 회로 해석
- 재료 비선형·히스테리시스·방사

---

## 7. Quick start

```bash
git clone https://github.com/qquartsco-svg/EMF.git
cd EMF
pip install -e ".[dev]"
pytest tests/
python3 examples/run_em_induction_demo.py
```

### 예제 — 데모 전 스택

```python
from em_induction import analyze, FaradayEMFInput

rep = analyze()
print(rep.omega_em, rep.verdict.value, rep.faraday_emf.emf_volts)
print(rep.disclaimer)
```

### 예제 — 변자속만 (Faraday / L3 중심)

```python
from em_induction import analyze, FaradayEMFInput, MagneticFluxInput, StaticRegimeInput

rep = analyze(
    static_regime_input=StaticRegimeInput(time_varying_magnetic_field=True),
    magnetic_flux_input=MagneticFluxInput(b_field_t=0.1, loop_area_m2=0.05, n_turns=1),
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=2e-4),
    lumped_inductor_input=None,
)
print("EMF (V):", rep.faraday_emf.emf_volts)
```

### 예제 — 럼프트 인덕터만 (L5 중심)

```python
from em_induction import analyze, LumpedInductorInput, MagneticFluxInput, StaticRegimeInput

rep = analyze(
    static_regime_input=StaticRegimeInput(),
    magnetic_flux_input=MagneticFluxInput(b_field_t=0.0, loop_area_m2=1e-6),
    faraday_emf_input=None,
    lumped_inductor_input=LumpedInductorInput(inductance_h=1e-3, di_dt_a_per_s=200.0),
)
print("L dI/dt EMF (V):", rep.lumped_inductor.emf_volts)
```

### 예제 — dΦ/dt 부호만 넣는 최소 Faraday

```python
from em_induction import analyze, FaradayEMFInput

rep = analyze(
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=-0.03),
    lumped_inductor_input=None,
)
print(rep.faraday_emf.emf_volts)
```

---

## License

MIT — [LICENSE](LICENSE)
