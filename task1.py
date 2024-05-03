

def computerCount(number: int) -> str:
    endOv = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    endRa = [2 , 3, 4,]
    endR = [1]
    if number > 0:
        if int(str(number)[-2:]) in endOv:
            return f'{number}  компьютеров'
        elif int(str(number)[-1:]) in endRa:
            return f'{number}  компьютера'
        elif int(str(number)[-1:]) in endR:
            return f'{number}  компьютер'
        else:
            return f'{number}  компьютеров'
    else:
        return "НЕТ КОМПЬЮТЕРОВ"


for i in range(1000):
    print(computerCount(i))
