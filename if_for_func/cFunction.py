#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def roundFunction(inValue):
    step1 = inValue * 1000
    step2 = int(step1)
    outValue = step2 / 1000
    return outValue

# 내용: 함수는 숫자형 리스트에서 최대 최소값 전부를 제거한 후 평균을 구함
# 파라미터(입력/출력): listValue: list
# 목적: 최대 최소 제외한 평균 구하기

def avgFunction(listValue):
    listMax = max(listValue)
    listMin = min(listValue)
    maxCount = listValue.count(listMax)
    minCount = listValue.count(listMin)
    listValueSum = 0             # 총 합
    listValueLen = 0             # 총 개수

    for i in range(0, len(listValue)):
        if (listValue[i] == listMax) | (listValue[i] == listMin):  
            pass                                  # 리스트 안에 최대값 또는 최소값은 pass

        else:
            listValueSum = listValueSum + listValue[i] # 총 합에 저장
            listValueLen = listValueLen + 1            # 총 개수에 저장

    if len(listValue)-maxCount-minCount == 0:   #개수가 0인지 검사
        avg = 0
    else:
        avg = listValueSum / listValueLen

    return avg