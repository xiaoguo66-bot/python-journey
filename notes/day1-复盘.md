# Day 1 复盘（2026-09-21）

> 目标：把“我要学 Python”变成“我已经在学了”。今晚结束时，这条已经成立。

## 一、今天完成了什么

| # | 事项 | 状态 |
|---|---|---|
| 1 | Python 3.11.9 环境确认（3.11 够用，不必追 3.12） | 完成 |
| 2 | Git 全局用户已配置（`xiaoguo66-bot`） | 完成 |
| 3 | VS Code 已安装 | 完成 |
| 4 | 建本地仓库 `D:\pythonwork` | 完成 |
| 5 | 首次提交 `27c79e5`（README + .gitignore） | 完成 |
| 6 | GitHub 建远端仓库 `python-journey`（Public） | 完成 |
| 7 | 推送到远端，本地与远程绑定成功 | 完成 |
| 8 | 在 GitHub 网页改 README → 本地 pull 同步 | 完成 |
| 9 | 本地改 README（加 "go go go"）→ 提交 → 推送 | 完成，且修复了 SSL 报错 |

**仓库地址**：https://github.com/xiaoguo66-bot/python-journey

## 二、Git 核心概念（必须内化）

### 四个区域
```
工作区  --git add-->  暂存区  --git commit-->  本地仓库  --git push-->  远程仓库(GitHub)
   ↑                                                                        ↓
   └──────────────────────  git pull  ←────────────────────────────────────┘
```
- **暂存区为什么存在**：一次改了 5 个文件，可以只挑 2 个提交。`add` = 挑哪些要存档，`commit` = 真的存档。
- `.git` 目录装着全部历史，删了它 = 仓库历史消失（文件还在）。

### 每天的三行循环
```bash
git add -A
git commit -m "feat: 今天做了什么"
git push origin main
```
### 提交信息前缀（约定式提交）
| 前缀 | 含义 |
|---|---|
| `feat:` | 新功能 / 新脚本 |
| `fix:` | 修 bug |
| `docs:` | 文档、笔记 |
| `test:` | 测试 |
| `chore:` | 配置、杂事 |

### 救命命令
| 场景 | 命令 |
|---|---|
| 查看当前状态（最常用，没有之一） | `git status` |
| 看历史提交 | `git log --oneline` |
| 看改动内容 | `git diff` |
| 撤销某文件的修改 | `git restore 文件名` |
| 全部回退到上次提交（慎用） | `git reset --hard` |
| 看当前连的是哪个远端 | `git remote -v` |
| 看自己在哪个目录 | `pwd`（Git Bash）/ `cd`（CMD） |

### VS Code 图形界面（日常最省事）
`Ctrl+Shift+G` 打开源代码管理 → 点文件旁的 `+`（= add）→ 写信息 → `Ctrl+Enter`（= commit）→ 点「同步更改」（= pull + push）。

## 三、今天踩的 5 个坑（复盘价值最高的部分）

### 坑 1：人在错误的文件夹里敲命令
提示：`MINGW64: ~/OneDrive/桌面 (master)` —— 你在桌面目录，不在 `D:\pythonwork`。
后果：`git remote add` 报错 `already exists`（桌面本身也是个 Git 仓库，origin 指向另一个项目）。
**教训：敲命令前先看终端提示符最前面那行路径。**

### 坑 2：GitHub 用户名写错
正确是 `xiaoguo66-bot`，不是 `xiaoguo66`（少了 `-bot`）。

### 坑 3：CMD 的 `cd` 不跨盘符
在 `C:\Users\26982>` 敲 `cd D:\pythonwork` 只是“记住了 D 盘该去哪”，人没动。
正确写法：`cd /d D:\pythonwork`，或直接 `code D:\pythonwork`。

### 坑 4：`code` 不带参数
不带参数会恢复上次会话（打开了以前 PHP 项目的旧标签页）。
正确：`code D:\pythonwork` —— 用 VS Code 打开文件夹，内置终端自动定位到该目录，坑 1 直接归零。

### 坑 5：VS Code 提示“文件系统是只读的”
原因：打开的是**对比视图**（标签页标题形如 `README.md (27c79e5) → README.md (313a2a1)`），这种视图天生只读。
判断：**标题带括号和箭头 = 只读对比视图；光秃秃的文件名 = 能编辑的真文件。**
解决：`Ctrl+Shift+E` 回到资源管理器 → 双击文件名打开。

### 坑 6（附）：SSL 证书报错 `unable to get local issuer certificate (20)`
Git 的 OpenSSL 后端在这台机器上找不到根证书库。
修法（一条命令，全局永久生效）：
```bash
git config --global http.sslBackend schannel
```
改用 Windows 系统证书库。换电脑或重装 Git 后再遇到，还是这条命令。

## 四、一条最重要的规矩

**先拉，后推。尽量别在 GitHub 网页上改文件。**
网页改了会在本地不知情的情况下多出一个提交，下次 push 必被拒。
标准流程：本地改 → 提交 → 同步更改。

## 五、Day 2 任务（明天）

- **学**：w3schools 的 Variables / Data Types / If...Else / While / For 五节
- **写**（放 `D:\pythonwork\scripts\`）：
  1. `grade.py` —— 输入分数，输出 优秀 / 及格 / 不及格
  2. `seven.py` —— 打印 1-100 中能被 7 整除的数，并统计有几个
- **收尾**：`git add -A` → `git commit -m "feat: Day2 变量与循环练习"` → 同步更改

两个提前点破的坑：
- `input()` 拿到的永远是**字符串**，比较大小前要 `int()` 转换
- 计数用 `count += 1`（等价 `count = count + 1`）

## 六、两条支线任务（别只推主线）

1. **问应届身份**：去学校就业指导中心 / 当地人社局确认「26 届、未缴社保，能否按应届身份应聘」。这个答案会改变整体求职策略。
2. **投相关岗位**：IT 技术支持、桌面运维、IDC 机房运维、NOC。门槛不高，上班就在攒相关经验。

## 七、当前定位（暂定，可调整）

- 方向：**测试开发（主）> Python 后端（争取）**；运维开发先降为备选
- 时间预算：工作日 2 小时 + 周末 4-6 小时 ≈ 每周 20 小时，12 周约 240 小时
- 主项目方向：**短链服务 + pytest 自动化测试**（一个项目同时覆盖测开与后端两个方向）
- 12 周红线：**不碰** Unity 深挖、AI 应用、爬虫、Django、第二本教程
