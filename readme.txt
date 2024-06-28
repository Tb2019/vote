解压文件，web文件夹是一个完整的项目，在pycharm中打开

1、安装Django
	pip install django

2、设置运行ip：进入mysite/settings.py
	ALLOWED_HOSTS = ['***', 'localhost', '127.0.0.1']
	***填入本机ip,使得服务可以在指定ip启动

3、控制台运行程序
	python manage.py runserver 本机ip:8000
	局域网可以访问该地址，进行投票
	
	如果8000端口报错不可用
	windows：
	打开“Windows 防火墙”。
	点击“高级设置”。
	在左侧点击“入站规则”，然后在右侧点击“新建规则”。
	选择“端口”，然后点击“下一步”。
	选择“TCP”，并在“特定本地端口”中输入 8000，然后点击“下一步”。
	选择“允许连接”，然后点击“下一步”。
	根据需要选择网络类型（通常选择所有类型），然后点击“下一步”。
	为规则命名（例如“Django 服务器”），然后点击“完成”。
	
	mac：
	打开“系统偏好设置”。
	选择“安全性与隐私”。
	点击“防火墙”标签，然后点击“防火墙选项”。
	点击“添加应用程序”按钮，选择你的终端应用程序，然后点击“添加”。
	确保终端应用程序设置为“允许传入连接”。

4、一次投票结束后，清除历史投票纪录
	控制台运行
	python manage.py shell
	进入Django shell
	from polls.models import Vote
	Vote.objects.all().delete()