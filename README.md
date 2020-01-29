# 自动更新Aria2 Bt tracker
## 使用方法 For U-NAS：
`su root`进入root账户。
```
apt-get install git -y
cd
git clone https://github.com/maxzh0916/aria2-auto-tracker.git
python3 ./aria2-auto-tracker/aria2-auto-update-tracker.py
```
## 开机执行
`vi /etc/rc.local`在"exit 0"前添加python3 ./aria2-auto-tracker/aria2-auto-update-tracker.py

## 计划任务
`crontab -e`

添加：

`0 */1 * * * root python3 /root/aria2-auto-tracker/aria2-auto-update-tracker.py`

每小时更新一次，其他频率百度。

## 清理日志
`python3 aria2-auto-update-tracker.py --delete`