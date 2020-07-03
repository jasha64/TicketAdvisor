from knowledge import *  # major_station_list
import sql


def solve(src, dest, mode, w1, qzzz):
    # mode=0 means all trains, mode=1 means high-speed bullet trains (G/D/C), mode=2 means legacy trains (Z/T/K/numbers)
    # cost = w1 * distance + (1-w1) * time
    # 'qzzz' is the abbreviation of Chinese word '强制中转'(Qiang2 Zhi4 Zhong1 Zhuan3), which means forced transit city,
    #  user may choose the transit city according to his or her own wish.
    selected_city = ''
    selected_train1 = []
    selected_train2 = []
    all_res_list = []
    selected_cost = 40000  # min([each[1] for each in selected_train1]) if selected_train1 else 40000
    selected_dist = 40000
    selected_time = 40000
    # The number '40000' is from Mao Zedong's poet “坐地日行八万里，巡天遥看一千河” (By sitting on the ground
    # we travel 80,000 Chinese miles a day, touring the sky and seeing a thousand galaxies from afar)
    # Because the perimeter of Earth equator is about 40,000 km, I use 40000 here to represent infinity.
    for city, stations in major_station_list.items():  # transit city
        if qzzz != '':
            if city != qzzz:
                continue
        if src in stations or dest in stations:
            continue
        res_list1 = []
        res_list2 = []
        for station in stations:  # transit station
            tmp = sql.query(src, station, mode, w1)
            if tmp:
                res_list1.extend(tmp)
        if not res_list1:
            continue
        for station in stations:
            tmp = sql.query(station, dest, mode, w1)
            if tmp:
                res_list2.extend(tmp)
        if not res_list2:
            continue
        # in fact not all res_list need to be sorted; only the one in the final return values needs
        # however, according to my test, the according optimization makes little use,
        #   and thus sorting isn't the performance bottleneck
        res_list1.sort(key=lambda x: (x[1], x[3]))
        cost1 = res_list1[0][1]
        res_list2.sort(key=lambda x: (x[1], x[3]))
        cost2 = res_list2[0][1]
        # each record in the res_list is like:
        #         (
        #             train_no, cost, dist, time_delta,
        #             (src station, arrived_time, start_time),
        #             (dest station, arrived_time, start_time)
        #         )
        cost = cost1 + cost2
        all_res_list.append((city, cost, res_list1[0], res_list2[0]))
        # each record in all_res_list is like:
        # (
        #   city, cost, dist, time
        #   (
        #     train1_no, cost1, dist1, time_delta1,
        #     (src station, arrived_time, start_time),
        #     (transfer station, arrived_time, start_time)
        #   ),
        #   (
        #     train2_no, cost2, dist2, time_delta2,
        #     (transfer station, arrived_time, start_time),
        #     (dest station, arrived_time, start_time)
        #   ),
        # )
        # train1/train2 above is the one with lowest cost between src sta and trans sta / trans sta and dest sta
        if cost >= selected_cost:
            continue
        selected_city = city
        selected_cost = cost
        selected_dist = min(train1[2] for train1 in res_list1) + min(train2[2] for train2 in res_list2)
        selected_time = min(train1[3] for train1 in res_list1) + min(train2[3] for train2 in res_list2)
        selected_train1 = res_list1
        selected_train2 = res_list2
    all_res_list.sort(key=lambda x: (x[1], x[3]))
    return selected_city, selected_cost, selected_dist, selected_time, selected_train1, selected_train2, all_res_list
