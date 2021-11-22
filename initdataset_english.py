attributes = [
    ['cao', 'thap'],
    ['dai', 'ngan'],
    ['dai', 'ngan'],
    ['khoe', 'yeu'],
    ['khoe', 'yeu'],
    ['khoe', 'yeu'],
    ['tot', 'kem'],
    ['tot', 'kem'],
    ['tot', 'kem'],
    ['nhanh', 'cham']
]

samples = [
    ['cao', 'dai', '', 'khoe', 'khoe', 'khoe', 'tot', 'tot', '','nhanh','Tennis'],
    ['cao', 'dai', 'dai', '', '', 'khoe', 'tot', 'tot','','','Boi'],
    ['','','','khoe','','','tot','','tot','','Ban cung'],
    ['', 'ngan', 'ngan', 'khoe', 'khoe', 'khoe', 'tot', 'tot', 'tot', '','Cu ta'],
    ['','','','','khoe','khoe','tot','tot', '','nhanh','Chay ben'],
    ['','','','khoe','khoe','khoe','tot','tot','tot','','Dau vat'],
    ['cao', 'dai', '','','','khoe','','tot','','nhanh','Boxing'],
    ['', '', '', '','khoe','khoe','tot','tot','','nhanh','Bong ban'],
    ['', '', '', 'khoe','khoe','khoe','','tot','','nhanh','Cau long'],
    ['', '', '', '','khoe','khoe','','tot','','','Dap xe'],
    ['cao', 'dai', '', '','','khoe','tot','tot','tot','nhanh','Bong ro'],
    ['cao', '', '', 'khoe','khoe','khoe','tot','tot','','nhanh','Bong chuyen'],
    ['thap', 'ngan', 'ngan', '','','khoe','tot','tot','','','The duc dung cu'],
]

def fill(pos,s):
    if pos == 10:
        with open('dataset.txt', 'a') as w:
            for i in range(11):
                w.write(s[i])
                if i < 10:
                    w.write(',')
                else:
                    w.write('\n')
    else:
        if s[pos] != '':
            fill(pos + 1, s)
        else:
            for i in attributes[pos]:
                s[pos] = i
                fill(pos+1,s)
                s[pos] = ''

if __name__ == '__main__':
    for s in samples:
        fill(0,s)