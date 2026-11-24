# COMPONENT_MAP.md — FibonacciSpiralDotPattern 不衰減知識庫

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## 0. 六十秒進入狀況

- **專案定位**：以 Python GUI 即時探索與生成費氏數列（Fibonacci）螺旋點陣圖案，並匯出 PNG／SVG／DXF 工程圖的小工具。
- **建置／執行指令**：
  - 建立環境：`python -m venv .venv` → 啟動後 `pip install -r requirements.txt`（Windows 另附 `init_env.bat`）
  - 執行程式：`python fibonacci_spiral.py`
- **測試指令**：無特定自動化測試框架（GUI 操作與匯出實測為主）。
- **程式碼慣例**：Python 3、PEP-8、UTF-8 繁體中文註解與文件。

---

## 1. 專案結構與相依套件

```
FibonacciSpiralDotPattern/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── LLM_MEMORY.md / COMPONENT_MAP.md / README.md / LICENSE
├── fibonacci_spiral.py      ← 主程式（GUI + 幾何生成 + PNG/SVG/DXF 匯出）
├── init_env.bat             ← Windows 環境初始化批次檔
└── requirements.txt         ← numpy, matplotlib, ezdxf, Pillow, sv-ttk
```
（註：`.gitattributes` 與 `scripts/hooks/{pre-commit,commit-msg}` 統一置於上層 `AndyToolBox/` 根目錄管轄。）

---

## 2. 環境隱性條件與已知地雷

1. **macOS 首次啟動 `matplotlib` 看似卡住（2026-09-08 實測已驗證）**：首次 `import matplotlib.pyplot` 會呼叫 `system_profiler -xml SPFontsDataType` 建立字型快取（如 `~/.matplotlib/fontlist-v390.json`）；建完後匯入僅約 `0.21s`。**切勿在首次建快取期間按 `Ctrl-C` 中斷**，否則下次啟動會重頭掃描。
2. **`core.hooksPath` 屬本機設定**：新 clone 或換機後須依 `AGENTS.md` §0 自檢確認 `core.hooksPath=scripts/hooks`。
