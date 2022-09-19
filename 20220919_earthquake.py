import math
#這裡速度統一單位為km/s
s, p = map(float, input().split())#p:6.5 s:3.5
#因為光速為3*10**6所以忽略發射電磁波的時間
if p > s:#p波波速必定大於s波波速
    c = 3*10**5#電磁波速度為光速
    deepth = float(input('輸入地震深度'))
    distancses = float(input('輸入震央距離'))

    t1 = deepth / p
    processing = 2#訊號處理須2秒
    
    time = (math.sqrt(deepth**2 + distancses**2))/s
    #有地震深度、震央距離 利用勾股定理計算出震源到我的直線距離
    
    print(time)#輸出國家級警報可提前到達的秒數


