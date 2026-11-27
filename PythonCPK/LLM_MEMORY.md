# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: build
- 最後更新: 2026-11-27 10:11 / 當時階段: maintain
- 交接基準 commit: （初始提交：整併入 AndyToolBox 清零舊版控，首次接手請以 git log -1 覆蓋）
- 進行中任務: 等待新 session/新工具審閱 `package.yml` 與 `.gitignore` 異動（CI 實測已通過，見〈交接日誌〉最上方條目的檢查點 1-5）
- 阻塞點: 舊版控已清零（原 15:28 v15 已於母倉 15:54 簽結；2026-07-26 `package.yml`＋`.gitignore` 5 檢核點見 `ARCHIVE.md`；本次整併入 `AndyToolBox` 並移轉 CI 至 `../.github/workflows/pythoncpk-package.yml` 與 `pythoncpk-v*` 合併待審）。；2026-11-24 16:07 初始整併待審下壓（commit `e97566f`）；2026-11-26 10:35 v16 升級待審下壓（基準 `3bd0bf7..HEAD -- PythonCPK`）

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ 測試是否正常 ]

### B3. 中期目標(本月)

- [ ]

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-11-27 10:11 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「推 全倉 套WF」將本 dir `AGENTS.md` 自 Online v16 整份覆蓋升至 v17（§5 禁假優缺點＋§1 `[build]` PDCA Act 閉環；無模板外自訂規則；覆蓋前 hash `611c967`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 8 倉同步 Online v17 憲法（D41）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 17`/`Playbook-Variant: online`，全文 `12,791 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff 3bd0bf7..HEAD -- PythonCPK` 核對 Online v17 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-26 10:35 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「我看過 同步8倉後推」將本 dir `AGENTS.md` 自 Online v15 整份覆蓋升至 v16（精簡英文＋`ARCHIVE` 16 KB 索引規則；無模板外自訂規則；覆蓋前 hash `e97566f`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準（user 明示 `>16 KB` `ARCHIVE` 索引留便宜模型另做）。為何改：全 8 倉同步 Online v16 憲法（D39）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 16`/`Playbook-Variant: online`，全文 `12,405 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff e97566f..HEAD -- PythonCPK` 核對 Online v16 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-24 16:07 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B 3A` 整併入 `AndyToolBox/PythonCPK/` 並清零舊 `.git` 歷史；移出重複 `scripts/hooks/` 與 `.gitattributes`（統一歸根目錄）；原 `.github/workflows/package.yml` 上移改為 `../.github/workflows/pythoncpk-package.yml`（tag 改 `pythoncpk-v*`、補 `working-directory: PythonCPK` 與根相對路徑）；同步更新 `COMPONENT_MAP.md`。為何改：5 工具整併並避免 monorepo `v*` tag 衝突。
- 驗證方式: `ruby YAML.load_file` 過；`app.py`/`DATA.csv`/`requirements.txt`/`.gitignore` 完整；整檔 `<16 KB`、C 區 `<10 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `../.github/workflows/pythoncpk-package.yml` 路徑與 `pythoncpk-v*` guard 及 `COMPONENT_MAP.md` 同步。等待 new session（或 `/clear`）審閱。
- 地雷警告: 舊 commit hash 已失效，首次審結請覆蓋新倉基準；本 context 禁自審。

### 2026-11-24 15:28 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「再部屬12區」將本 dir `AGENTS.md` 自 Online v14 整份覆蓋升至 v15（無模板外自訂規則；覆蓋前 hash `f23cddd`）；原首筆 v14 待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 12 倉同步 Online v15 憲法（D38）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 15`/`Playbook-Variant: online`，全文 `10,219 B`/92 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff d752f91..HEAD` 核對 Online v15 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 context 禁自審。

### 2026-11-24 14:05 [maintain] 使用工具: Antigravity (Gemini 4 Neon)

- 完成了什麼: 依使用者「12全區佈署」指示將本目錄 `AGENTS.md` 自 Online v13 整份覆蓋升級至 v14（無模板外自訂規則；覆蓋前 hash `352c7f7`）；保留原交接基準待審。為何改：全 12 倉同步 Online v14 憲法。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 14` 與 `Playbook-Variant: online`，全文 `10,191 B`/89 行與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 逐位元組一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v14 模板確認條文一致且 A 區進行中任務未遭改寫。等待 `new session`（或 `/clear` 清空 `context`，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 `context` 禁自審。

### 2026-11-18 19:39 [maintain] 使用工具: Antigravity

- 完成了什麼: 使用者於 2026-11-18 19:39 明示「我看過結案」，依 §2.1 正式簽結 v12／v13 憲法升級及 §0 記憶整理（`COMPONENT_MAP.md`／`ARCHIVE.md`），自〈阻塞點〉移除（保留既有待決／待審項與原基準）。
- 驗證方式: `git diff --name-only` 僅異動 `LLM_MEMORY.md`；純記憶更新免新審閱；C 區 `< 10 KB`。
- 下一個 agent 該做什麼: 由新 session 審結 2026-07-26 `package.yml` 與 `.gitignore`（`a4aeac2..34cccec`）。
- 地雷警告: 無

### 2026-11-18 16:59 [maintain] 使用工具: Antigravity

- 完成了什麼: 依 AGENTS.md §0 防膨脹維護執行記憶整理：(1) 建立 `COMPONENT_MAP.md`，自〈E〉與 2026-07-26～08-25 舊日誌完整萃取專案結構、發版契約、`.gitignore`／Pillow 地雷與 CI 驗證台帳；(2) 將 2026-08-25～07-06 舊日誌移入 `ARCHIVE.md` 並壓縮入〈D〉（2026-07-26 待審 5 檢查點已寫入〈阻塞點〉）；(3) 2026-11-18 16:01 v13 待審依下壓抄入〈阻塞點〉。為何改：〈交接日誌〉超 10 KB 且補齊三層架構。
- 驗證方式: `python3` 驗 `C. 交接日誌` 降至 2.8 KB（`<10KB`）、`COMPONENT_MAP.md` 2.6 KB（`<16KB`）、本筆 `<1200B`、時間戳嚴格遞減。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對新建 `COMPONENT_MAP.md`（已萃取技術脈絡與 07-26 知識無遺漏）及 `ARCHIVE.md` 完整性（與〈阻塞點〉前次待審可批次審結）。等待 `new session` 審閱。
- 地雷警告: 無

### 2026-11-18 16:01 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示將本目錄 `AGENTS.md` 自 Online v12 整份覆蓋升級至 v13（無模板外自訂規則；覆蓋前 hash `5cfe749`）。為何改：同步全 12 專案憲法至 v13。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 13` 與 `Playbook-Variant: online`，全文與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v13 模板確認條文一致且 A 區進行中任務未遭改寫；並於〈阻塞點〉續列前次待審。等待 `new session` 審閱。
- 地雷警告: 〈交接日誌〉約 12.0 KB（>10 KB），接續工作須依 §0 壓縮

### 2026-10-28 11:39 [maintain] 使用工具: Cursor Grok 4.7

- 完成了什麼: 使用者指示把本目錄 AGENTS.md 從 online v11 整份覆蓋成 v12。與其他 v11 檔內容相同，沒有模板外自訂規則。覆蓋前 hash d752f91。
- 驗證方式: 讀檔首兩行是 Playbook-Version: 12 與 Playbook-Variant: online，且有「## 6. 對人訂正」。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 v12 模板，確認條文一致且 A 區進行中任務沒被改寫。等待新 session／新工具審閱。
- 地雷警告: 無


### 2026-10-22 11:15 [maintain] 使用工具: Cursor Auto

- 完成了什麼: 依 AI_AGENT_Playbook_Online.md 將本目錄 AGENTS.md 自 v10 整份覆蓋升級至 v11（online）。覆蓋前 AGENTS.md hash: 537bb5f（可用 `git show .md` 找回）。v11 重點：§0 接手環境自檢／驗證方式必填／待審下壓保護；§2.1 使用者簽結與批次審閱。
- 驗證方式: 讀檔確認開頭 `<!-- Playbook-Version: 11 -->` 與 `<!-- Playbook-Variant: online -->`；內容含「接手環境自檢」「驗證方式」「待審下壓」「使用者簽結」。
- 下一個 agent 該做什麼: 無（純憲法升級；若接手請依 §0 做 hooksPath 自檢）
- 地雷警告: 無


### 2026-09-14 10:20 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示，將 AGENTS.md 升級至 Playbook v10（三層架構規範、防膨脹門檻改為 10KB、單筆長度上限約 1200 bytes、Review Loop 排除 COMPONENT_MAP.md）。
- 下一個 agent 該做什麼: 使用者明示推送到 GitHub（豁免本次審閱）。請後續接手的 agent 依各自專案階段推進任務。
- 地雷警告: 無

## D. 已封存結論(自〈交接日誌〉搬入,唯讀)

原文保留於 [`ARCHIVE.md`](./ARCHIVE.md)；不衰減知識已萃取至 [`COMPONENT_MAP.md`](./COMPONENT_MAP.md)。

- **2026-08-25 16:04 [maintain]** `AGENTS.md` 升級至 Playbook v9，同步更新 `scripts/hooks/` 與〈交接基準 commit〉欄；舊版 v2 存於 `4462419`。
- **2026-07-26 [build]** `.github/workflows/package.yml` 補齊 `workflow_dispatch`、`upload-artifact@v4` 與 `refs/tags/` guard（CI run `30203433189` 綠燈）；新增 `.gitignore` 8 規則並移除 `.pyc` 追蹤；README 調整為 H3 分段版式；07-26 待審 5 檢查點保留於〈阻塞點〉。
- **2026-07-06 [plan/build]** 導入 Playbook v1→v2 並推送 `7ca4b86..7b6d112`。

## E. 專案技術脈絡

自 Playbook v10 起，建置／測試指令與發版契約改記於 [`COMPONENT_MAP.md`](./COMPONENT_MAP.md)（不衰減層），不再記載於本檔。
