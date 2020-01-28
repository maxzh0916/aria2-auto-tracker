import os
import urllib.request
import logging

'''其他系统修改config后使用'''

config = {
    'aria2_service_name': 'unas-aria2',  # aria2服务名
    'aria2_config_path': '/etc/aria2',  # aria2配置文件路径
    'tracker_url': 'https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all_http.txt'  # 使用CDN以保证读取可靠性，可以替换
}


def service_restart():
    os.system('service ' + config['aria2_service_name'] + ' restart')
    logging.info('重启Aria2服务。')


def get_tracker():
    response = urllib.request.urlopen(config['tracker_url'])
    result = response.read().decode('utf-8').replace('\n\n', ',')
    logging.info('获取tracker列表。')
    return result


def update_tracker(tracker_url):
    with open(config['aria2_config_path'] + '/aria2.conf', 'r') as file:
        result = file.readlines()
        if '\n' not in result[-1]:
            result[-1] = result[-1] + '\n'
        for i in result:
            if 'bt-tracker' in i:
                result.remove(i)
        result.append('bt-tracker=' + tracker_url + '\n')
    with open(config['aria2_config_path'] + '/aria2.conf', 'w') as file:
        file.write(''.join(result))
    logging.info('更新tracker列表')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filename='/root/aria2-auto-update-tracker.log',
                        filemode='a',
                        format='%(asctime)s: %(message)s'
                        )
    url = get_tracker()
    update_tracker(url)
    service_restart()
