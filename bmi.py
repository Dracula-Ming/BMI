height = input('請輸入身高(cm)： ')
height = int(height)
weight = input('請輸入體重(kg)： ')
weight = int(weight)
height = height / 100
bmi = weight / height / height
if bmi < 18.5:
    print('你的bmi為', bmi, '體重過輕,哇!真苗條~')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi為', bmi, '正常範圍,繼續保持喔!')
elif bmi >= 24 and bmi < 27:
    print('你的bmi為', bmi, '稍重,要注意囉!')
elif bmi >= 27 and bmi < 30:
    print('你的bmi為', bmi, '輕度肥胖,要開始控制飲食和要運動囉!')
elif bmi >= 30 and bmi < 35:
    print('你的bmi為', bmi, '中度肥胖,要開始控制飲食和要運動囉!')
else :
    print('你的bmi為', bmi, '重度肥胖,要開始控制飲食和要運動囉!')