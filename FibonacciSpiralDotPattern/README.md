<!-- AI AGENTS: Read ./AGENTS.md first, then ./LLM_MEMORY.md.
     Do NOT write planning content into this file. -->

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

# Fibonacci Spiral Dot Pattern

這是我寫著玩的，一個用來生成與探索費氏數列（Fibonacci）螺旋圖案的 Python 小工具。  
透過圖形化的介面，你可以即時調整各種幾何與微調參數（例如點的數量、形狀、數學模型、角度與顏色漸變等），並且支援將結果匯出為 PNG、SVG 以及 DXF 工程圖格式。

## 開發環境與執行方式

1. 建立虛擬環境：
   ```bash
   python -m venv .venv
   ```

2. 啟動虛擬環境：
   - **Windows (PowerShell)**:
     ```powershell
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .\.venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source .venv/bin/activate
     ```

3. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```
   *(主要依賴包含 `numpy`, `matplotlib`, `ezdxf`, `sv-ttk` 等)*

4. 執行程式：
   ```bash
   python fibonacci_spiral.py
   ```

## 授權條款 (License)

本專案採用 [MIT License](LICENSE.md) 授權。
