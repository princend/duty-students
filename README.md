# 值日生排程

1.資料來源 google excel ,利用appscript取得資料

https://docs.google.com/spreadsheets/d/1HnUwH8EKnzC4S69jBA6vLZbw_Ms5sPgZ9_M1a5CbqI8/edit?gid=0#gid=0

2.使用flask 架起輕量網站
  call /notify 則會利用line notify 發送訊息至line

3.部屬在google cloud run
  已設定觸發器 持續部屬

4.使用google scheduler 每日排程定期call /notify api
  目前是1~5 早上八點
