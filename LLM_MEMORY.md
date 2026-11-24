# LLM_MEMORY.md — 工作記憶(agent 讀寫;規則見 AGENTS.md,勿在此重複)

> - **Language and Encoding Standards**: All system files, code annotations, memory files (`LLM_MEMORY.md`), and handover logs for this project are uniformly encoded in **UTF-8** and **Traditional Chinese** by default.

## A. 目前狀態(每次交接必更新)

- 目前階段: maintain
- 最後更新: 2026-11-24 16:06 / 當時階段: maintain
- 交接基準 commit: （初始提交：整併 5 倉清零舊版控，首次接手請以 git log -1 覆蓋）
- 進行中任務: 完成 5 工具整併為 AndyToolBox（1B/2B/3A/4A/5A）並推送至公開遠端倉，待 new session 審閱或 user 簽結。
- 阻塞點: 初始整併提交（5 工具搬遷、根/子三檔架構、3 支 monorepo CI workflow、VoltMatch 排除 AppDir）待審。

## B. 規劃(規劃階段 [plan] 專屬區;狀態: 已定案)

### B1. 架構決策(已定案後鎖定,建置/維運階段不得改)

| # | 決策 | 理由 | 狀態 |
|---|------|------|------|
| 1 | 5 工具清版控整併單倉、巢狀獨立三檔、CI 上移前綴 tag、踢除 `VoltMatch/AppDir` | 見同 dir `COMPONENT_MAP.md` §2（user 拍板 `1B 2B 3A 4A 5A`） | 已定案 |

### B2. 短期目標(本週)

- [x] 建立 `AndyToolBox` 根層骨架、搬入 5 工具、改寫 3 支 monorepo CI workflow 並推上公開遠端倉
- [ ] 完成初始整併審閱（或 user 簽結）並確認遠端 5 舊倉刪除狀態

### B3. 中期目標(本月)

- [ ] 實測各工具前綴 tag 或 `workflow_dispatch` CI 打包流程

### B4. 長期目標

- [ ] 維持根層與 5 子工具獨立交接與憲法同步

## C. 交接日誌(只追加,不刪改;最新在最上,每筆一個小節)

<!-- 規則見 AGENTS.md §0/§2；標題：### YYYY-MM-DD HH:MM [階段] <工具>；欄：完成了什麼/驗證方式/下一個 agent 該做什麼/地雷警告 -->

### 2026-11-24 16:06 [maintain] Antigravity (Gemini 4 Neon)

- 完成了什麼: 依 user 拍板 `1B 2B 3A 4A 5A` 建立 `AndyToolBox`：(1) 建根三檔(`AGENTS.md` v15)、`README`/`.gitattributes`/`.gitignore` 與模板 6 `scripts/hooks/`；(2) 純工作檔遷入 5 工具留獨立子三檔(去重複 `.git`/`scripts/`/`.gitattributes`/`.github/` 與 `VoltMatch/AppDir/` 342 檔)；(3) 3 支 `package.yml` 上移改前綴 tag(`pythoncpk-v*`/`qrcode-v*`/`voltmatch-v*`) 與 `working-directory`/`paths`。為何改：5 工具整併降維護並清膨脹。
- 驗證方式: `hooksPath=scripts/hooks`；`ruby YAML.load_file` 驗 3 支 workflow 過；`git check-ignore -v` 驗 `VoltMatch/AppDir/` 命中且 `VoltMatch.spec` 未被擋；6 處 `AGENTS.md` 一致(`10,219 B`)、全數記憶 `<16 KB`/日誌 `<10 KB`/本筆 `<1200 B`。
- 下一個 agent 該做什麼: 本次改動需要審閱：核對 5 工具檔案、3 支 monorepo workflow、`.gitignore` 未誤擋 `VoltMatch.spec` 及 6 套三檔架構。等待 new session（或 `/clear`）審閱。
- 地雷警告: 初始提交無既有基準 hash，審結後請覆蓋為首筆 commit；本 context 禁自審。

## D. 已封存結論(自〈交接日誌〉壓縮搬入,唯讀)

<!-- 專案技術脈絡（建置指令、測試指令、程式碼慣例）自 v10 起一律記載於同目錄的 COMPONENT_MAP.md（見 AGENTS.md §0）。 -->
