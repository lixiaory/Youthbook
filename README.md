# 📚 青年基于知识图谱的智能图书推荐系统

<div align="center">

**[中文](README.md)** | **[English](README_EN.md)**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

一个基于知识图谱和评论关键词的智能图书推荐系统，提供可解释的推荐理由和多种自定义推荐策略。


</div>

---



## 🚀 快速开始

### 环境要求

- Python 3.8+
- 4GB+ RAM

### 安装步骤

1. **安装依赖**

```bash
pip install -r requirements.txt
```

3. **准备数据**

将原始数据文件放入 `data/raw/` 目录：
- `newBookInformation` - 图书信息
- `newCommentdata` - 评论数据

4. **启动服务**

```bash
python start.py
```

首次运行会自动构建知识图谱（约 30-60 分钟），之后启动仅需几秒。

访问 `http://localhost:5000` 即可使用。

---

## 📖 使用指南

### 基本使用

1. **添加喜欢的图书** - 在搜索框输入书名并添加
2. **选择推荐策略** - 知识图谱/关键词/混合
3. **自定义关键词**（可选）- 选择关注的特征词
4. **查看推荐结果** - 包含评分、理由和匹配度

### API 使用

```bash
POST /api/recommend
Content-Type: application/json

{
    "favorite_books": ["三体"],
    "strategy": "mixed",
    "top_k": 20
}
```

更多 API 文档请查看 `docs/guides/` 目录。

---


## 📁 项目结构

```
doubanBookComment/
├── config/                 # 配置文件
├── data/                   # 数据目录
│   ├── raw/               # 原始数据
│   ├── processed/         # 处理后的数据
│   └── resources/         # 资源文件
├── src/                    # 源代码
│   ├── core/              # 核心业务逻辑
│   └── utils/             # 工具模块
├── static/                 # 静态资源
├── templates/              # HTML模板
├── app.py                  # Flask应用
└── start.py                # 启动脚本
```

---

## 🛠️ 技术栈

- **后端**: Flask + NetworkX + Pandas + Jieba + scikit-learn
- **前端**: JavaScript + CSS3
- **算法**: 知识图谱 + TF-IDF + TextRank

---



## 📜 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️ Star！**

</div>
# Youthbook
# Youthbook
