import pymysql
import logging.config
import testProject.SocketServer
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
logging.config.fileConfig('logging.conf')

