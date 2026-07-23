# KCC건설 KMI 대시보드 (김DRN 제작본)

## 📌 Vercel 배포 및 vercel.json 설정 기록

### 1. `vercel.json` 생성 이유
Vercel, GitHub Pages 등 웹 호스팅 서비스는 도메인 주소(예: `https://...vercel.app/`)에 접속할 때 기본적으로 루트 폴더의 `index.html` 파일을 자동으로 찾아 메인 화면으로 보여줍니다.

본 프로젝트에는 `index.html` 대신 `선행지표_통합대시보드_배포용.html`, `수주대시보드.html` 등 여러 개별 대시보드 HTML 파일만 존재합니다.
따라서 기존 HTML 코드를 수정하거나 이름을 바꾸지 않고, Vercel 기본 주소로 접속했을 때 **`선행지표_통합대시보드_배포용.html`이 메인 화면으로 바로 나타나도록** 설정하기 위해 `vercel.json`을 추가했습니다.

### 2. `vercel.json` 설정 내용
```json
{
  "rewrites": [
    {
      "source": "/",
      "destination": "/선행지표_통합대시보드_배포용.html"
    }
  ]
}
```
- `source: "/"` : 사용자가 Vercel 기본 주소로 접속할 때
- `destination: "/선행지표_통합대시보드_배포용.html"` : 해당 HTML 대시보드 화면으로 내부 연결(Rewrite)

---

## 📂 대시보드 목록
- `선행지표_통합대시보드_배포용.html` (기본 메인 연결 페이지)
- `선행지표_통합대시보드.html`
- `건축본부_기성수금_현황판_R1.html`
- `인프라사업팀_기성수금_현황판_R1.html`
- `수주대시보드.html`
- `목표실행달성률.html`
