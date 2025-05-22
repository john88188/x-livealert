[English Version](./README.en.md)

# 预警机器人（xAI Live Search 方案）

基于 xAI Live Search API 的自动化实时预警与发帖机器人。

---

## 项目简介
本项目可自动定时检索互联网最新内容，基于关键词筛选后，利用 AI 生成摘要并自动发布到 X（Twitter），适用于危机、突发事件等实时预警场景。
本项目主要是提供**创意**，项目本身未经验证，除特别说明外，否则不会进行维护。

---

## 功能模块
1. **Live Search**：定时（默认60秒）根据关键词实时检索最新内容。
2. **grok_analyzer**：对检索结果进行智能分析，生成简洁预警摘要。
3. **x_poster**：将摘要内容自动发布到 X（Twitter）。

---

## 安装与运行

### 1. 克隆仓库
```bash
git clone <repo_url>
cd <repo_dir>
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
需设置以下环境变量（可写入 .env 文件或系统环境变量）：
- `XAI_API_KEY`：xAI API 密钥
- `X_API_KEY`、`X_API_SECRET`、`X_ACCESS_TOKEN`、`X_ACCESS_TOKEN_SECRET`：X（Twitter）API 密钥

### 4. 配置关键词
编辑 `config/settings.py`，修改 `KEYWORDS` 列表即可自定义监控关键词。

### 5. 运行项目
```bash
python run.py
```

---

## 目录结构
```
project_root/
│
├── config/
│   ├── __init__.py
│   ├── settings.py         # 关键词与参数配置
│   └── logging_config.py   # 日志配置（自动创建 logs 目录）
│
├── src/
│   ├── __init__.py
│   ├── main.py             # 主流程
│   ├── data/
│   │   ├── __init__.py
│   │   └── live_search.py  # 实时检索
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── keyword_matcher.py
│   │   └── grok_analyzer.py
│   └── notification/
│       ├── __init__.py
│       └── x_poster.py     # 自动发帖
│
├── requirements.txt
├── run.py                  # 启动入口
└── README.md
```

---

## 依赖
- openai==1.30.0
- tweepy==4.14.0

---

## 日志
日志文件自动写入 `logs/alert_bot.log`，首次运行会自动创建 logs 目录。

---

## 注意事项
- 请确保所有 API KEY 均已正确设置，否则程序会自动退出并记录错误日志。
- 关键词可随时在 `config/settings.py` 中调整。
- 适用于 Python 3.8 及以上版本。

---

## 联系与支持
如需定制开发、部署支持或遇到问题，欢迎联系项目维护者。

[SamGor三哥](https://x.com/biggor888)

---

[English Version Below](./README.en.md)