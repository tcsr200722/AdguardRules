# AdguardRules 

![CI](https://github.com/YOUSIKI/AdguardRules/workflows/CI/badge.svg)

利用 Github Actions 定期收集、更新网络上的 Adguard 规则并同步到 Gitee 仓库 (https://gitee.com/yousiki/AdguardRules)，方便在国内网络环境下使用。

## 这个项目为什么存在

许多 Adguard 规则都在 github 或境外服务器上维护，然而在国内网络环境下常常无法访问这些网站，导致 Adguard 自动更新失败。每天为了更新过滤器规则需要手动开启其他上网手段，这就非常不优雅。

## 这个项目的工作原理

在 `rules.txt` 中列出了我收集到的网络上的许多过滤器地址，`downloader.py` 脚本会读取其中的 URLs 并将过滤器文件下载到 `rules` 文件夹下。
配置 Github Actions （见 `.github/workflows/main.yml`）每天运行一次该下载脚本，向 `LAST_UPDATED` 文件写入运行时间，并更新 Github 和 Gitee 仓库。

## 如何使用本项目

在 https://gitee.com/yousiki/AdguardRules/tree/master/rules 中找到你想使用过滤器，获取原始数据地址并将其添加到 Adguard 自定义过滤器中。
例如，如果想使用 `easylist.txt` 则将 `https://gitee.com/yousiki/AdguardRules/raw/master/rules/easylist.txt` 添加到 Adguard 中。

## Contribute

欢迎通过 PR 加入更多过滤器。
