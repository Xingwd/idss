# FDS

金融数据源(Financial Data Source)

## 环境配置

### 配置Selenium环境

Selenium 支持多种浏览器，但是 FDS 目前只支持 Chrome，所以请使用 Chrome 并安装 chromedriver。

chromedriver 版本需要和本地 Chrome 浏览器版本保持大版本一致。

chromedriver下载地址： `https://chromedriver.storage.googleapis.com/index.html`。

本节以下内容均摘自 [安装浏览器驱动](https://www.selenium.dev/zh-cn/documentation/getting_started/installing_browser_drivers/)。

大多数驱动程序需要 Selenium 额外的可执行文件才能与浏览器通信。您可以在启动 WebDriver 之前手动指定可执行文件的存放位置，但这会使测试的可移植性降低，因为可执行文件必须位于每台 计算机上的同一位置，或包含在测试代码存储库中。

通过将包含 WebDriver 二进制文件的文件夹添加到系统 path 环境变量中，Selenium 将能够找到其他二进制文件，而无需您的测试代码来定位驱动程序的确切位置。

- 创建一个目录来放置可执行文件，例如 `C:\WebDriver\bin` 或 `/opt/WebDriver/bin`
- 将目录添加到您的 path 中：
  - 在 Windows 上 - 以管理员身份打开命令提示符，然后运行以下命令将目录永久添加到计算机上所有用户的路径中：

    ```shell
    setx PATH "%PATH%;C:\WebDriver\bin"
    ```

  - 在 macOS 和 Linux 上的 Bash 用户 - 在终端中：

    ```shell
    export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile
    ```

- 现在您可以测试更改了。关闭所有打开的命令提示符，然后打开一个新的提示符。 输入您在上一步创建的文件夹中的某一个二进制文件的名称，例如：

    ```shell
    chromedriver
    ```

    如果您的 PATH 配置正确，您将看到一些有关驱动程序启动的输出：

    ```shell
    Starting ChromeDriver 2.25.426935 (820a95b0b81d33e42712f9198c215f703412e1a1) on port 9515
    Only local connections are allowed.
    ```

    您可以通过按 `Ctrl + C` 重新获得对命令提示符的控制。
