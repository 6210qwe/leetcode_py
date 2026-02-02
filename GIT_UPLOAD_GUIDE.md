# Git 上传指南

## 📋 当前上传策略

### ✅ 会上传的文件

**核心代码**:
- `leetcode_solutions/` - 所有Python源代码
- `scripts/` - 辅助脚本

**配置文件**:
- `setup.py` - 打包配置
- `pyproject.toml` - 构建配置
- `MANIFEST.in` - 文件清单
- `LICENSE` - 许可证
- `.gitignore` - Git忽略规则
- `.gitattributes` - Git属性配置

**核心文档**:
- `README.md` - 项目说明（必须）
- `CONTRIBUTING.md` - 贡献指南

**GitHub Actions**:
- `.github/workflows/publish.yml` - 自动发布工作流
- `.github/workflows/test.yml` - 自动测试工作流

### ❌ 不会上传的文件

**测试文件**:
- `test_installation.py`
- `tests/` 目录（如果存在）
- 所有 `*_test.py` 文件

**示例文件**:
- `examples/` 目录

**详细文档**（暂时不上传）:
- `build_and_upload.md`
- `GITHUB_PYPI_GUIDE.md`
- `GITHUB_SETUP.md`
- `QUICK_START_GITHUB.md`
- `QUICKSTART.md`
- `PROBLEM_FORMAT.md`
- `PROJECT_OVERVIEW.md`
- `PROJECT_STRUCTURE.md`
- `RELEASE.md`
- `SETUP_CHECKLIST.md`
- `STRUCTURE_ANALYSIS.md`
- `SUMMARY.md`
- `.github/workflows/README.md`

**构建产物**:
- `build/`
- `dist/`
- `*.egg-info/`
- `__pycache__/`

**其他临时文件**:
- 虚拟环境目录
- IDE 配置文件
- 日志文件
- 临时文件

## 🚀 上传步骤

### 1. 检查要上传的文件

```bash
# 查看哪些文件会被添加
git status

# 查看详细的忽略规则
git check-ignore -v *
```

### 2. 初始化并上传

```bash
# 初始化Git仓库
git init

# 添加文件（.gitignore会自动生效）
git add .

# 查看将要提交的文件（确认没有不需要的文件）
git status

# 提交
git commit -m "Initial commit: LeetCode solutions package"

# 添加远程仓库（替换YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/leetcode-solutions.git

# 推送
git branch -M main
git push -u origin main
```

### 3. 验证上传

在GitHub仓库页面检查：
- ✅ 只包含必要的代码和配置文件
- ✅ 没有测试文件、示例文件
- ✅ 没有构建产物
- ✅ 没有临时文件

## 📝 后续添加文档

如果以后需要添加详细文档，可以：

1. **修改 .gitignore**，移除对应的忽略规则
2. **添加文件**:
   ```bash
   git add <文档文件>
   git commit -m "Add documentation"
   git push
   ```

或者使用 `git add -f` 强制添加被忽略的文件（不推荐）。

## 🔍 检查忽略规则

```bash
# 查看哪些文件被忽略
git status --ignored

# 测试特定文件是否被忽略
git check-ignore -v <文件路径>
```

## ⚠️ 注意事项

1. **不要强制添加被忽略的文件**（除非确实需要）
2. **定期检查** `.gitignore` 是否完整
3. **提交前检查** `git status` 确认没有意外文件

