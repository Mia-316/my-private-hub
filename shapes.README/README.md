# Shapes - Python 图形类设计

> 一个基于面向对象继承与工厂模式设计的 Python 图形类库，提供统一的图形抽象基类与四种具体图形实现。

## 项目简介

本项目为软件工程训练营第一次作业成果，使用 Python 的抽象基类（ABC）与继承机制，设计了一套可扩展的图形类体系。核心目标是演示面向对象设计原则中的**继承（Inheritance）**、多态（Polymorphism）与工厂模式（Factory Pattern）在实际代码中的应用。

## 特性一览

- 抽象基类 `Shape` 定义统一接口，规范所有图形子类的行为
- 四种具体图形实现：`Square`（正方形）、`Rectangle`（长方形）、`Triangle`（三角形）、`Circle`（圆形）
- 内置工厂函数 `create_shape`，根据类型名称动态创建对应图形对象
- 完善的参数校验机制，确保输入数据的合法性与一致性
- 清晰的文档字符串与类型注解，代码可读性强

## 架构设计

### 类继承关系

```
┌─────────────────────┐
│      Shape (ABC)    │
│  - shape_type: str  │
│  - dimensions: dict   │
│  - validate()       │
│  - required_fields()│
└──────────┬──────────┘
           │
    ┌──────┼──────┬────────┐
    ▼      ▼      ▼        ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Square│ │Rectan│ │Triang│ │Circle│
│      │ │ gle  │ │  le  │ │      │
└──────┘ └──────┘ └──────┘ └──────┘
```

### UML 类图

![Shapes.py UML 类继承关系图](shapes_uml.png)

### 模块结构

```
shapes.py
├── Shape (抽象基类)
│   ├── __init__(dimensions)
│   ├── validate()          # 参数校验
│   └── required_fields()   # 抽象方法：子类实现
│
├── Square (正方形)
│   └── required_fields() → ("side",)
│
├── Rectangle (长方形)
│   └── required_fields() → ("length", "width")
│
├── Triangle (三角形)
│   └── required_fields() → ("base", "height")
│
├── Circle (圆形)
│   └── required_fields() → ("diameter",)
│
└── create_shape()          # 工厂函数
```

## 快速开始

### 环境要求

- Python 3.9 或更高版本

### 使用示例

```python
from shapes import create_shape

# 创建正方形：边长 5.0 厘米
square = create_shape("square", {"side": 5.0})

# 创建长方形：长 5.0 厘米、宽 3.0 厘米
rectangle = create_shape("rectangle", {"length": 5.0, "width": 3.0})

# 创建三角形：底 6.0 厘米、高 4.0 厘米
triangle = create_shape("triangle", {"base": 6.0, "height": 4.0})

# 创建圆形：直径 2.0 厘米
circle = create_shape("circle", {"diameter": 2.0})
```

### 参数说明

| 图形类型   | 参数名称               | 说明         | 数据类型   |
|------------|------------------------|--------------|------------|
| `square`   | `side`                 | 边长         | 正浮点数   |
| `rectangle`| `length`, `width`      | 长、宽       | 正浮点数   |
| `triangle` | `base`, `height`       | 底边长、高   | 正浮点数   |
| `circle`   | `diameter`             | 直径         | 正浮点数   |

> **数据约定**：所有长度数据在进入本模块前必须已换算为**厘米**。

## 错误处理

模块内置完善的参数校验，会在以下场景抛出 `ValueError`：

```python
# 1. 不支持的图形类型
create_shape("hexagon", {"side": 5.0})
# → ValueError: 不支持的图形类型: 'hexagon'

# 2. 缺少必需参数
create_shape("rectangle", {"length": 5.0})
# → ValueError: 缺少必需参数: width（图形类型: rectangle）

# 3. 参数值非正数
create_shape("square", {"side": -5.0})
# → ValueError: 参数 side 的值必须大于 0

# 4. 参数值非数字
create_shape("circle", {"diameter": "abc"})
# → ValueError: 参数 diameter 的值不是有效数字
```

## 测试运行

模块底部包含完整的自测代码，直接运行文件即可执行全部测试用例：

```bash
python shapes.py
```

**预期输出：**

```
[PASS] create_shape 返回正确的子类实例
[PASS] 各子类返回正确的字段名
[PASS] 无效图形类型抛出 ValueError
[PASS] 缺少参数时抛出 ValueError
[PASS] 非正数参数抛出 ValueError
[PASS] 继承关系正确

全部测试通过!
```

## 设计亮点

### 1. 抽象基类规范接口

使用 `abc.ABC` 定义抽象基类 `Shape`，强制所有子类实现 `required_fields()` 方法，确保接口一致性。

### 2. 统一校验逻辑

基类提供 `validate()` 方法，统一处理参数缺失、类型错误和值域检查，避免在各子类中重复编写校验代码。

### 3. 工厂模式解耦

`create_shape()` 工厂函数封装对象创建逻辑，调用方无需关心具体子类的构造细节，新增图形类型时对调用方透明。

### 4. 类型注解

全模块使用 Python 类型注解（如 `dict[str, float]`、`tuple[str, ...]`），提升代码可维护性和 IDE 支持。

## 作者信息

- **姓名**：王菲
- **学号**：U202412692
- **课程**：软件工程训练营
- **日期**：2026年8月

## 许可证

本项目仅用于教学演示，未经允许不得用于商业用途。
