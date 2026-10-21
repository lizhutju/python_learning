# Phase 1 · Python 基础学习

按天推进的 Python 学习练习。每个目录对应一天，内容从输出语句一路到模块拆分与导入。

## 目录结构

```
Phase1/
├── Day01/                  # 第一个程序
│   └── hello.py
├── Day02/                  # 文件与 CSV 读写
│   ├── main.py
│   └── students.csv
├── Day03/                  # 列表推导、生成器、set、模块拆分
│   ├── main.py
│   ├── statistics_utils.py
│   └── practice/           # 可独立运行的练习版本
│       ├── main.py
│       ├── demo.py
│       └── statistics_utils.py
└── README.md
```

## 每日知识点

| 天 | 主题 | 关键内容 |
| --- | --- | --- |
| Day01 | 第一个程序 | `print()`、字符串字面量、单引号与双引号 |
| Day02 | 文件与数据 | `csv.DictReader`、`pathlib.Path`、字典、函数定义与返回元组 |
| Day03 | 数据处理进阶 | 生成器 `yield`、`sorted` + `key`+`reverse`、`set` 去重计数、模块导入与 `__main__` 守卫 |

## 运行方式

每个脚本都可以独立运行，无需安装依赖（仅用标准库）：

```bash
cd Phase1
python3 Day01/hello.py
python3 Day02/main.py
python3 Day03/main.py
python3 Day03/practice/main.py
python3 Day03/practice/demo.py
```

脚本内部使用 `Path(__file__).resolve().parent` 定位数据文件，所以在任意工作目录下运行结果都一致。

## 约定

- 所有脚本以 `if __name__ == "__main__":` 收尾，模块被 `import` 时不执行主流程。
- `practice/` 目录自带一份 `statistics_utils.py`，保证练习版本可以独立运行。
- 练习中涉及边界情况时（如空列表求平均），代码会显式做保护而不是直接崩溃。

## 下一步

- [ ] 给每个练习补充 `assert` 断言，覆盖边界情况
- [ ] Day04：异常处理（`try/except`）与文件写入
- [ ] Day05：面向对象（类与实例）
