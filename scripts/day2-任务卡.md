# Day 2 任务卡（2026-09-21）

## 学（30 分钟，快速过一遍即可）

w3schools Python 教程这五节：
1. Python Variables
2. Python Data Types
3. Python If...Else
4. Python While Loops
5. Python For Loops

**不要逐字精读**。看标题→看示例代码→自己敲一遍→往下走。目标是"知道有这个东西"，细节用到再查。

## 写（1-1.5 小时，本目录）

### 练习 1：`grade.py`
输入一个分数（0-100），输出评级：
- 90 分及以上 → `优秀`
- 60 分及以上 → `及格`
- 60 分以下 → `不及格`

提示：
- `input()` 拿到的是**字符串**，要用 `int()` 转数字才能比较大小
- 三个分支用 `if / elif / else`
- 加分项：输入的不是数字时，提示"请输入数字"而不是崩溃

### 练习 2：`seven.py`
打印 1-100 中所有能被 7 整除的数，并在最后输出一共有几个。

提示：
- 循环用 `for i in range(1, 101)`（`range` 顾头不顾尾，所以是 101）
- 判断整除用 `i % 7 == 0`（`%` 是取余，余数为 0 就是能整除）
- 计数：循环外 `count = 0`，循环内满足条件时 `count += 1`
- 加分项：用一行列表推导式 `nums = [i for i in range(1, 101) if i % 7 == 0]`，然后 `len(nums)` 就是个数

## 跑（在 Git Bash 终端里）

```bash
python grade.py
python seven.py
```

如果提示 `python: command not found`，换 `py grade.py` 或 `python3 grade.py` 试。

## 收尾（必须做）

```bash
git add -A
git commit -m "feat: Day2 变量与循环练习"
git push origin main
```

## 自检清单

- [ ] 两个脚本都能跑通，输出结果正确
- [ ] 代码里没有冗余的重复判断
- [ ] 提交信息写清楚了今天做了什么
- [ ] GitHub 上能看到今天的提交
