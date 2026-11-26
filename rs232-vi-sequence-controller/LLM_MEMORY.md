# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: build
- 最後更新: 2026-11-26 10:35 / 當時階段: maintain
- 交接基準 commit: （初始提交：整併入 AndyToolBox 清零舊版控，首次接手請以 git log -1 覆蓋）
- 進行中任務: 測試中
- 阻塞點: 舊版控已清零（原 15:28 v15 已於母倉 15:54 簽結；2026-11-23 `COMPONENT_MAP.md` 補建與本次整併入 `AndyToolBox` 合併待審）。；2026-11-24 16:07 初始整併待審下壓（commit `e97566f`）

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ ]

### B3. 中期目標(本月)

- [ ]

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-11-26 10:35 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「我看過 同步8倉後推」將本 dir `AGENTS.md` 自 Online v15 整份覆蓋升至 v16（精簡英文＋`ARCHIVE` 16 KB 索引規則；無模板外自訂規則；覆蓋前 hash `e97566f`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準（user 明示 `>16 KB` `ARCHIVE` 索引留便宜模型另做）。為何改：全 8 倉同步 Online v16 憲法（D39）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 16`/`Playbook-Variant: online`，全文 `12,405 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff e97566f..HEAD -- rs232-vi-sequence-controller` 核對 Online v16 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-24 16:07 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B` 整併入 `AndyToolBox/rs232-vi-sequence-controller/` 並清零舊 `.git` 歷史；移除子目錄重複 `scripts/hooks/` 與 `.gitattributes`（統一改由上層 `AndyToolBox/` 根目錄管轄），同步更新 `COMPONENT_MAP.md`；原 15:28 v15 已於母倉 15:54 簽結。為何改：5 工具整併為單一 monorepo 並保留獨立三檔交接。
- 驗證方式: `AGENTS.md` Online v15 完整保留；`232.py`/`requirements.txt`/`README.md` 完整；整檔 `<16 KB`、C 區 `<10 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對整併檔案完整與 `COMPONENT_MAP.md` 同步。等待 new session（或 `/clear`）審閱。
- 地雷警告: 舊 commit hash 已失效，首次審結請覆蓋新倉基準；本 context 禁自審。

### 2026-11-24 15:28 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「再部屬12區」將本 dir `AGENTS.md` 自 Online v14 整份覆蓋升至 v15（無模板外自訂規則；覆蓋前 hash `b6f7ef8`）；原首筆 v14 待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 12 倉同步 Online v15 憲法（D38）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 15`/`Playbook-Variant: online`，全文 `10,219 B`/92 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff 73c92dc..HEAD` 核對 Online v15 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 context 禁自審。

### 2026-11-24 14:07 [maintain] 使用工具: Antigravity (Gemini 4 Neon)

- 完成了什麼: 依使用者「12全區佈署」指示將本目錄 `AGENTS.md` 自 Online v13 整份覆蓋升級至 v14（無模板外自訂規則；覆蓋前 hash `0b59dc4`）；無待審已覆蓋交接基準為 `73c92dc`。為何改：全 12 倉同步 Online v14 憲法。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 14` 與 `Playbook-Variant: online`，全文 `10,191 B`/89 行與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 逐位元組一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v14 模板確認條文一致且 A 區進行中任務未遭改寫。等待 `new session`（或 `/clear` 清空 `context`，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 `context` 禁自審。

### 2026-11-23 17:00 [build] 使用工具: Antigravity

- 完成了什麼: 依使用者 2A 補建 `COMPONENT_MAP.md`（遷移舊 E 區、萃取 `232.py` SCPI／50ms 斜坡／緊急停止安全契約與 `README.md` 誤寫 `RS232.py` 檔名落差），啟用本機 `core.hooksPath=scripts/hooks` 並覆蓋基準 `73c92dc`；未改程式碼。為何改：補齊 v13 三檔。
- 驗證方式: `git config --get core.hooksPath`=`scripts/hooks`；對讀 `232.py`、`requirements.txt`、`README.md`；`python3` 驗本筆 `<1200 B`、C 區 `<10 KB`、`COMPONENT_MAP <16 KB`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `COMPONENT_MAP.md` 與 `232.py` 實況一致且未動程式碼。等待 `new session` 審閱。
- 地雷警告: 接手自檢原 `core.hooksPath` 空，已設 `scripts/hooks` 並 `chmod +x`；僅本地提交未 `push`。

### 2026-11-18 19:39 [maintain] 使用工具: Antigravity

- 完成了什麼: 使用者於 2026-11-18 19:39 明示「我看過結案」，依 §2.1 正式簽結 v12／Online v13 憲法升級，自〈阻塞點〉移除並覆蓋交接基準為 `0b59dc4`。
- 驗證方式: `git diff --name-only` 僅異動 `LLM_MEMORY.md`；純記憶更新免新審閱；C 區 `< 10 KB`。
- 下一個 agent 該做什麼: 無（已覆蓋基準為 `0b59dc4`）。
- 地雷警告: 無

### 2026-11-18 16:01 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示將本目錄 `AGENTS.md` 自 Online v12 整份覆蓋升級至 v13（無模板外自訂規則；覆蓋前 hash `3fbf3c8`）。為何改：同步全 12 專案憲法至 v13。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 13` 與 `Playbook-Variant: online`，全文與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v13 模板確認條文一致且 A 區進行中任務未遭改寫；並於〈阻塞點〉續列前次待審。等待 `new session` 審閱。
- 地雷警告: 無

### 2026-10-28 11:39 [maintain] 使用工具: Cursor Grok 4.7

- 完成了什麼: 使用者指示把本目錄 AGENTS.md 從 online v11 整份覆蓋成 v12。與其他 v11 檔內容相同，沒有模板外自訂規則。覆蓋前 hash e7e3698。
- 驗證方式: 讀檔首兩行是 Playbook-Version: 12 與 Playbook-Variant: online，且有「## 6. 對人訂正」。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 v12 模板，確認條文一致且 A 區進行中任務沒被改寫。等待新 session／新工具審閱。
- 地雷警告: 無


### 2026-10-22 11:15 [maintain] 使用工具: Cursor Auto

- 完成了什麼: 依 AI_AGENT_Playbook_Online.md 將本目錄 AGENTS.md 自 v10 整份覆蓋升級至 v11（online）。覆蓋前 AGENTS.md hash: 9be043f（可用 `git show .md` 找回）。v11 重點：§0 接手環境自檢／驗證方式必填／待審下壓保護；§2.1 使用者簽結與批次審閱。
- 驗證方式: 讀檔確認開頭 `<!-- Playbook-Version: 11 -->` 與 `<!-- Playbook-Variant: online -->`；內容含「接手環境自檢」「驗證方式」「待審下壓」「使用者簽結」。
- 下一個 agent 該做什麼: 無（純憲法升級；若接手請依 §0 做 hooksPath 自檢）
- 地雷警告: 無

### 2026-09-14 10:20 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示，將 AGENTS.md 升級至 Playbook v10（三層架構規範、防膨脹門檻改為 10KB、單筆長度上限約 1200 bytes、Review Loop 排除 COMPONENT_MAP.md）。
- 下一個 agent 該做什麼: 使用者明示推送到 GitHub（豁免本次審閱）。請後續接手的 agent 依各自專案階段推進任務。
- 地雷警告: 無

### 2026-08-25 17:14 [maintain] 使用工具: Claude Code

- 完成了什麼: 依 Playbook Online v9 執行分支 C 升級（原版本 v2，無 `Playbook-Variant` 標記，§2 使用 commit 為交接機制，判定為 online 變體）：`AGENTS.md` 整份覆蓋至 v9 模板（新增交接基準 commit 機制、Review Loop 順序條款、巢狀範圍條款 §4、語言與編碼規範等；§5 早已指向 LLM_MEMORY，無需再搬遷）；A 區「最新 commit」欄改名為「交接基準 commit」；`scripts/hooks/pre-commit`、`commit-msg` 整份覆蓋為最新版，並執行 `git config core.hooksPath scripts/hooks`（先前檔案存在但從未啟用，等同 hook 從未真正生效過）；新增 `.gitattributes` 的 `scripts/hooks/* text eol=lf`；README.md 頂端補上語言與編碼規範引導行。覆蓋前 `AGENTS.md` 的舊版可用 `git show a61843d:AGENTS.md` 找回。
- 下一個 agent 該做什麼: 無（純框架升級，無程式碼邏輯變更）
- 地雷警告: 無

### 2026-07-06 16:45 [maintain] 使用工具: Claude Code

- 完成了什麼: 升級 Playbook 到 v2 版本
  - AGENTS.md：整份覆蓋為 v2 模板，新增 §0 交接日誌書寫規範、§2.1 Review Loop，§5 純化為憲法條文（移除依專案填寫的技術脈絡）
  - LLM_MEMORY.md：新增〈E. 專案技術脈絡〉區塊，遷入舊 AGENTS.md §5 已填的建置指令、測試指令、程式碼慣例
  - scripts/hooks/：新建 pre-commit 與 commit-msg 兩支 hook，強制檢查 commit 訊息格式與 LLM_MEMORY.md 變更
  - git config core.hooksPath 已設為 scripts/hooks，hook 已啟用
- 下一個 agent 該做什麼: 無（本次純粹升級框架，無程式碼邏輯變更；使用者需自行 commit，訊息格式：`[maintain] 升級 AI agent 工作流至 Playbook v2`）
- 地雷警告: 無

<!-- 範例格式,新條目複製此結構插入在本註解下方:

### YYYY-MM-DD HH:MM [plan / build / maintain 擇一] 使用工具: <agent 名稱>

- 完成了什麼:
- 下一個 agent 該做什麼:
- 地雷警告: 無
-->

## D. 已封存結論(自〈總結封存〉搬入,唯讀)

## E. 專案技術脈絡

（已於 2026-11-23 依 AGENTS.md §5 移入 [COMPONENT_MAP.md](COMPONENT_MAP.md)）
