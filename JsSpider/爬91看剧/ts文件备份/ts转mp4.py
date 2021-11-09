import os
 
def get_tslist(_list, outname):
    _list.sort(key= lambda x:int(x[5:9]))
    out_list = 'concat:'
    for n in _list:
        out_list = out_list + n + '|'
    str1 = 'ffmpeg -i '
    str2 = ' -acodec copy -vcodec copy -absf aac_adtstoasc '
    end_list = str1 + "\"" +out_list[:-1] + "\"" + str2 + outname
    os.system(end_list)
 
def get_mp4list(dstroot, outname2):
    __list = os.listdir(dstroot)
    __list.sort()
    print(__list)
    _list = []
    for n in __list:
        if n[-3:] == '.ts':
            _list.append(n)
    _list.sort(key= lambda x:int(x[5:9]))
    # print(_list)
    # print(_list)
    temp = []
    cnt = 0
    cnt2 = 1
    cnt3 = 0
    for n in _list:
        if n[-3:] == '.ts':
            temp.append(n)
            cnt = cnt + 1
            cnt3 = cnt3 + 1
            if cnt == 10 or cnt3 == len(_list):
                outname = str(cnt2) + '.mp4'
                get_tslist(temp, outname)
                temp = []
                cnt = 0
                cnt2 = cnt2 + 1
    end_mp4(outname2)
 
def end_mp4(outname2):
    __list = os.listdir('./')
    _list = []
    for n in __list:
        if n[-4:] == '.mp4':
            _list.append(n)
    _list.sort()
    cnt = 0
    for k in _list:
        if k[-4:] == '.mp4':
            cnt = cnt + 1
 
    for m in range(len(_list)):
        n = str(m+1) + '.mp4'
        print(n)
        str1 = 'file ' + n + '\n'
        f = open('1.txt', 'a+')
        f.write(str1)
        f.close()
        if m == cnt:
            break
    end_str = 'ffmpeg -y -f concat -safe 0 -i ' + '1.txt' + ' -c copy output.mp4'
    print(end_str)
    os.system(end_str)
 
if __name__ == "__main__":
    dstroot = './text'
    outname = 'out.mp4'
    get_mp4list(dstroot, outname)