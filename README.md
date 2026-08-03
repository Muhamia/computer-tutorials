# computer-tutorials

这是计算机教程的源代码仓库。

- [在线阅读](http://muhamia.github.io/computer-tutorials/)
- [离线 PDF 下载](https://github.com/Muhamia/computer-tutorials/releases)

## 构建方式

### 在线阅读版

使用 MkDocs 构建，在 GitHub Pages 中部署。

源码推送到 `main` 分支后 **不会** 自动部署。需要手动触发 GitHub Actions（ `.github/workflows/deploy.yml` ）才会重新构建并发布网页。

两种触发方式：

1. 命令行： `gh workflow run deploy.yml` （需安装 [GitHub CLI](https://cli.github.com/) 并登录）。

2. 进入仓库的 Actions 页面，选中“Deploy MkDocs”，点击“Run workflow”。

### 离线版

PDF 使用 Pandoc 或 MkDocs 构建（未定），在 Releases 页面中不定期发布。
