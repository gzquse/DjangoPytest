# -*- coding:utf-8 -*-
"""
Socket接口
跟随启动时执行
"""
import socketserver
import json
import logging
import threading
import pymysql

logger = logging.getLogger()


def create_order(params):
    conn = pymysql.connect("localhost", "root", "root", "testproject")
    cursor = conn.cursor()
    sql = f"insert into order_info (name, type, dep, date, system, order_info.`desc`, status) " \
          f"values " \
          f"('{params.get('order_name')}','{params.get('order_type')}','{params.get('order_dep')}'," \
          f"'{params.get('order_date')}','{params.get('order_sys', '')}','{params.get('order_desc')}','0')"
    print(sql)
    cursor.execute(sql)

    sql = "select max(id) from order_info"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    conn.commit()

    return result[0]


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        answer_json = {
            "code": "000000",
            "msg": "Success",
        }
        try:
            data_len = int(self.request.recv(10))

            logger.info("请求报文长度: %d", data_len)

            buff_len = 1024
            recv_data = b""
            while data_len > 0:
                answer = self.request.recv(buff_len)
                recv_data += answer
                data_len -= len(answer)

            logger.info("请求报文体:\n%s", json.dumps(json.loads(recv_data.decode('utf-8')), indent=4, ensure_ascii=False))
            params = json.loads(recv_data.decode('utf-8'))
            if 'service' not in params:
                # answer_json['code'] = '500001'
                raise RuntimeError("非法请求.")
            if params.get('service') == 'createOrder':
                if 'order_name' not in params or params['order_name'] is None or len(params['order_name'].strip()) == 0:
                    answer_json['code'] = '500004'
                    raise RuntimeError("需求名称必输.")
                if 'order_dep' not in params or params['order_dep'] is None or len(params['order_dep'].strip()) == 0:
                    answer_json['code'] = '500005'
                    raise RuntimeError("需求部门必输.")
                if 'order_type' not in params or params['order_type'] is None or len(params['order_type'].strip()) == 0:
                    answer_json['code'] = '500006'
                    raise RuntimeError("需求类型必输.")
                if 'order_date' not in params or params['order_date'] is None or len(params['order_date'].strip()) == 0:
                    answer_json['code'] = '500007'
                    raise RuntimeError("需求日期必输.")

                newId = create_order(params)
                answer_json['order_id'] = newId
            else:
                answer_json['code'] = '500003'
                raise RuntimeError("错误的service参数.")
        except Exception as e:
            logger.exception(e)
            answer_json['code'] = "999999" if answer_json['code'] == '000000' else answer_json['code']
            answer_json['msg'] = str(e)

        json_str = json.dumps(answer_json)
        logger.info("应答报文体:\n%s", json.dumps(answer_json, indent=4, sort_keys=True))
        answer_str = "%010d%s" % (len(json_str.encode('utf-8')), json_str)
        logger.info("应答报文: %s", answer_str)
        self.request.send(answer_str.encode('utf-8'))
        self.request.close()
        logger.info("客户端发送完成，断开连接.")


def server_start():
    try:
        hostaddress = ("127.0.0.1", 8888)
        server = socketserver.ThreadingTCPServer(hostaddress, MyHandler)
        print("启动Socket服务...", hostaddress)
        server.serve_forever()
    except Exception as e:
        pass


t = threading.Thread(target=server_start)
t.start()
