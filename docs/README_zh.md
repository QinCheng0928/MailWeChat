# 邮件微信通知助手
这是一个基于 Python 的轻量级脚本，用于**定时监控电子邮箱中的未读邮件**。当检测到新邮件时，它会提取邮件主题和发件人，并通过**Server酱**推送到你的微信公众号。

<h4 align="center">
    <p>
        <a href="https://github.com/QinCheng0928/MailWeChat/blob/main/README.md">English</a> | <b>简体中文</b>
    </p>
</h4>

### ✨ **主要功能**

- **自动监控：**利用 GitHub Actions 固定时间自动运行（可自定义）。
- **及时推送：**通过Server酱API实现微信接收邮件提醒，不再错过重要通知。
- **安全可靠**：所有敏感信息（密码、密钥）均存储在 GitHub Secrets 中，不会泄露。 
- **无需服务器**：完全运行在 GitHub 的免费云端环境中。

### 🚀 快速开始

#### 🛠️ 第一步：准备工作 (邮箱与推送服务)

1. **开启邮箱IMAP服务：**登录您的网页版邮箱，在设置中找到 **IMAP/SMTP 服务**并开启。系统会给你一个 16 位的随机字符串，这是代码中的 `EMAIL_PASS`。
2. **获取Server酱Key：**访问 [Server酱官网](https://sct.ftqq.com/)，使用微信扫码登录，在**Key&API**版面复制**SendKey**，通常以SCT开头。

#### 🛠️ 第二步：配置 GitHub 仓库

1. **Fork仓库：**确保您的 GitHub 仓库中包含 `main.py` 和 `.github/workflows/main.yml`。
2. **设置 Secrets：**
   - 进入仓库的 **Settings** -> **Secrets and variables** -> **Actions**。
   - 点击 **New repository secret**，依次添加以下四个值：
     - `IMAP_SERVER`：例如`imap.qq.com`，`imap.163.com`，`imap.gmail.com`
     - `EMAIL_USER`: 完整邮箱账号，例如`yourname@qq.com`
     - `EMAIL_PASS`: 获取16位的随机字符串，例如`snitcyuzpbgdbca`
     - `SC_KEY`: 刚才获取Server酱的SendKey，例如`SCT12345T7890abcdef...`

#### 🧪 第三步：手动测试

手动触发GitHub Actions运行：

1. 在左侧选中 **Email Checker** 工作流。
2. 点击右侧的 **Run workflow** 下拉菜单，点击绿色的 **Run workflow** 按钮。
3. 稍等片刻，观察任务是否显示为绿色对勾。如果显示红色叉号，点击进去查看 `Run script` 步骤的错误日志。

#### 📈 第四步：日常自动监控

1. **自动执行**：根据您的`run.yml`配置，GitHub 每隔 2 小时（在第 11 分钟时）会自动启动一次。
2. **接收推送**：只要有**未读邮件**，您的微信就会收到类似“新邮件：[邮件标题]”的通知。
3. **注意**：GitHub Actions 的定时任务可能存在延迟，这是正常的云端资源调度现象。

