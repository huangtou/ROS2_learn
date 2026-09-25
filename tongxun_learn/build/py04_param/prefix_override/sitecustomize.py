import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/huangbo/ros2_learn/tongxun_learn/install/py04_param'
