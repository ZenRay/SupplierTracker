#coding:utf8
import logging
import pathlib

from os import path
from configparser import ConfigParser

logger = logging.getLogger("Supplier.lib.config")
__current_path = path.dirname(__file__)
Path = pathlib.Path(path.join(__current_path, "config"))


# load database configuration
if Path.joinpath('db.ini').exists():
    db = ConfigParser()
    db.read(Path.joinpath('db.ini'))
    logger.debug(f'数据库配置文件加载成功')
else:
    raise FileNotFoundError(f'数据库配置文件缺失，添加 `db.ini`文件')


del Path