<!-- AI AGENTS: Read ./AGENTS.md first, then ./LLM_MEMORY.md and ./COMPONENT_MAP.md.
     Do NOT write planning content into this file. -->

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

# AndyToolBox

個人工程與桌面實用工具集合（Monorepo），收錄 5 個獨立 Python 工具；各子目錄皆維持自身 README、依賴清單與執行入口。

## 收錄工具

| 子目錄 | 用途 | 技術棧 | 執行入口 | 自動發版 Tag 前綴 |
|---|---|---|---|---|
| [FibonacciSpiralDotPattern](./FibonacciSpiralDotPattern/) | 費氏數列螺旋點陣圖案產生與 PNG/SVG/DXF 匯出 | Python / Tkinter / Matplotlib / ezdxf | `python fibonacci_spiral.py` | — |
| [PythonCPK](./PythonCPK/) | 製程能力分析（CPK）桌面工具 | Python / PyQt6 / Pandas / SciPy | `python app.py` | `pythoncpk-v*` |
| [QrcodeGenerator](./QrcodeGenerator/) | 進階 QR Code 產生器（PNG/SVG/GIF） | Python / Tkinter / Segno / Pillow | `python QrcodeGenerator.py` | `qrcode-v*` |
| [VoltMatch](./VoltMatch/) | 分壓電阻組合窮舉與最佳化桌面工具 | Python / Tkinter / NumPy / tksheet | `python main.py` | `voltmatch-v*` |
| [rs232-vi-sequence-controller](./rs232-vi-sequence-controller/) | RS232（SCPI）可程式化直流電源三段時序與斜坡控制 | Python / Tkinter / pyserial / NumPy | `python 232.py` | — |

## 打包與發版（GitHub Actions）

三個支援自動建置 Windows EXE 與 Linux AppImage 的工具由根目錄 `.github/workflows/` 各自獨立觸發，避免共用 `v*` tag 衝突：

- **PythonCPK**：推送 `pythoncpk-v*`（例：`git tag pythoncpk-v1.0.2 && git push origin pythoncpk-v1.0.2`），或於 Actions 手動執行 `PythonCPK Package & Release`（僅產 artifact）。
- **QrcodeGenerator**：推送 `qrcode-v*`（例：`git tag qrcode-v1.0.1 && git push origin qrcode-v1.0.1`），或於 Actions 手動執行 `QrcodeGenerator Package & Release`。
- **VoltMatch**：推送 `voltmatch-v*`（例：`git tag voltmatch-v26.1124.1 && git push origin voltmatch-v26.1124.1`）發布 Release；改動 `VoltMatch/**` 推送至 `main` 或開 PR 亦會自動建置驗證 artifact。
