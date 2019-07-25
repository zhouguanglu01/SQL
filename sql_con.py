import pymysql
import argparse


def parseArgs():

    parse = argparse.ArgumentParser(description="sql连接测试")
    parse.add_argument("--host", "-o", help="主机信息", required=True)
    parse.add_argument("--port", "-p", help="端口信息", required=True)
    parse.add_argument("--user", "-u", help="用户名", required=True)
    parse.add_argument("--passwd", "-p", help="密码", required=True)
    parse.add_argument("--database", "-d", help="数据库", required=True)
    args = parse.parse_args()

    # 为空的判断放到web端，这里就简单输出一下
    if not args.host or not args.port or not args.user or not args.passwd or not args.database:
        print("主机/端口/用户名/密码/数据库 信息不全 退出")
        return 0
    


    print(args)
