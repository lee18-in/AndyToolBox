# COMPONENT_MAP.md — rs232-vi-sequence-controller 不衰減知識庫

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## 0. 六十秒進入狀況

- **專案定位**：以 Python 3 + Tkinter + RS232（SCPI 指令）控制可程式化直流電源供應器之三段式電壓／電流時序與斜坡過渡（Ramp）工具。
- **建置／安裝指令**：`pip install -r requirements.txt`（依賴 `pyserial`、`numpy`）。
- **執行／測試指令**：`python 232.py`（無自動化測試框架，依實體 RS232 電源供應器手動測試）。
- **程式碼慣例**：標準 Python 3 + Tkinter；控制迴圈運行於獨立背景執行緒防 GUI 凍結，註解與文件採 UTF-8 繁體中文。

---

## 1. 專案結構與核心控制契約

```
rs232-vi-sequence-controller/
├── AGENTS.md / CLAUDE.md / GEMINI.md
├── LLM_MEMORY.md / COMPONENT_MAP.md / README.md / LICENSE
├── 232.py                   ← 主程式（Tkinter GUI + SCPI RS232 控制 + 緊急停止）
└── requirements.txt         ← pyserial, numpy
```
（註：`.gitattributes` 與 `scripts/hooks/{pre-commit,commit-msg}` 統一置於上層 `AndyToolBox/` 根目錄管轄。）

- **序列埠預設參數**（`232.py` L7–L8）：`SERIAL_PORT = 'COM3'`、`BAUDRATE = 115200`（硬編於頂端常數，依實體連接埠調整，如 Linux `/dev/ttyUSB0`）。
- **SCPI 通訊契約**：`:SOUR:CURR <A>`、`:SOUR:VOLT <V>`、`:OUTP ON`／`:OUTP OFF`（指令結尾 `\n`；含 `?` 則 `readline()` 回讀）。
- **斜坡過渡規則**（`ramp_va()`）：段落轉換時間 `< 50 ms` 直接跳終點；`>= 50 ms` 以 `np.linspace` 分 50 步線性漸變，每步檢查 `stop_flag`。
- **安全紅線（緊急停止 `emergency_stop()`）**：立即設 `stop_flag = True`，重新開埠強制送 `:SOUR:CURR 0` → `:SOUR:VOLT 0` → `:OUTP OFF` 歸零斷電。

---

## 2. 已知落差與環境地雷

1. **檔名落差（已核實）**：`README.md` L41／L45 撰寫檔名為 `RS232.py`，但倉庫實際主程式檔名為 **`232.py`**（尚未修改 README）。
2. **`core.hooksPath` 屬本機設定**：新 clone 或換機後須依 `AGENTS.md` §0 自檢確認 `core.hooksPath=scripts/hooks`。
