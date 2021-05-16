class NameCheck:
    
    def __init__(self, text):
        self.text = text
        self.length = 0
        
    def text_len(self):
        for i in self.text:
            self.length += 1
        print(self.length,"test")
        return self.length
    
    def even_or_odd(self):
        if self.length % 2 == 0:
            return '偶数'
        else:
            return '奇数'
x1 = 'たろう'

# クラス『NameCheck』をインスタンス化
nc_ta = NameCheck(x1)
len1 = nc_ta.length
print(len1)
y1 = nc_ta.text_len()
print(y1)
len2 = nc_ta.length
print(len2)
y2 = nc_ta.even_or_odd()
print(y2)