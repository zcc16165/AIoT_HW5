# AIoT_HW5
## step 1: 將訓練好的模型存下來
    import pickle
    import gzip
    with gzip.GzipFile('./myModel.pgz','w') as f:
        pickle.dump(model, f)
## step 2: 將模型移到ea.py的資料夾裡
![image](https://user-images.githubusercontent.com/70211278/209819419-182e6deb-cbaa-4e7a-afa0-b56053bcfc1d.png)

## step 3: 執行結果
![image](https://user-images.githubusercontent.com/70211278/209819502-fbb9d15d-cd30-45cc-b5ca-1305be4a016e.png)
