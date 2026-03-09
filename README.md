# Email WeChat Notifier

<h4 align="center">
    <p>
        <b>English<b> | <a href="https://github.com/QinCheng0928/MailWeChat/blob/main/docs/README_zh.md">简体中文</a>
    </p>
</h4>



This is a lightweight Python-based script designed for **periodically monitoring unread emails** in your inbox. Upon detecting a new email, it extracts the subject and sender details and pushes a notification to your WeChat via **ServerChan**.


### ✨ **Key Features**

- **Automated Monitoring:** Runs automatically at fixed intervals using GitHub Actions (customizable).
- **Instant Push:** Receive email alerts on WeChat via the ServerChan API; never miss an important notification again.
- **Secure & Reliable:** All sensitive information (passwords, keys) is stored in GitHub Secrets to prevent leaks.
- **Serverless:** Runs entirely on GitHub's free cloud environment—no personal server required.

### 🚀 Quick Start

#### 🛠️ Step 1: Preparation (Email & Push Service)

1. **Enable Email IMAP Service:** Log in to your webmail provider, locate the **IMAP/SMTP Service** in settings, and enable it. The system will provide a 16-digit random string; this is the `EMAIL_PASS` used in the code.
2. **Get ServerChan Key:** Visit the [ServerChan Website](https://sct.ftqq.com/), log in via WeChat, and copy your **SendKey** (usually starting with `SCT`) from the **Key & API** section.

#### 🛠️ Step 2: Configure GitHub Repository

1. **Fork the Repository:** Ensure your GitHub repository contains `main.py` and `.github/workflows/main.yml`.
2. **Set Up Secrets:**
   - Navigate to your repository **Settings** -> **Secrets and variables** -> **Actions**.
   - Click **New repository secret** and add the following four values:
     - `IMAP_SERVER`: e.g., `imap.qq.com`, `imap.163.com`, or `imap.gmail.com`
     - `EMAIL_USER`: Your full email address, e.g., `yourname@qq.com`
     - `EMAIL_PASS`: The 16-digit authorization code, e.g., `snitcyuzpbgdbca`
     - `SC_KEY`: The ServerChan SendKey obtained earlier, e.g., `SCT12345T7890abcdef...`

#### 🧪 Step 3: Manual Testing

Manually trigger the GitHub Actions workflow to verify the setup:

1. Select the **Email Checker** workflow on the left sidebar of the **Actions** tab.
2. Click the **Run workflow** dropdown menu on the right and click the green **Run workflow** button.
3. Wait a moment and check if the task displays a green checkmark. If a red "X" appears, click into the logs to check the `Run script` step for errors.

#### 📈 Step 4: Daily Automated Monitoring

1. **Automatic Execution:** Based on your `run.yml` configuration, GitHub will automatically launch the script every 2 hours (at the 11th minute of the hour).
2. **Receive Notifications:** As long as there are **unread emails**, you will receive a WeChat notification such as "New Email: [Subject]".
3. **Note:** Scheduled GitHub Actions tasks may experience minor delays due to cloud resource scheduling; this is normal behavior.