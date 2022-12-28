# AIoT_HW5
## step 1: 執行老師給的myea.py後
<img width=600 height=400 src=https://user-images.githubusercontent.com/70211278/209815844-5ce7d2d2-92a7-4fbf-8839-05092750bfba.png>

## step 2: 修改程式碼
#### 使用 trainN.csv 來訓練
    #=================read Data=================#
    #data=pd.read_csv("training.csv")        #載入traning.csv至data
    data=pd.read_csv("trainN.csv") 
    X=data['value'].values.reshape(-1,1)
    Y=data['status'].values.reshape(-1,1)

#### 使用 SVC 模型
    model=SVC()           #邏輯迴歸
    #model.fit(ndX,ndY)                      #訓練模型
    model.fit(X,Y)
    my_score=model.score(X,Y)
    #print(my_score)

## step 3: 結果
<img width=600 height=400 src=https://user-images.githubusercontent.com/70211278/209816413-bdb32f4c-1039-451c-9464-7564116b8c8a.png>
