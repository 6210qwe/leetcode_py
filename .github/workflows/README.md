# GitHub Actions 工作流说明

## 工作流文件

### 1. publish.yml - 自动发布到 PyPI

**触发条件**:
- 推送版本标签（格式：`v*`，如 `v0.1.0`）
- 手动触发（在 Actions 页面点击 "Run workflow"）

**执行步骤**:
1. 检出代码
2. 设置 Python 环境
3. 安装构建工具（build, twine）
4. 构建包
5. 检查包
6. 发布到 PyPI
7. 创建 GitHub Release（如果推送了标签）

**所需 Secrets**:
- `PYPI_API_TOKEN`: PyPI API token

### 2. test.yml - 自动测试

**触发条件**:
- 推送到 main/master/develop 分支
- 创建 Pull Request

**执行步骤**:
1. 在多平台（Ubuntu, Windows, macOS）测试
2. 多 Python 版本（3.8, 3.9, 3.10, 3.11）测试
3. 安装包
4. 运行测试

## 使用方式

### 发布新版本

```bash
# 1. 更新版本号
# 2. 提交更改
git commit -m "Bump version to 0.1.1"
git push origin main

# 3. 创建标签（触发发布）
git tag v0.1.1
git push origin v0.1.1
```

### 手动触发

在 GitHub 仓库的 Actions 页面，选择工作流，点击 "Run workflow"。


















