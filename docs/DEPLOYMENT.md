# 部署指南 - Books API

## 重要说明

**根据评分标准，部署到外部平台是必须的：**
- 40-49分：可以不部署（但分数受限）
- 50-59分及以上：**必须**部署到外部服务器（如PythonAnywhere）

## 推荐部署平台

### 1. PythonAnywhere（最推荐）

**优点：**
- 免费套餐可用
- 专为Python/Django优化
- 配置简单
- 课程示例明确提到

**步骤：**

1. **注册账号**
   - 访问 https://www.pythonanywhere.com/
   - 使用GitHub账号或邮箱注册（免费版足够）

2. **创建GitHub仓库**（如果还没有）
   ```bash
   cd /Users/king/Documents/大四/大四下/Web_coursework/books_api
   git init
   git add .
   git commit -m "Initial commit: Books API complete"
   # 在GitHub创建仓库后推送
   git remote add origin https://github.com/YOUR_USERNAME/books-api.git
   git push -u origin main
   ```

3. **在PythonAnywhere上**
   - 点击 "Web" 标签页
   - 点击 "Add a new web app"
   - 选择 "Manual configuration" (非Django特定)
   - Python版本选择 3.9 或更高

4. **克隆仓库**
   ```bash
   # 在PythonAnywhere的Bash终端中
   cd ~
   git clone https://github.com/YOUR_USERNAME/books-api.git
   cd books-api
   ```

5. **设置虚拟环境**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 books-api-venv
   workon books-api-venv
   pip install -r requirements.txt
   ```

6. **配置环境变量**
   ```bash
   # 创建.env文件（可选，用于生产环境）
   echo "DJANGO_SETTINGS_MODULE=books_api.settings" > .env
   echo "DEBUG=False" >> .env
   ```

7. **运行迁移**
   ```bash
   cd ~/books-api
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

8. **加载样例数据**（可选）
   ```bash
   python seed_data.py
   ```

9. **配置WSGI文件**
   - 在PythonAnywhere的Web标签页，点击进入WSGI配置文件
   - 修改为：
   ```python
   import os
   import sys

   path = '/home/yourusername/books-api'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'books_api.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

10. **设置静态文件**
    - 在Web标签页的Static files部分添加：
      - URL: /static/
      - Path: /home/yourusername/books-api/staticfiles

11. **重新加载Web应用**
    - 点击Reload按钮

12. **验证部署**
    - 访问 `https://yourusername.pythonanywhere.com/api/docs/`
    - 应该看到Swagger文档界面

---

### 2. Heroku（备选）

**优点：** 免费层（需信用卡验证）
**缺点：** 配置稍复杂，有休眠限制

```bash
# 创建Procfile
echo "web: gunicorn books_api.wsgi:application" > Procfile

# 安装heroku cli并部署
heroku create books-api-YourName
git push heroku main
heroku run python manage.py migrate
```

---

### 3. Railway（现代选择）

- 连接GitHub自动部署
- 免费额度
- 简单配置

---

## 部署检查清单

- [ ] 代码已推送到GitHub（公开仓库）
- [ ] requirements.txt 包含所有依赖
- [ ] .gitignore 排除敏感文件
- [ ] 数据库迁移已运行
- [ ] 静态文件配置正确
- [ ] API文档可访问
- [ ] 测试API端点正常工作
- [ ] 样例数据已加载（可选）

## 常见问题

**Q: 部署后API无法访问？**
A: 检查WSGI配置、Python路径、依赖安装

**Q: 静态文件404？**
A: 确保运行 `collectstatic` 并正确配置static files

**Q: 数据库错误？**
A: 确认迁移已运行，SQLite文件有写入权限

**Q: 如何更新部署？**
A: 推送代码到GitHub，PythonAnywhere会自动拉取（需配置）

## 生产环境建议

1. **更换SECRET_KEY**
   - 使用 `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - 更新settings.py中的SECRET_KEY

2. **禁用DEBUG模式**
   - 在settings.py中设置 `DEBUG = False`

3. **配置ALLOWED_HOSTS**
   - 添加你的域名：`ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']`

4. **使用PostgreSQL**（可选）
   - 更适合生产环境
   - 需要安装 `psycopg2-binary`

## 验证部署成功

访问以下URL验证：
- `https://yourusername.pythonanywhere.com/api/` - API根
- `https://yourusername.pythonanywhere.com/api/docs/` - Swagger文档
- `https://yourusername.pythonanywhere.com/api/books/` - 书籍列表

应该看到JSON响应或Swagger界面。

---

**下一步：** 创建GitHub仓库并推送到云端！
