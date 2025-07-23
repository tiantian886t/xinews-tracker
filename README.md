# 🌐 Xinews Tracker

这是一个自动化系统，用于全球追踪关于“习近平 / Xi Jinping / 習近平”的新闻文章和视频，并通过 Telegram 机器人第一时间推送。

## ✅ 功能
- 每 5 分钟自动监控 Google News、BBC、VOA、RFA 等新闻源
- 匹配关键词后立即推送到 Telegram
- 可通过 GitHub Actions 实现 24 小时云端运行

## 📦 如何使用

1. 上传所有代码到你的 GitHub 仓库（建议命名为 `xinews-tracker`）
2. 打开仓库 → Settings → Secrets → Actions
3. 添加两个加密变量：
   - `TG_BOT_TOKEN`：你的 Telegram Bot Token
   - `TG_USER_ID`：你的 Telegram 数字 ID
4. 打开仓库的 "Actions" 页面，点击 `Run workflow` 测试一次
5. 成功后每 5 分钟自动运行，实时追踪新闻！

---

由 ChatGPT 为 tiantian886t 专属定制 🚀