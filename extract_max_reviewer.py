# extract max reviewer
import pandas as pd
import numpy as np

reviewer=OrderedDict()
datalist=[]
temp = []

with open('/content/drive/My Drive/Z두번째 지난 플젝_지역별 평점 분석/yelp dataset/review.json', 'r', encoding='UTF-8') as rf:
  for line in rf:
    lineobj = json.loads(line)
    if lineobj['user_id'] == max_reviewer:
      temp.append(lineobj['user_id'])
      temp.append(lineobj['business_id'])
      temp.append(lineobj['text'])
      temp.append(lineobj['stars'])
      datalist.append(temp)
      temp=[]

df = pd.DataFrame(datalist)
