# 환율 조회 웹앱

부트캠프 3일차 Streamlit 실습입니다. 통화와 금액을 선택하면 Frankfurter의 최신 기준 환율과 환산 금액을 표시합니다.

## PowerShell에서 실행

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Frankfurter 공개 API는 키 없이 사용할 수 있습니다.
