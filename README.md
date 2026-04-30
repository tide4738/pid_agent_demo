# PID-Agent-Demo

一个用 Python 编写的 PID 控制仿真小项目，用来演示“Planner / Executor / Reviewer”式闭环 Agent 如何通过多轮评估和参数调整，逐步优化控制效果。

## 项目特点

- 使用 `PIDAgent` 模拟控制器参数自动调节。
- 使用 `IndustrialPlant` 模拟一个简化的工业对象。
- 支持多轮仿真、指标评估和参数自优化。
- 最终绘制初始控制结果与优化后结果的对比曲线。

## 运行环境

- Python 3.9 或更高版本
- `numpy`
- `matplotlib`

## 安装依赖

```bash
pip install numpy matplotlib
```

## 运行方式

在项目根目录执行：

```bash
python pid_agent_sim.py
```

运行后会：

1. 先进行一次初始仿真。
2. 再执行 3 轮闭环优化。
3. 输出每轮评估结果。
4. 弹出曲线图，展示优化前后的过程变量变化。

## 项目结构

```text
PID-Agent-Demo/
├── pid_agent_sim.py
└── README.md
```

## 可扩展方向

- 引入更真实的被控对象模型。
- 将 PID 参数调整策略改成搜索算法或强化学习策略。
- 增加结果保存功能，比如导出为图片或 CSV。
- 把单文件脚本拆分为模块化项目，方便后续扩展。

## 说明

这个项目目前是一个演示型脚本，适合用来展示控制优化和 Agent 闭环思路。如果你希望，我可以继续帮你补充 `requirements.txt`、`.gitignore`，或者把它整理成一个更适合发布到 GitHub 的完整仓库结构。
