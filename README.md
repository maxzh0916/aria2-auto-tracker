# 自动更新Aria2 Bt tracker
## 使用方法 For U-NAS：
`su root`进入root账户。
```
cd
wget https://raw.githubusercontent.com/maxzh0916/aria2-auto-tracker/master/aria2-auto-update-tracker.py
python3 aria2-auto-update-tracker.py
```
## 开机执行
`vi /etc/rc.local`在"exit 0"前添加python3 /root/aria2-auto-update-tracker.py

## 计划任务
`crontab -e` 
