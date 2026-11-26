# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: maintain
- 最後更新: 2026-11-26 10:35 / 當時階段: maintain
- 交接基準 commit: （初始提交：整併入 AndyToolBox 清零舊版控，首次接手請以 git log -1 覆蓋）
- 進行中任務: 測試現有功能，邊用邊測發現並修復 bug
- 阻塞點: 舊版控已清零（原 15:28 v15 已於母倉 15:54 簽結；2026-11-23 `COMPONENT_MAP`/`ARCHIVE` 補建與本次整併入 `AndyToolBox`、移轉 CI 至 `../.github/workflows/qrcode-package.yml` 與 `qrcode-v*` 合併待審）。；2026-11-24 16:07 初始整併待審下壓（commit `e97566f`）

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ ] 我幫妳測試應用功能，發現並記錄 bug

### B3. 中期目標(本月)

- [ ]

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-11-26 10:35 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「我看過 同步8倉後推」將本 dir `AGENTS.md` 自 Online v15 整份覆蓋升至 v16（精簡英文＋`ARCHIVE` 16 KB 索引規則；無模板外自訂規則；覆蓋前 hash `e97566f`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準（user 明示 `>16 KB` `ARCHIVE` 索引留便宜模型另做）。為何改：全 8 倉同步 Online v16 憲法（D39）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 16`/`Playbook-Variant: online`，全文 `12,405 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff e97566f..HEAD -- QrcodeGenerator` 核對 Online v16 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-24 16:07 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B 3A` 整併入 `AndyToolBox/QrcodeGenerator/` 並清零舊 `.git` 歷史；移出重複 `scripts/hooks/` 與 `.gitattributes`（統一歸根目錄）；原 `.github/workflows/package.yml` 上移改為 `../.github/workflows/qrcode-package.yml`（tag 改 `qrcode-v*`、增 `workflow_dispatch` 與 `refs/tags/qrcode-v` guard、補 `working-directory: QrcodeGenerator`）；同步更新 `COMPONENT_MAP.md`。為何改：5 工具整併並避免 monorepo tag 衝突。
- 驗證方式: `ruby YAML.load_file` 過；`QrcodeGenerator.py`/`assets/qrcodegenerator.png`/`requirements.txt`/`.gitignore` 完整；整檔 `<16 KB`、C 區 `<10 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `../.github/workflows/qrcode-package.yml` 路徑與 `qrcode-v*` guard 及 `COMPONENT_MAP.md` 同步。等待 new session（或 `/clear`）審閱。
- 地雷警告: 舊 commit hash 已失效，首次審結請覆蓋新倉基準；本 context 禁自審。

### 2026-11-24 15:28 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「再部屬12區」將本 dir `AGENTS.md` 自 Online v14 整份覆蓋升至 v15（無模板外自訂規則；覆蓋前 hash `b3ba39f`）；原首筆 v14 待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 12 倉同步 Online v15 憲法（D38）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 15`/`Playbook-Variant: online`，全文 `10,219 B`/92 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff ee26633..HEAD` 核對 Online v15 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 context 禁自審。

### 2026-11-24 14:07 [maintain] 使用工具: Antigravity (Gemini 4 Neon)

- 完成了什麼: 依使用者「12全區佈署」指示將本目錄 `AGENTS.md` 自 Online v13 整份覆蓋升級至 v14（無模板外自訂規則；覆蓋前 hash `ce7601a`）；併合遠端 `cdc83e4` 補建之 `COMPONENT_MAP.md`／`ARCHIVE.md` 與 09-12 審結紀錄，保留遠端基準 `ee26633` 並將 11-23 待審下壓入〈阻塞點〉。為何改：全 12 倉同步 Online v14 憲法。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 14` 與 `Playbook-Variant: online`，全文 `10,191 B`/89 行與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 逐位元組一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v14 模板確認條文一致且 A 區進行中任務未遭改寫、`COMPONENT_MAP.md` 萃取與舊日誌壓縮無遺失。等待 `new session`（或 `/clear` 清空 `context`，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 `context` 禁自審。

### 2026-11-23 17:00 [maintain] 使用工具: Antigravity

- 完成了什麼: ①依 §2.1 獨立審結 `2026-09-12`（`48d6b16`/`384646a`）通過：`venv*/` 僅配目錄、無 tracked `.spec`、`README.md` 無殘留 `bin/` 連結、Releases 與 `package.yml` 完整、`filter-repo` 已瘦身，清阻塞點並覆蓋基準 `ee26633`；②依 2A 建 `COMPONENT_MAP.md`、依 §0 移 07-05～09-12 10:46 五筆至 `ARCHIVE.md` 並壓入 D 區；③啟用 `core.hooksPath`。為何改：補三檔並防日誌超 10 KB。
- 驗證方式: `hooksPath=scripts/hooks`；`git check-ignore -v venv/ .venv2/ build/ dist/ foo.spec bin/test.AppImage bin/test.exe` 全命中；對讀 `README.md`／`package.yml`；`python3` 驗本筆 `<1200 B`、C 區 `<10 KB`、`COMPONENT_MAP <16 KB`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對新建 `COMPONENT_MAP.md` 與 `ARCHIVE.md` 無遺漏不衰減事實與原文。等待 `new session` 審閱。
- 地雷警告: 接手自檢原 `core.hooksPath` 空，已設 `scripts/hooks` 並 `chmod +x`；僅本地提交未 `push`。

### 2026-11-18 19:39 [maintain] 使用工具: Antigravity

- 完成了什麼: 使用者於 2026-11-18 19:39 明示「我看過結案」，依 §2.1 正式簽結 v12／Online v13 憲法升級，自〈阻塞點〉移除（保留既有待決／待審項與原基準）。
- 驗證方式: `git diff --name-only` 僅異動 `LLM_MEMORY.md`；純記憶更新免新審閱；C 區 `< 10 KB`。
- 下一個 agent 該做什麼: 由新 session 審結 2026-09-12 `venv/bin` 移出版控。
- 地雷警告: 無

### 2026-11-18 16:01 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示將本目錄 `AGENTS.md` 自 Online v12 整份覆蓋升級至 v13（無模板外自訂規則；覆蓋前 hash `913e111`）。為何改：同步全 12 專案憲法至 v13。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 13` 與 `Playbook-Variant: online`，全文與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v13 模板確認條文一致且 A 區進行中任務未遭改寫；並於〈阻塞點〉續列前次待審。等待 `new session` 審閱。
- 地雷警告: 無

### 2026-10-28 11:39 [maintain] 使用工具: Cursor Grok 4.7

- 完成了什麼: 使用者指示把本目錄 AGENTS.md 從 online v11 整份覆蓋成 v12。與其他 v11 檔內容相同，沒有模板外自訂規則。覆蓋前 hash 9c9f1b6。
- 驗證方式: 讀檔首兩行是 Playbook-Version: 12 與 Playbook-Variant: online，且有「## 6. 對人訂正」。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 v12 模板，確認條文一致且 A 區進行中任務沒被改寫。等待新 session／新工具審閱。
- 地雷警告: 無


### 2026-10-22 11:15 [maintain] 使用工具: Cursor Auto

- 完成了什麼: 依 AI_AGENT_Playbook_Online.md 將本目錄 AGENTS.md 自 v10 整份覆蓋升級至 v11（online）。覆蓋前 AGENTS.md hash: 4d40941（可用 `git show .md` 找回）。v11 重點：§0 接手環境自檢／驗證方式必填／待審下壓保護；§2.1 使用者簽結與批次審閱。
- 驗證方式: 讀檔確認開頭 `<!-- Playbook-Version: 11 -->` 與 `<!-- Playbook-Variant: online -->`；內容含「接手環境自檢」「驗證方式」「待審下壓」「使用者簽結」。
- 下一個 agent 該做什麼: 無（純憲法升級；若接手請依 §0 做 hooksPath 自檢）
- 地雷警告: 無

### 2026-09-14 10:20 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示，將 AGENTS.md 升級至 Playbook v10（三層架構規範、防膨脹門檻改為 10KB、單筆長度上限約 1200 bytes、Review Loop 排除 COMPONENT_MAP.md）。
- 下一個 agent 該做什麼: 使用者明示推送到 GitHub（豁免本次審閱）。請後續接手的 agent 依各自專案階段推進任務。
- 地雷警告: 無

### 2026-09-12 11:17 [maintain] 使用工具: Claude Opus 5 (Cursor)

- 完成了什麼: 使用者裁示 A1：`git filter-repo` 自歷史徹底移除 `bin/*.AppImage`／`bin/*.exe`／`venv/`。`.git` 65M→180K。gitignore 規則已存在，無需再改。
- 下一個 agent 該做什麼: 本次改動需要審閱: 確認 Releases 流程仍可取得安裝檔。等待新 session 審閱。
- 地雷警告: 未 push；待使用者確認後 force-push（覆寫遠端歷史）。filter-repo 後舊 SHA 全部失效。

## D. 已封存結論(自〈總結封存〉搬入,唯讀)

- **2026-07-05 ～ 2026-09-12 10:46（5 筆完整日誌已搬入 [ARCHIVE.md](ARCHIVE.md)）**：完成 Playbook 導入與 v9 升級、切換 `maintain` 階段、修復 `.gitignore` 引號失效（改 `venv*/`/`.venv*/` 與建置產物規則並移出 1,327 檔 `venv/` 與 `bin/`，已於 11-23 審結）。不衰減技術契約見 [COMPONENT_MAP.md](COMPONENT_MAP.md)。

## E. 專案技術脈絡

（已於 2026-11-23 依 AGENTS.md §5 移入 [COMPONENT_MAP.md](COMPONENT_MAP.md)）
