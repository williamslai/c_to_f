#華氏 = 攝氏*(9/5)+32
#攝氏 = (華氏-32)*5/9
#攝氏('C)轉換成華式('F)程式
#讓使用者輸入攝氏溫度，然後印出華氏溫度。

celsius = input('請輸入攝氏溫度: ')
celsius = int(celsius)
fa = celsius * 9 / 5 + 32
print('華氏溫度等於 ', fa)

