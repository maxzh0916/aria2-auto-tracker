import os
import sys
import urllib.request
import urllib.error
import logging

'''其他系统修改config后使用'''

config = {
    'aria2_service_name': 'unas-aria2',  # aria2服务名
    'aria2_config_path': '/etc/aria2',  # aria2配置文件路径
    'trackers_all_http': True,
    'trackers_all_https': False,
    'trackers_all_ip': True,
    'trackers_all_udp': True
}


def service_restart():
    os.system('service ' + config['aria2_service_name'] + ' restart')
    logging.info('重启Aria2服务')


def get_tracker():
    response_trackers_all_http = ''
    response_trackers_all_https = ''
    response_trackers_all_ip = ''
    response_trackers_all_udp = ''
    result = ''
    logging.info('开始获取tracker列表')
    if config['trackers_all_http']:
        try:
            logging.info('正在从Github加载trackers_all_http列表')
            response_trackers_all_http = urllib.request.urlopen(
                'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt')
        except urllib.error.URLError:
            logging.info('Github加载trackers_all_http失败')
            logging.info('正在从CDN服务器加载trackers_all_http列表')
            response_trackers_all_http = urllib.request.urlopen(
                'https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all_http.txt')
        finally:
            result = result + response_trackers_all_http.read().decode('utf-8').replace('\n\n', ',')

    if config['trackers_all_https']:
        try:
            logging.info('正在从Github加载trackers_all_https列表')
            response_trackers_all_https = urllib.request.urlopen(
                'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt')
        except urllib.error.URLError:
            logging.info('Github加载trackers_all_https失败')
            logging.info('正在从CDN服务器加载trackers_all_https列表')
            response_trackers_all_https = urllib.request.urlopen(
                'https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all_https.txt')
        finally:
            result = result + response_trackers_all_https.read().decode('utf-8').replace('\n\n', ',')

    if config['trackers_all_ip']:
        try:
            logging.info('正在从Github加载trackers_all_ip列表')
            response_trackers_all_ip = urllib.request.urlopen(
                'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt')
        except urllib.error.URLError:
            logging.info('Github加载trackers_all_ip失败')
            logging.info('正在从CDN服务器加载trackers_all_ip列表')
            response_trackers_all_ip = urllib.request.urlopen(
                'https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all_ip.txt')
        finally:
            result = result + response_trackers_all_ip.read().decode('utf-8').replace('\n\n', ',')

    if config['trackers_all_udp']:
        try:
            logging.info('正在从Github加载trackers_all_udp列表')
            response_trackers_all_udp = urllib.request.urlopen(
                'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt')
        except urllib.error.URLError:
            logging.info('Github加载trackers_all_udp失败')
            logging.info('正在从CDN服务器加载trackers_all_udp列表')
            response_trackers_all_udp = urllib.request.urlopen(
                'https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all_udp.txt')
        finally:
            result = result + response_trackers_all_udp.read().decode('utf-8').replace('\n\n', ',')
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
    logging.info('开始更新tracker列表')


if __name__ == '__main__':
    path = __file__[:__file__.rfind("/")]
    logging.basicConfig(level=logging.INFO,
                        filename=path + '/running.log',
                        filemode='a',
                        format='%(asctime)s: %(message)s'
                        )

    if len(sys.argv) > 1 and sys.argv[1] == '--delete':
        os.system('rm -rf ' + path + '/running.log')
        exit()

    url = get_tracker()
    update_tracker(url)
    service_restart()
