def dateComp(date_one, date_two):
    date_one_id = date_one.split('.')
    date_two_id = date_two.split('.')
    if int(date_one_id[2]) > int(date_two_id[2]):
        return True
    elif int(date_one_id[2]) == int(date_two_id[2]):
        if int(date_one_id[1]) > int(date_two_id[1]):
            return True
        elif int(date_one_id[1]) == int(date_two_id[1]):
            if int(date_one_id[0]) > int(date_two_id[0]):
                return True
            elif int(date_one_id[0]) == int(date_two_id[0]):
                return True
    return False


def addItem(list_bas, item, item_loc):
    new_list = list_bas[0:item_loc]
    new_list.append(item)
    for i in range(len(list_bas) - item_loc):
        new_list.append(list_bas[item_loc + i])
    return new_list


def expDate(current_date, prod_dates):
    thrown_away = []
    thrown_locs = []
    thrown_number = 0
    for i in range(len(prod_dates)):
        if dateComp(current_date, prod_dates[i]):
            thrown_away.append(prod_dates[i])
            thrown_locs.append(i)

    for i in range(len(thrown_locs)):
        prod_dates.pop(thrown_locs[i] - thrown_number)
        thrown_number += 1


def dateSort(current_date, prod_dates):
    loc = None
    sorted_dates = []
    prev_placed = True

    for i in range(len(prod_dates)):
        if dateComp(prod_dates[i], current_date):
            sorted_dates.append(prod_dates[i])
            loc = i
            break

    for i in range(len(prod_dates)):
        if (loc == i):
            continue
        prev_placed = True
        for j in range(len(sorted_dates)):
            if prev_placed:
                if j == 0:
                    if dateComp(sorted_dates[j], prod_dates[i]):
                        sorted_dates = addItem(sorted_dates, prod_dates[i], 0)
                        prev_placed = False
                        continue
                if j == len(sorted_dates) - 1:
                    if dateComp(prod_dates[i], sorted_dates[j]):
                        sorted_dates = addItem(sorted_dates, prod_dates[i], len(sorted_dates))
                    else:
                        sorted_dates = addItem(sorted_dates, prod_dates[i], len(sorted_dates) - 1)
                    continue

                if dateComp(prod_dates[i], sorted_dates[j]):
                    if dateComp(sorted_dates[j + 1], prod_dates[i]):
                        sorted_dates = addItem(sorted_dates, prod_dates[i], j + 1)
                        prev_placed = False
                        continue
                if dateComp(sorted_dates[j], prod_dates[i]):
                    if dateComp(prod_dates[i], sorted_dates[j - 1]):
                        sorted_dates = addItem(sorted_dates, prod_dates[i], i)
                        prev_placed = False
                        continue

    return sorted_dates


def dateToint(sorted_dates, unsorted_dates, date_current):
    date_num = 0
    prev_date = None
    sorted_dateInt = []
    unsorted_dateInt = []

    for i in range(len(sorted_dates)):
        if (dateComp(date_current, sorted_dates[i])):
            sorted_dateInt.append(-1)
            continue
        if (prev_date == sorted_dates[i]):
            sorted_dateInt.append(date_num)
            continue
        date_num += 1
        sorted_dateInt.append(date_num)
        prev_date = sorted_dates[i]

    for i in unsorted_dates:
        unsorted_dateInt.append(sorted_dateInt[sorted_dates.index(i)])

    return unsorted_dateInt


def listDif(list1, list2):
    listOrig = list1
    for i in list2:
        if i in listOrig:
            listOrig.pop(listOrig.index(i))

    return listOrig


def calcDate(exp_dates, date_cur):
    exp_dates_process = exp_dates[:]
    sorted_date = dateSort(date_cur, exp_dates_process)
    date_int = dateToint(sorted_date, exp_dates, date_cur)
    return date_int
