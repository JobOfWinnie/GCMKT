---
updated: 2026-07-12
status: needs-verification
source: 使用者對話中提供之描述，尚未對照 SurveyCake／綠界官方文件查核（本次網路政策未阻擋這兩個網域，但尚未執行查核動作）
---

# 事實查核：SurveyCake 與綠界（ECPay）平台功能

## 已知（來自使用者描述，待官方文件覆核）
- SurveyCake 是問卷／名單收集工具，非金流工具，不能直接收款。
- 綠界（ECPay）是 API 型金流，可提供收款連結頁。
- 零程式碼可行路線：SurveyCake 表單收資料 → 導向綠界收款連結頁 → SurveyCake
  自訂感謝頁轉址 → 觸發完成通知與自動回信。
- SurveyCake 免費版每月回覆數上限：100 份。

## 爭議事項（來源：七份既有素材交叉比對，2026-07-12，詳見 contradiction_audit_2026-07.md 5.1）
七份素材中一份（Gemini／Genspark／Grok）主張 SurveyCake **專業版（PRO）**
有內建付款設定，可在後台直接填入綠界 MerchantID／HashKey／HashIV 完成站內
收款；另兩份（ChatGPT／Claude、Manus／Perplexity）與使用者原始任務說明皆
主張 SurveyCake 不能直接收款，必須靠「自訂感謝頁導向綠界收款連結頁」的
零程式碼路線。**目前 SOP 採多數意見（導頁法），Gemini 的「PRO 內建站內
付款」說法尚未官方查證，不得作為 SOP 依據，僅記錄於此待查證。**

## 待查核動作
- 至 SurveyCake 官方定價頁核對免費版回覆數上限是否仍為每月 100 份，
  以及付費升級的實際級距與價格。
- 至 SurveyCake 官方文件查證 PRO 版是否真的有內建綠界站內付款設定功能
  （見上方爭議事項）。
- 至綠界官方文件核對收款連結（隨buy／Payment Button）功能是否仍支援
  零程式碼串接，以及目前實際信用卡手續費率（目前 Excel 記帳表暫用 2.75%
  為假設值，非查證數字）。
- 查核後更新本檔 `status: active` 並附上具體查核日期與網址來源。
