# COMPONENT_MAP.md — QrcodeGenerator 不衰減知識庫

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## 0. 六十秒進入狀況

- **專案定位**：以 Python（Tkinter + Segno + Pillow）開發的進階 QR Code 產生器，支援即時預覽、顏色自訂、容錯/版本/編碼/UTF-8 ECI 設定，以及 PNG／SVG／GIF 輸出。
- **建置／執行指令**：
  - 本地安裝：`pip install -r requirements.txt`（`Pillow`、`segno`；README 另列 `qrcode[pil]`）
  - 本地執行：`python QrcodeGenerator.py`
  - 自動打包發布：push `qrcode-v*` tag 觸發 `../.github/workflows/qrcode-package.yml`（Windows PyInstaller `--onefile --windowed` `.exe`＋Linux `--onedir` + `appimagetool` `.AppImage` → GitHub Releases；亦支援 `workflow_dispatch` 僅產 artifact）。
- **測試指令**：無自動化測試指令（手動測試 GUI 與輸出格式為主）。
- **程式碼慣例**：UTF-8、繁體中文註解與文件；二進位安裝檔一律走 GitHub Releases，禁止提交至版控。

---

## 1. 專案結構與 CI 契約

```
QrcodeGenerator/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── LLM_MEMORY.md / COMPONENT_MAP.md / ARCHIVE.md / README.md / LICENSE
├── .gitignore
├── QrcodeGenerator.py               ← 主程式
├── requirements.txt                 ← Pillow, segno
└── assets/qrcodegenerator.png       ← Linux AppImage 應用程式圖示
```
（註：`.gitattributes` 與 `scripts/hooks/` 統一由上層 `AndyToolBox/` 根目錄管轄；CI 位於 `../.github/workflows/qrcode-package.yml`。）

- **CI 打包關鍵紅線**（見 `../.github/workflows/qrcode-package.yml`）：Python `"3.12"` 加引號；Linux 建置不用 `--windowed`、不用 YAML heredoc（改以 `printf` 寫 `.desktop` 與 `AppRun`）、執行 `appimagetool` 必加 `APPIMAGE_EXTRACT_AND_RUN=1`，產物以 `softprops/action-gh-release@v2` 上傳（僅 `refs/tags/qrcode-v*` 觸發 Release）。

---

## 2. 環境隱性條件、地雷與驗證台帳

1. **`.gitignore` 引號語法地雷（2026-09-12 事故根因）**：過去 `.gitignore` 寫成 `"venv/"`（帶雙引號）從未生效，導致 1,327 個 Linux `venv/` 檔（32.9 MB）與 `bin/` 執行檔（53.5 MB）進版控。現已改為 `venv*/`、`.venv*/`、`bin/*.AppImage`、`bin/*.exe`、`build/`、`dist/`、`*.spec`，並以 `git filter-repo` 自全歷史清除（`.git` 65 MB → 180 KB）。
2. **`*.spec` 規則注意**：目前 repo 無追蹤任何 `.spec` 檔；日後若需版控自訂 PyInstaller `.spec`，須調整 `.gitignore` 排除。
3. **`core.hooksPath` 屬本機設定**：新 clone 或換機後須依 `AGENTS.md` §0 自檢確認 `core.hooksPath=scripts/hooks`（搭配 `.gitattributes` 鎖定 `scripts/hooks/* text eol=lf`）。

| 日期 | 驗證項目 | 方法 | 結果 |
|---|---|---|---|
| 2026-09-12 | `.gitignore` 生效與歷史瘦身 | `git check-ignore -v`、`git filter-repo`、hook 反向測試 | 1,327 檔 `venv/`＋2 檔 `bin/` 徹底清除；`.git` 65M→180K |
| 2026-11-23 | 09-12 審閱檢核點 1–4＋`package.yml` 獨立複查 | 核對 `.gitignore`、`git check-ignore -v`、`README.md`、`package.yml`、`git ls-files` | 全數通過結案（無殘留 `bin/` 失效連結、CI Releases 完整） |
