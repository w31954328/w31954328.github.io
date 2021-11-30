import pymysql

# 返回 连接，游标
def get_conn():
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1", user="root", password="root", db="myspider", charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_page3_l1_data():
    sql ="SELECT location,total_vaccinations FROM us_state_vaccinations where date=(select date from us_state_vaccinations order by date desc limit 1) and not(location='United States') ORDER BY cast(total_vaccinations as SIGNED INTEGER) DESC limit 0,10"
    res = query(sql)
    return res

# if __name__ == "__main__":
#     print(get_data())