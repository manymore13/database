import akshare as ak

# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20231022', adjust="")
# print(stock_zh_a_hist_df)
# print(ak.__ver)

index_value_name_funddb_df = ak.index_value_name_funddb()
index_value_name_funddb_df.to_csv("index.csv")
print(index_value_name_funddb_df)