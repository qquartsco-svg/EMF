> **한국어 (정본).** English: [README_EN.md](README_EN.md)

# EMF — Electromagnetic Induction Foundation `v0.1.0`

**기전력(EMF)·자기유도**를 파인만 **물리학 강의 2권** 흐름(대략 **16–17장**)에 맞춰 **L1–L5 스크리닝 레이어**로 쌓은 패키지다. GitHub 공개명 **EMF** 는 이 주제를 짧게 가리킨다.

**핵심:** 유도 기전력의 대표식 **ℰ = − N dΦ/dt** (SI) 와, 회로 언어 **V = −L dI/dt** 를 **교육·검증용 proxy**로 다룬다. **FDTD·SPICE·완전 맥스웰 수치해석**을 대체하지 않는다.

**영문 동반본:** [README_EN.md](README_EN.md) · 강의 흐름 표: [docs/FEYNMAN_VOL2_LAYER_MAP.md](docs/FEYNMAN_VOL2_LAYER_MAP.md) · 정전기·경계 상류(00_BRAIN): `_staging/01_A_Electromagnetic_Boundary_Foundation`

---

## 목차

| 절 | 내용 |
|----|------|
| [개념](#1-개념-emf와-레이어) | EMF, 자속, Faraday, 플럭스 규칙 주의 |
| [레이어](#2-레이어-l1l5) | L1–L5 요약 |
| [확장·활용](#3-확장성-및-활용) | 브리지, 00_BRAIN 내 위치 |
| [보안·무결성](#4-보안-및-무결성) | SHA-256 매니페스트, 한계 |
| [후속 방향](#5-후속-방향-로드맵) | 가능한 확장 vs 범위 밖 |
| [Quick start](#6-quick-start) | 설치·테스트·데모 |

---

## 1. 개념 (EMF와 레이어)

- **EMF(기전력):** 도선 루프를 따라 단위 전하가 받는 **접선 힘의 적분**에 해당하는 양으로 이해하는 것이 파인만 17장 서술에 가깝다. **정전기만** 있을 때는 보통 **보수장**이라 ∮**E**·d**l**=0 에 가깝고, **변자속·운동·화학원** 등이 있으면 **비보수** 성분과 **유도 EMF** 이야기가 필요해진다.
- **자속 Φ:** 이 코드의 L2는 **균일 B·평면 루프** 토이 **Φ = NBAcosθ** 로 자속을 잡는다.
- **Faraday:** L3에서 **ℰ = −N dΦ/dt** 로 스크리닝한다.
- **플럭스 규칙 주의:** L4는 슬라이딩 막대·접점 등 **면·경로 정의**가 까다로운 경우(파인만 §17–2 톤)를 **교육용**으로 짚는다.

상세 정본: [CONCEPT.md](CONCEPT.md)

---

## 2. 레이어 (L1–L5)

| 레이어 | 역할 |
|--------|------|
| **L1** | ∂B/∂t·루프 변형·화학 EMF 등 → **정전 서사**가 얼마나 유효한지 |
| **L2** | **자속** (균일 B 토이) |
| **L3** | **Faraday EMF** |
| **L4** | **플럭스 규칙** 적용 시 주의 |
| **L5** | **럼프트** V = −L dI/dt |

---

## 3. 확장성 및 활용

- **`ecosystem_bridges`:** `_staging` 동위에 있을 때 `01_A`(정전·ε₀·μ₀), `Atmospheric_Electric_Circuit`(파인만 9–10장), Optics(EM 경유)를 **얕게** 조회한다.
- **상류:** 정전·경계는 **`Electromagnetic_Boundary_Foundation`** 에서 쌓는 편이 정합적이다(해당 README에 본 패키지 안내 링크 있음).
- **하류(이 패키지 밖):** 다상 매질, 변압기 상세, **상호인덕턴스 행렬**, FDTD — 별도 엔진·도구를 전제로 한다.
- **교육·시나리오:** `omega_em`, `verdict` 는 **정답 선언이 아니라** 입력이 물리 서사와 얼마나 맞물리는지 보는 **observer 스타일** 지표다.

---

## 4. 보안 및 무결성

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

## 5. 후속 방향 (로드맵)

**가능한 확장(이 레포 안에서):**

- 운동기전력·**dv×B** 와 플럭스 규칙을 **같은 입력에서 병치**하는 얇은 모듈
- 상호인덕턴스 **1쌍 코일** 토이
- 브리지 강화(자기 공명·주파수 코어 등)

**범위 밖(별도 프로젝트로 두는 편이 좋음):**

- 맥스웰 **FDTD/FEM**, **SPICE** 수준 회로 해석
- 재료 비선형·히스테리시스·방사

---

## 6. Quick start

| 항목 | 내용 |
|------|------|
| Python | `>=3.10` |
| 테스트 | 로컬 `pytest` 기준 **5 passed** (변경 가능) |
| 의존성 | 런타임 표준 라이브러리 위주 · dev: `pytest>=8.0` |

```bash
git clone https://github.com/qquartsco-svg/EMF.git
cd EMF
pip install -e ".[dev]"
pytest tests/
python3 examples/run_em_induction_demo.py
```

```python
from em_induction import analyze, FaradayEMFInput

rep = analyze()
print(rep.faraday_emf.emf_volts, rep.disclaimer)

rep2 = analyze(
    faraday_emf_input=FaradayEMFInput(n_turns=1, dflux_dt_weber_per_s=-0.03),
    lumped_inductor_input=None,
)
print(rep2.faraday_emf.emf_volts)
```

---

## License

MIT — [LICENSE](LICENSE)
