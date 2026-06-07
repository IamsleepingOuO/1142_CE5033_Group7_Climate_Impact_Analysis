# 1142_CE5033_Group7_Climate_Impact_Analysis


## How to use
```cd``` inside the folder

### First time

```
docker build -t climate-env .
```

### Run docker and prepare for Jupyter connection

``` 
docker run -it --rm -p 8888:8888 -v $(pwd):/workspace climate-env
```

### Run Jupyter Lab
```
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

## 剩餘工作
* notebook內容修改(對執行結果進行分析等)
* 簡報
