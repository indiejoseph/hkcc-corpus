# [《香港二十世紀中期粵語語料庫》](http://corpus.ied.edu.hk/hkcc/)打包器

[`香港二十世紀中期粵語語料庫`](http://corpus.ied.edu.hk/hkcc/)含人工分詞後的電影對話句子，非常適合作為 NLP 的分詞任務語料，或作為 Dialogue System 的對話語料。

本程序目的是打包[`香港二十世紀中期粵語語料庫`](http://corpus.ied.edu.hk/hkcc/)的語料成 CSV 檔案，為方便 NLP / Machine Learning 的朋友使用。

因版權問題 Repo 內不包含語料庫內容，請先到 [`http://corpus.ied.edu.hk`](http://corpus.ied.edu.hk) 註冊後登入，再把瀏覽器中的 Cookie `PHPSESSID` 加到 Enviroment Variable 中
```
export SESS_ID=xxxxxxxx
```
後再執行:
```
python main.py
```

## Improvement
因 `http://corpus.ied.edu.hk` 的網站不太 stable 中間多次 timeout，需加 resume 的功能。

## Author
Joseph Cheng / [@indiejoseph](http://indiejoseph.github.io)
