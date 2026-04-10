# Electromagnetic Induction Foundation — SHA-256 무결성

- **목적:** 릴리스에 포함된 파일 트리의 **동일성**을 SHA-256으로 확인한다.
- **범위:** `SIGNATURE.sha256` 에 열거된 경로(README, CONCEPT, `em_induction`, 테스트, 스크립트, `VERSION` 등).
- **“블록체인” 표현:** 암호화폐 원장이 아니라, **무결성 매니페스트**에 가깝다.

검증:

```bash
python3 scripts/generate_signature.py   # 파일 변경 후 재생성
python3 scripts/verify_signature.py
python3 scripts/verify_package_identity.py
python3 scripts/release_check.py
```

**보안 한계:** 이 서명은 **파일 내용이 변조되지 않았는지**를 검사할 뿐, 물리 법칙의 정답·실험 재현·악성 런타임 행위를 보증하지 않는다. 신뢰는 **출처(저장소·커밋 서명·CI)** 와 함께 설계한다.
