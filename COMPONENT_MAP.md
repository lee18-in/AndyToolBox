# COMPONENT_MAP.md — AndyToolBox 不衰減知識庫

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## 0. 六十秒進入狀況

- **定位**：整併 5 個獨立 Python 桌面／工程工具之 monorepo（2026-11-24 自 5 獨立倉清零舊 `.git` 歷史合併建立）。
- **工作流架構**：採**巢狀獨立交接**（根目錄 1 套三檔管轄根設定與 CI；5 子目錄各保留獨立 `AGENTS.md`/`LLM_MEMORY.md`/`COMPONENT_MAP.md`，互不越界）。
- **Build / Test**：根目錄無統一 build/test；各工具建置與測試慣例見對應子目錄 `COMPONENT_MAP.md`。
- **發版核心紅線**：GitHub Actions 只讀根目錄 `.github/workflows/`，三個打包工具採獨立前綴 tag（`pythoncpk-v*`、`qrcode-v*`、`voltmatch-v*`），禁止共用裸 `v*`。

## 1. 結構與子專案契約

```
AndyToolBox/
├── .gitattributes                       ← scripts/hooks/* text eol=lf
├── .gitignore                           ← 共用忽略規則（刻意不含 *.spec 防擋 VoltMatch.spec；含 AppDir/）
├── .github/workflows/
│   ├── pythoncpk-package.yml            ← pythoncpk-v* + workflow_dispatch（working-directory: PythonCPK）
│   ├── qrcode-package.yml               ← qrcode-v* + workflow_dispatch（working-directory: QrcodeGenerator）
│   └── voltmatch-package.yml            ← voltmatch-v* + main/PR paths VoltMatch/** + workflow_dispatch
├── scripts/hooks/{pre-commit,commit-msg}← Playbook 模板 6 原文，自動偵測根與 5 子目錄巢狀管轄
├── AGENTS.md / CLAUDE.md / GEMINI.md    ← Online v15
├── LLM_MEMORY.md / COMPONENT_MAP.md / README.md
├── FibonacciSpiralDotPattern/           ← 詳見子目錄 COMPONENT_MAP.md
├── PythonCPK/                           ← 詳見子目錄 COMPONENT_MAP.md
├── QrcodeGenerator/                     ← 詳見子目錄 COMPONENT_MAP.md
├── VoltMatch/                           ← 詳見子目錄 COMPONENT_MAP.md（AppDir/ 已於整併移除）
└── rs232-vi-sequence-controller/        ← 詳見子目錄 COMPONENT_MAP.md
```

## 2. 決策與否決理由（2026-11-24 整併拍板）

1. **清零舊 `.git` 重建單倉(1B)**：不保留 5 舊倉歷史，減少膨脹並以單一 initial commit 起步；原 3 倉既有 Releases 隨舊倉刪除（另機保留備份）。
2. **巢狀獨立三檔(2B)**：根與 5 子目錄各維運獨立工作流（共 6 處 `AGENTS.md` v15），子目錄不放重複 `scripts/hooks/` 與 `.gitattributes`，統一由根目錄 `core.hooksPath=scripts/hooks` 管轄。
3. **CI 上移與前綴 tag(3A)**：3 支 `package.yml` 移至根 `.github/workflows/`；所有 `hashFiles()`、`upload-artifact` `path:`、`action-gh-release` `files:` 改為相對於 repo 根之路徑，`run:` 步驟設 `defaults.run.working-directory`；`VoltMatch` 保留 `gh release create` 不用第三方 Action（守子專案決策 #1），並對 `push`/`pull_request` 加 `paths: ['VoltMatch/**', '.github/workflows/voltmatch-package.yml']`（GitHub Actions 對 tag push 不評估 `paths`，故 `voltmatch-v*` 必觸發）。
4. **移除 `VoltMatch/AppDir/`(4A)**：原 342 檔(25 MB)屬舊打包產物，CI 會自 `assets/voltmatch.png` 重建，已排除並寫入根與子目錄 `.gitignore`。

## 3. 環境隱性條件與地雷

1. **根 `.gitignore` 禁加 `*.spec`**：`VoltMatch/VoltMatch.spec` 為版控檔；`PythonCPK` 與 `QrcodeGenerator` 各自子目錄 `.gitignore` 仍保留 `*.spec`。
2. **`core.hooksPath` 屬本機設定**：新 clone 須依 `AGENTS.md` §0 自檢設為 `scripts/hooks` 並 `chmod +x scripts/hooks/*`。
3. **五檔頭英文編碼聲明禁刪**：根與子目錄 `AGENTS.md`/`LLM_MEMORY.md`/`COMPONENT_MAP.md`/`README.md`/`ARCHIVE.md` 均維持頂端聲明。

## 4. 驗證台帳

| 日期 | 項目 | 環境/方法 | 結果 |
|---|---|---|---|
| 2026-11-24 | 整併建倉、3 支 CI YAML、`.gitignore` 與記憶門檻 | macOS arm64：`ruby YAML.load_file`、`git check-ignore -v`、`check_hooks.sh`、`python3` 大小檢查 | 全數通過（詳見 `LLM_MEMORY.md` 首筆） |
