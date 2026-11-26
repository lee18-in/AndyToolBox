# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.
>
> 三份檔案分工（`AGENTS.md`／`LLM_MEMORY.md`／[`COMPONENT_MAP.md`](./COMPONENT_MAP.md)）見 `AGENTS.md` §0。

## A. 目前狀態(每次交接必更新)

- 目前階段: build
- 最後更新: 2026-11-26 10:35 / 當時階段: maintain
- 交接基準 commit: （初始提交：整併入 AndyToolBox 清零舊版控，首次接手請以 git log -1 覆蓋）
- 遠端狀態: 已整併入 `AndyToolBox/VoltMatch/` 隨新倉首推 `origin/main`（不記雜湊，見 AGENTS.md §2）
- 進行中任務: 不同作業系統的uiux相容 畫面顯示 字形排版調整 for 不同作業系統(已完成 Circuit 電路圖區塊)
- 阻塞點: 舊版控已清零（原 15:28 v15 已於母倉 15:54 簽結；07-26/07-29/09-12 歷史檢核點存 `ARCHIVE.md`；本次整併入 `AndyToolBox`、移轉 CI 至 `../.github/workflows/voltmatch-package.yml` 與 `voltmatch-v*`、依 4A 移除 `AppDir/` 並補 `.gitignore` 待審）。；2026-11-24 16:07 初始整併待審下壓（commit `e97566f`）

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 草稿 | 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|

### B2. 短期目標(本週)

- [ ] 跨作業系統 UI/UX 相容性優化：針對不同作業系統（Windows / Linux 等）進行畫面顯示與字體排版調整，確保視覺體驗一致。

### B3. 中期目標(本月)

- [ ] 核心計算邏輯 API 化：重構計算模組，定義標準化的輸入變數與輸出格式介面，將運算邏輯與 UI 介面解耦。

### B4. 長期目標

- [ ]

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

### 2026-11-26 10:35 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「我看過 同步8倉後推」將本 dir `AGENTS.md` 自 Online v15 整份覆蓋升至 v16（精簡英文＋`ARCHIVE` 16 KB 索引規則；無模板外自訂規則；覆蓋前 hash `e97566f`）；原首筆待審依 §0 下壓入〈阻塞點〉並守原交接基準（user 明示 `>16 KB` `ARCHIVE` 索引留便宜模型另做）。為何改：全 8 倉同步 Online v16 憲法（D39）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 16`/`Playbook-Variant: online`，全文 `12,405 B`/93 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<=1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff e97566f..HEAD -- VoltMatch` 核對 Online v16 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 依 user 明示同步後 push；依 §2.1 本 context 禁自審。

### 2026-11-24 16:07 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B 3A 4A` 整併入 `AndyToolBox/VoltMatch/` 並清零舊 `.git` 歷史：(1) 移除 `AppDir/` 342 檔(25 MB)並於 `.gitignore` 補 `AppDir/`；(2) 移出重複 `scripts/hooks/` 與 `.gitattributes`（統一歸根目錄）；(3) `.github/workflows/package.yml` 上移改為 `../.github/workflows/voltmatch-package.yml`（tag 改 `voltmatch-v*`、補 `working-directory: VoltMatch`、`paths: VoltMatch/**` 與 `workflow_dispatch`，維持 `gh release create`）；(4) 同步 `COMPONENT_MAP.md`。為何改：5 工具整併瘦身並防 monorepo CI 誤觸發。
- 驗證方式: `ruby YAML.load_file` 過；`git check-ignore -v` 驗 `AppDir/` 命中且 `VoltMatch.spec` 未被擋；整檔 `<16 KB`、C 區 `<10 KB`、`COMPONENT_MAP <16 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `../.github/workflows/voltmatch-package.yml`、`AppDir/` 排除與 `COMPONENT_MAP.md` 更新。等待 new session（或 `/clear`）審閱。
- 地雷警告: 舊 commit hash 已失效，首次審結請覆蓋新倉基準；本 context 禁自審。

### 2026-11-24 15:28 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user「再部屬12區」將本 dir `AGENTS.md` 自 Online v14 整份覆蓋升至 v15（無模板外自訂規則；覆蓋前 hash `dfaabc8`）；原首筆 v14 待審依 §0 下壓入〈阻塞點〉並守原交接基準。為何改：全 12 倉同步 Online v15 憲法（D38）。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 15`/`Playbook-Variant: online`，全文 `10,219 B`/92 行與母倉逐 byte 一致；日誌 `<10 KB`、本檔 `<16 KB`、本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：`git diff b064f30..HEAD` 核對 Online v15 條文一致且 A 區進行中任務未改寫。等待 new session（或 `/clear` 清空 context，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 context 禁自審。

### 2026-11-24 14:07 [maintain] 使用工具: Antigravity (Gemini 4 Neon)

- 完成了什麼: 依使用者「12全區佈署」指示將本目錄 `AGENTS.md` 自 Online v13 整份覆蓋升級至 v14（無模板外自訂規則；覆蓋前 hash `f21f89f`）；保留原交接基準待審。為何改：全 12 倉同步 Online v14 憲法。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 14` 與 `Playbook-Variant: online`，全文 `10,191 B`/89 行與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 逐位元組一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v14 模板確認條文一致且 A 區進行中任務未遭改寫。等待 `new session`（或 `/clear` 清空 `context`，建議換模型）審閱。
- 地雷警告: 未 push；依 §2.1 本 `context` 禁自審。

### 2026-11-18 19:39 [maintain] 使用工具: Antigravity

- 完成了什麼: 使用者於 2026-11-18 19:39 明示「我看過結案」，依 §2.1 正式簽結 v12／v13 憲法升級及 §0 分流（`COMPONENT_MAP.md`／`ARCHIVE.md`），自〈阻塞點〉移除（保留既有待決／待審項與原基準）。
- 驗證方式: `git diff --name-only` 僅異動 `LLM_MEMORY.md`；純記憶更新免新審閱；C 區 `< 10 KB`。
- 下一個 agent 該做什麼: 由新 session 批次審結 07-26、07-29 與 09-12 歷史待審。
- 地雷警告: 無

### 2026-11-18 16:59 [maintain] 使用工具: Antigravity

- 完成了什麼: 依 AGENTS.md §0 防膨脹維護整理雙記憶檔：(1) `COMPONENT_MAP.md` 校正 #5／#13（記明 `e3090d2` `filter-repo` 已清歷史）與 §7 LF 實況，並將已取代 Playbook v10 歷史條目（#8–#12、附帶發現）移入 `ARCHIVE.md` 降至 16 KB 以下；(2) 將 2026-07-26～09-03 18:13 四筆舊日誌移入 `ARCHIVE.md` 並壓縮入〈D〉（待審檢查點保留於〈阻塞點〉）；(3) 2026-11-18 16:01 v13 待審下壓至〈阻塞點〉。為何改：雙檔超 10 KB／16 KB 門檻。
- 驗證方式: `python3` 驗 `C. 交接日誌` 降至 4.4 KB（`<10KB`）、`COMPONENT_MAP.md` `<16KB`、本筆 `<1200B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 `COMPONENT_MAP.md` 校正與分流無誤、且 `ARCHIVE.md` 完整留存 (1)(2) 待審原文（與〈阻塞點〉前次待審可批次審結）。等待 `new session` 審閱。
- 地雷警告: 舊 SHA 因 `filter-repo` 失效；未 push。

### 2026-11-18 16:01 [maintain] 使用工具: Antigravity

- 完成了什麼: 依使用者指示將本目錄 `AGENTS.md` 自 Online v12 整份覆蓋升級至 v13（無模板外自訂規則；覆蓋前 hash `61c6934`）。為何改：同步全 12 專案憲法至 v13。
- 驗證方式: `head -n 2 AGENTS.md` 為 `Playbook-Version: 13` 與 `Playbook-Variant: online`，全文與 `Andy_AI_AGENT_WorkFlow/AGENTS.md` 一致。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 Online v13 模板確認條文一致且 A 區進行中任務未遭改寫；並於〈阻塞點〉續列前次待審。等待 `new session` 審閱。
- 地雷警告: `COMPONENT_MAP.md` 約 16.3 KB（>16 KB），接續工作須依 v13 §0 三向分流；〈交接日誌〉約 12.0 KB（>10 KB），接續工作須依 §0 壓縮

### 2026-10-28 11:39 [maintain] 使用工具: Cursor Grok 4.7

- 完成了什麼: 使用者指示把本目錄 AGENTS.md 從 online v11 整份覆蓋成 v12。與其他 v11 檔內容相同，沒有模板外自訂規則。覆蓋前 hash b064f30。
- 驗證方式: 讀檔首兩行是 Playbook-Version: 12 與 Playbook-Variant: online，且有「## 6. 對人訂正」。
- 下一個 agent 該做什麼: 本次改動需要審閱：對照 v12 模板，確認條文一致且 A 區進行中任務沒被改寫。等待新 session／新工具審閱。
- 地雷警告: 無


### 2026-10-22 11:15 [maintain] 使用工具: Cursor Auto

- 完成了什麼: 依 AI_AGENT_Playbook_Online.md 將本目錄 AGENTS.md 自 v10 整份覆蓋升級至 v11（online）。覆蓋前 AGENTS.md hash: 2c02728（可用 `git show .md` 找回）。v11 重點：§0 接手環境自檢／驗證方式必填／待審下壓保護；§2.1 使用者簽結與批次審閱。
- 驗證方式: 讀檔確認開頭 `<!-- Playbook-Version: 11 -->` 與 `<!-- Playbook-Variant: online -->`；內容含「接手環境自檢」「驗證方式」「待審下壓」「使用者簽結」。
- 下一個 agent 該做什麼: 無（純憲法升級；若接手請依 §0 做 hooksPath 自檢）
- 地雷警告: 無
### 2026-09-12 11:17 [build] 使用工具: Claude Opus 5 (Cursor)

- 完成了什麼: 使用者裁示 A2（**明確保留 B2 AppDir/**）：`git filter-repo` 僅移除 `bin/VoltMatch*.AppImage`／`bin/*.exe`；AppDir/ 342 檔仍在版控。`.git` 95M→13M。
- 下一個 agent 該做什麼: 本次改動需要審閱: AppDir 保留是否仍符合預期；bin 安裝檔改走 Releases。等待新 session 審閱。
- 地雷警告: 未 push；待使用者確認後 force-push（覆寫遠端歷史）。filter-repo 後舊 SHA 全部失效。

### 2026-09-12 10:47 [build] 使用工具: Claude Opus 5 (Cursor)

- 完成了什麼: 全機 repo 同步比對時,發現本 repo 工作樹有未提交的 `bin/VoltMatch-x86_64.AppImage` 刪除。依使用者 10:45 裁示提交(42.1MB 移出索引),並在 `.gitignore`〈Binary files〉區 `*.exe` 後補 `*.AppImage`。理由與「未 rewrite history」後果見 `COMPONENT_MAP.md` §6 #13;驗證見同檔 §8 新增兩列。使用者明示 push。
- 下一個 agent 該做什麼: 本次改動需要審閱: ①`*.AppImage` 置於全域〈Binary files〉區(非 `bin/` 限定)是否過寬——若未來要版控範例 AppImage 會被擋;②`bin/` 現已無任何版控檔案,確認 README〈⬇️ Download〉段與 `package.yml` 是否有指向 `bin/` 的路徑失效(本次未檢查);③42.1MB 仍在 git 歷史,是否要裁示 rewrite history。續行 B2 Windows 實機驗證 UI。等待新 session/新工具審閱。
- 地雷警告: 接手時 `core.hooksPath` 為空,hook 未生效(已於 10:39 對本機 12 個 repo 重設,並經反向測試確認兩支 hook 均能攔截);此設定不隨 clone 帶過來,換機器必須重設,已記入 `COMPONENT_MAP.md` §8。

## D. 已封存結論(自〈總結封存〉搬入,唯讀)

原文保留於 [`ARCHIVE.md`](./ARCHIVE.md)；不衰減知識已萃取至 [`COMPONENT_MAP.md`](./COMPONENT_MAP.md)。

- **2026-09-03 18:13 [build]** 新 session 審閱通過 Playbook v10 升級（`0e0176e..HEAD`），細節見 `COMPONENT_MAP.md` §8。
- **2026-09-03 18:04 [build]** `AGENTS.md` 升級至 Playbook v10、重構 `COMPONENT_MAP.md` 8 節並封存 10 筆舊日誌至 `ARCHIVE.md`。
- **2026-07-29 17:33 [build]** `.gitignore` 補 `.venv*/` 並 `git rm -r --cached .venv2`（2225 檔）；Ubuntu 安裝 uv 0.12.0；待審 3 檢核點見 `ARCHIVE.md` 與〈阻塞點〉。
- **2026-07-26 22:25 [build]** 新增 `tags: ["v*"]` release job 與 README〈⬇️ Download〉改版（`config.py` 版號 `26.0726.1`）；待審 3 檢核點見 `ARCHIVE.md` 與〈阻塞點〉。
- **2026-09-03 11:26 [build]** 建立 `COMPONENT_MAP.md` 初版（同日由 v10 重構取代）。
- **2026-08-27 [build] / 08-24 / 07-26 21:55** 移出 `bin/VoltMatch.exe`、`環境部屬.md` 補 Linux 指令、`CircuitCanvas` 動態排版防無限重繪（詳 `COMPONENT_MAP.md` §6–§8）。
- **2026-07-05～07-06** 導入 AI 工作流並升級 Playbook v1→v2，驗證 Git Hooks 攔截正常。

## E. 專案技術脈絡(依專案填寫,agent 得隨專案實況更新,保持精簡)

自 Playbook v10 起，建置／測試指令與程式碼慣例改記於 [`COMPONENT_MAP.md`](./COMPONENT_MAP.md) §1（不衰減層）——這類資訊不會過期作廢，不該放在會被封存的本檔。
