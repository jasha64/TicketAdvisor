import pymysql
import re

conn = None
cursor = None


def init():
    global conn
    global cursor
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='i7-6700K', db='12306')
    cursor = conn.cursor()


def rec(tuple1, tuple2, w1):
    """
    returns a record in the shape
        (
            train_no, dist, time_delta,
            (src station, arrived_time, start_time),
            (dest station, arrived_time, start_time)
        )
    input must be like
        (train_no, src station, arrived_time, start_time, duration_time, distance)
        (train_no, dest station, arrived_time, start_time, duration_time, distance)
    """
    # print(tuple1)
    # print(tuple2)
    train_no = tuple1[0]
    dist = int(tuple2[-1]) - (0 if tuple1[-1] == '-' else int(tuple1[-1]))

    pattern = re.compile(r"(\d\d):(\d\d)")  # "04:06"
    match = pattern.match(tuple1[-2]).groups()
    time1 = int(match[0]) * 60 + int(match[1])
    match = pattern.match(tuple2[-2]).groups()
    time2 = int(match[0]) * 60 + int(match[1])
    time_delta = time2 - time1

    cost = w1 * dist + (1-w1) * time_delta

    return train_no, cost, dist, time_delta, tuple1[1:4], tuple2[1:4]


def query(src, dest, mode, w1):
    global cursor
    cond = ("true", "(train_no like 'G%%' or train_no like 'D%%' or train_no like 'C%%')",
            " not (train_no like 'G%%' or train_no like 'D%%' or train_no like 'C%%')")
    special_train_list = ('D7112', 'D7114', 'D7116', 'D7118', 'D7141-D7142', 'D7143-D7144', 'D7163-D7164', 'D7165-D7166', 'D7167', 'D7183-D7184', 'D7185-D7186', 'K7931', 'K7933', 'K7935', 'K7937')
    # in the list are trains whose start station = end station (Dec 2017 database)
    sql = '''
        select train_no
        from train_no_detail
        where station in (%s, %s) and ''' + cond[mode] + '''
        group by train_no
        having (count(*) = 2 and train_no not in ''' + str(special_train_list) + ''') or count(*) = 3
    '''
    # print(sql)
    cursor.execute(sql, [src, dest])

    tmp_list = tuple([x[0] for x in cursor.fetchall()])
    if len(tmp_list) == 0:  # no point continuing if we don't have any possible result
        return None
    if len(tmp_list) == 1:  # str(tmp_list) is like "('K80',)", but SQL syntax requires "('K80')"
        query2_str = str(tmp_list)[:-2] + ')'
    else:
        query2_str = str(tmp_list)
    # possible solutions included in tmp_list, while they need further confirmation
    sql = '''
        select train_no, station, arrived_time, start_time, duration_time, distance
        from train_no_detail
        where station in (%s, %s) and train_no in ''' + query2_str + '''
    '''
    # print(sql)
    cursor.execute(sql, [src, dest])

    tmp2_list = list(cursor.fetchall())
    if not tmp2_list:
        return None
    res_list = []
    i = 0
    while i < len(tmp2_list):
        if tmp2_list[i][0] in special_train_list:  # circular train
            if tmp2_list[i][1] == src:
                res_list.append(rec(tmp2_list[i], tmp2_list[i + 1], w1))
            else:
                res_list.append(rec(tmp2_list[i + 1], tmp2_list[i + 2], w1))
            i = i + 3
        else:
            if tmp2_list[i][1] == src:  # otherwise, the train is in opposite direction
                res_list.append(rec(tmp2_list[i], tmp2_list[i + 1], w1))
            i = i + 2
    return res_list


def close():
    global conn
    global cursor
    # conn.commit() (no need to commit - not modified)
    cursor.close()
    conn.close()
