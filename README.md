# qa-mastery-roadmap
Caoxu's personal QA laboratory. 

曹旭的个人质量保障实验室。

Focusing on practical automation frameworks, test platform development, and exploring the application of AI in software testing. 

专注于实战自动化框架、测试平台开发，并探索AI在软件测试中的应用。

Documenting the roadmap to becoming a senior Test Architect. 

记录迈向高级测试架构师的成长路线图。

# 目录树

caoxu-qa-lab/   # 项目根目录
│
├── test-theory/               # 软件测试理论
│   ├── 1-testing-basics.md           # 测试基础、原则、V模型、W模型等
│   ├── 2-test-design-techniques.md   # 等价类、边界值、判定表等
│   ├── 3-test-process.md             # 测试计划、用例、报告
│   └── 4-defect-management.md        # 缺陷生命周期、缺陷报告
│
├── computer-basics/     # 计算机基础
│   ├── 1-network.md                 # HTTP/HTTPS, TCP/IP, 状态码
│   ├── 2-operating-system.md        # 进程与线程
│   └── 3-data-structures-algorithms.md
│
├── linux/               # Linux 技能
│   ├── notes/                       # 笔记目录
│   │   ├── 1-file-system-commands.md   # ls, cd, cp, mv, find
│   │   ├── 2-text-processing.md        # grep, awk, sed, vim
│   │   ├── 3-process-network.md        # ps, top, netstat, curl
│   │   └── 4-environment-setup.md      # 环境变量、权限管理
│   └── scripts/                     # 练习脚本
│       └── health_check.sh
│
├── database/            # 数据库
│   ├── notes/
│   │   ├── 1-SQL-basics.md            # 增删改查、聚合函数
│   │   ├── 2-advanced-SQL.md          # 多表JOIN、子查询、索引
│   │   └── 3-non-relational.md        # Redis基础与测试场景
│   └── sql-scripts/                  # 练习的SQL脚本
│       ├── create_test_db.sql
│       └── sample_queries.sql
│
├── python/              # Python 编程
│   ├── notes/
│   │   ├── 1-basics.md                # 数据类型、循环、函数
│   │   ├── 2-oop.md                   # 类、对象、继承
│   │   └── 3-modules-packages.md      # pip、虚拟环境
│   ├── projects/                      # 练习代码
│   │   └── calculator/
│   └── learning_log.md
│
├── interface-test/      # 接口测试
│   ├── notes/
│   │   ├── 1-http-api-concepts.md     # RESTful, 常见请求方法
│   │   ├── 2-postman-newman.md
│   │   └── 3-session-cookie-token.md
│   └── postman-collections/           # 存放导出的postman文件
│
├── automation-test/     # 自动化测试
│   ├── notes/
│   │   ├── 1-selenium-webdriver.md
│   │   ├── 2-page-object-model.md
│   │   └── 3-pytest-unittest.md
│   ├── framework-demo/                # Web UI自动化代码
│   │   ├── pages/
│   │   ├── tests/
│   │   └── conftest.py
│   └── requirements.txt
│
├── performance-test/    # 性能测试
│   ├── notes/
│   │   ├── 1-core-concepts.md         # 并发、TPS、响应时间
│   │   ├── 2-jmeter-basics.md
│   │   └── 3-locust-usage.md
│   └── jmeter-plans/                  # 存放.jmx脚本
│
├── test-development/    # 测试开发
│   ├── notes/
│   │   ├── 1-platform-ideas.md        # 造数平台、用例平台设计
│   │   └── 2-pytest-hook.md
│   └── sandbox/                       # 动手写的工具
│       └── create_test_data.py
│
├── other-skills/        # 其他测试相关技能
│   ├── 1-git-version-control.md
│   ├── 2-docker-basics.md
│   ├── 3-ci-cd.md
│   └── 4-charles-fiddler.md
│
└── README.md               