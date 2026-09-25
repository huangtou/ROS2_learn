import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/huangbo/ros2_learn/tongxun_learn/src/install/py02_service_my'
