import pymysql
import argparse
import logging, logging.config
logging.config.fileConfig('conf/log.conf')

logger = logging.getLogger("root")
# logger = logging.getLogger("main")
"""
    退出码 
    -1    参数不正确
    -2    数据库种类错误
    -3    数据库连接失败
"""
def parseArgs():

    parse = argparse.ArgumentParser(description="sql连接测试")
    parse.add_argument("--host", "-o", help="主机信息", required=True)
    parse.add_argument("--port", "-p", help="端口信息", required=True)
    parse.add_argument("--user", "-u", help="用户名", required=True)
    parse.add_argument("--passwd", "-w", help="密码", required=True)
    parse.add_argument("--database", "-d", help="数据库", required=True)
    parse.add_argument("--sql", "-s", help="数据库种类")
    args = parse.parse_args()

    # 为空的判断放到web端，这里就简单输出一下
    if not args.host or not args.port or not args.user or not args.passwd or not args.database:
        logger.debug("主机/端口/用户名/密码/数据库 信息不全 退出")
        return -1
    if not args.sql:
        args.sql = "mysql"
    # 这里需要保存到日志，把账号密码
    logging.debug(args)

    return  args


def try_connect(args):
    if args.sql == "mysql":
        try:
            db = pymysql.connect(host=args.host, port=int(args.port), user=args.user,
                             passwd=args.passwd, db=args.database)
            logging.info("数据库连接成功")
        except Exception as e:
            logger.error(e)
            return -3

    elif args.sql == "oracle":
        pass
    else:
        logger.warn("数据库目前只处理mysql和oracle，请推出")
        return -2

if __name__ == '__main__':
    args = parseArgs()
    try_connect(args)