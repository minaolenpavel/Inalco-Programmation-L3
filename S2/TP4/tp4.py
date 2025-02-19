import polars as pl

df = pl.read_csv("videos.csv", separator=",")

df.select(["channel_id", "tags"]).write_json("question_4.json")
