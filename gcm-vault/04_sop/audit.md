---
updated: 2026-07-12
status: active
source: 使用者對話中定案
---

# 每月稽核 SOP

## 執行時機
每月 1 日執行。

## 指令
Claude Code 開啟 Vault 後下達：

```
掃描全庫，列出：
1. updated 超過 90 天的檔案
2. 任兩檔之間數字或規格不一致處
3. 引用已標記 deprecated 內容的檔案
```

## 產出
產出 audit report（建議存於 `04_sop/audit_reports/audit_YYYYMM.md`），人工逐條裁決：
- 保留
- 更新
- 標記 deprecated

涉及外部事實的條目（平台功能、費率、法規），重新查核官方來源並更新
`06_facts/` 的日期與 `status`。

## 裁決完成後
Commit，訊息格式：`audit: 2026-07`（年-月，對應執行月份）。

## File Pruner（檔案修剪機制）
每週五執行，規則三條：
1. 同名多版只留最新版與上一版，其餘移入 `99_archive/`
2. `99_archive/` 以外不得存在標記 `status: deprecated` 的檔案
3. 任何檔案不得同時存在 Vault 與桌面兩份，桌面一律是暫存，用完即刪或歸檔

可用 `04_sop/scripts/file_pruner.py` 掃描違規檔案，人工確認後再刪除，
腳本本身不自動刪檔。
