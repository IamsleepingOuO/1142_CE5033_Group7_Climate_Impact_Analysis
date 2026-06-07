# 1142_CE5033_Group7_Climate_Impact_Analysis
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker Support](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![Development Branch](https://img.shields.io/badge/branch-dev-orange.svg)](https://github.com/IamsleepingOuO/1142_CE503)

## How to use
Downlad the dataset, put it under the folder.
https://www.kaggle.com/datasets/uom190346a/global-climate-events-and-economic-impact-dataset \
And ```cd``` into the folder.

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
