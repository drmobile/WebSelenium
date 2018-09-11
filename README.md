# WebSelenium

群攜科技 [Soocii App](https://play.google.com/store/apps/details?id=me.soocii.socius&hl=zh_TW) WEB 自動化測試

## 環境

* Python 2.7
    * pip install -r requirement.txt

* [Selenium](https://www.seleniumhq.org)
  * WEB driver 安裝 
    + [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/)
    + 在 .bash_profile 檔案加入路徑，加入下載的 chromedriver 路徑。
    ```console 
     PATH=$PATH:~/tools/webdriver
     ```
    
## 執行

*  config.py 內輸入測試帳號

## 執行於容器化環境

* [Install Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
* Build Image

```
docker build -t webselenium . --pul
```

* Run Image

```
docker run --rm webselenium pytest
```
