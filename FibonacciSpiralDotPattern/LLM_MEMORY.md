# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: build
- 最後更新: 2026-11-27 14:36 / 當時階段: build
- 交接基準 commit: （初始提交：整併入 AndyToolBox 清零舊版控，首次接手請以 git log -1 覆蓋）
- 進行中任務: 把圓點改成像向日葵花蕊中的類菱形排列
- 阻塞點: 舊版控已清零（原 15:28 v15 已於母倉 15:54 簽結；2026-11-23 `COMPONENT_MAP.md` 補建與本次整併入 `AndyToolBox` 合併待審）。；2026-11-24 16:07 初始整併待審下壓（commit `e97566f`）
    - 完成了什麼: 依 user「推 全倉 套WF」將本 dir `AGENTS.md` 自 Online v16 整份覆蓋升至 v17（§5 禁假優缺點＋§1 `[build]` PDCA Act 閉環；無模板外自訂規則；覆蓋前 hash `611c967`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 8 倉同步 Online v17 憲法（D41）。
    - 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 17`/`Playbook-Variant: online`，全文 `12,791 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
    - 下一個 agent 該做什麼: 本次改動需要審閱：`git diff 3bd0bf7..HEAD -- FibonacciSpiralDotPattern` 核對 Online v17 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
    - 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。
## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ ] 把滑塊邏輯弄得更直觀（包含細調、粗調、還原等功能）
- [ ] 實作設定的匯入與匯出

### B3. 中期目標(本月)

- [ ]

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-11-26 10:35 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「我看過 同步8倉後推」將本 dir `AGENTS.md` 自 Online v15 整份覆蓋升至 v16（精簡英文＋`ARCHIVE` 16 KB 索引規則；無模板外自訂規則；覆蓋前 hash `e97566f`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準；壓 07-06～09-08 舊日誌入〈已封存結論〉（user 明示 `>16 KB` `ARCHIVE` 索引留便宜模型另做）。為何改：全 8 倉同步 Online v16 憲法（D39）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 16`/`Playbook-Variant: online`，全文 `12,405 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff e97566f..HEAD -- FibonacciSpiralDotPattern` 核對 Online v16 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-24 16:07 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B` 整併入 `AndyToolBox/FibonacciSpiralDotPattern/` 並清零舊 `.git` 歷史；移除子目錄重複 `scripts/hooks/` 與 `.gitattributes`（統一改由上層 `AndyToolBox/` 根目錄管轄），同步更新 `COMPONENT_MAP.md`；原 15:28 v15 待審已於母倉 15:54 簽結。為何改：5 工具整併為單一 monorepo 並保留本目錄獨立三檔交接。
- 驗證方式: `AGENTS.md` Online v15 完整保留；工作檔與 `fibonacci_spiral.py`、`init_env.bat`、`requirements.txt` 完整；整檔 `<16 KB`、C 區 `<10 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對整併檔案完整與 `COMPONENT_MAP.md` 同步，並續推原任務「把圓點改成像向日葵花蕊中的類菱形排列」。等待 new session（或 `/clear`）審閱。
- 地雷警告: 舊 commit hash 已因清版控失效，首次審結請以新倉 commit 覆蓋基準；本 context 禁自審。

### 2026-11-23 17:00 [build] 使用工具: Antigravity

- 完成了什麼: 依使用者 2A 補建 `COMPONENT_MAP.md`（遷移舊 E 區指令、套件與 2026-09-08 macOS `matplotlib` 首次字型快取地雷），啟用本機 `core.hooksPath=scripts/hooks` 並覆蓋基準 `3b45374`；未改程式碼。為何改：補齊 v13 三檔結構。
- 驗證方式: `git config --get core.hooksPath`=`scripts/hooks`；對讀 `README.md`、`requirements.txt` 與日誌；`python3` 驗本筆 `<1200 B`、C 區 `<10 KB`、`COMPONENT_MAP <16 KB`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `COMPONENT_MAP.md` 完整收錄技術脈絡與 macOS 字型快取地雷。等待 `new session` 審閱。
- 地雷警告: 接手自檢原 `core.hooksPath` 空，已設 `scripts/hooks` 並 `chmod +x`；僅本地提交未 `push`。

### 2026-11-18 19:39 [maintain] 使用工具: Antigravity

- 完成了什麼: 使用者於 2026-11-18 19:39 明示「我看過結案」，依 §2.1 正式簽結 v12／Online v13 憲法升級，自〈阻塞點〉移除並覆蓋交接基準為 `eff9b40`。
- 驗證方式: `git diff --name-only` 僅異動 `LLM_MEMORY.md`；純記憶更新免新審閱；C 區 `< 10 KB`。
- 下一個 agent 該做什麼: 繼續「把圓點改成像向日葵花蕊中的類菱形排列」（已覆蓋基準為 `eff9b40`）。
- 地雷警告: 無

## D. 已封存結論(自〈總結封存〉搬入,唯讀)

- 2026-07-06～09-08：導入 Playbook v2 並於 08-25 升至 Online v9（補 hook 與 `.gitattributes`）；09-08 確認 macOS 首次 `import matplotlib.pyplot` 掃描系統字型快取屬正常等待行為（已入 `COMPONENT_MAP.md`）。

## E. 專案技術脈絡

（已於 2026-11-23 依 AGENTS.md §5 移入 [COMPONENT_MAP.md](COMPONENT_MAP.md)）
