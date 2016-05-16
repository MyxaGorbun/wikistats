    a = wg.get_id('Python')
    print(wg.get_links_from(1))
    print(wg.get_number_of_links_from(1))
    print(wg.get_number_of_pages())
    print(wg.get_page_size(1))
    print(wg.get_title(a))
    print(a)


 for i in range(len(wg._redirect)):
        if int(wg._redirect[i]) == 1:
            n += 1
    print('количество статей с перенаправлением: ', n)
    n = float('+inf')
    for i in range(len(wg._offset)-1):
        if wg._offset[i+1]-wg._offset[i] < n:
            n = wg._offset[i+1]-wg._offset[i]
    print('минимальное количество ссылок из статьи: ', n)
    a = 0
    for i in range(len(wg._offset)-1):
        if wg._offset[i+1]-wg._offset[i] == n:
            a +=1
    print('количество статей с минимальным количеством ссылок: ', a)
    n = 0
    for i in range(len(wg._offset)-1):
        if wg._offset[i+1]-wg._offset[i] > n:
            n = wg._offset[i+1]-wg._offset[i]
    print('максимальное количество ссылок из статьи: ', n)
    a = 0
    for i in range(len(wg._offset)-1):
        if wg._offset[i+1]-wg._offset[i] == n:
            a +=1
            s = i+1
    print('количество статей с максимальным количеством ссылок: ', a)
