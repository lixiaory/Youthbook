import gzip
import shutil
import os

compressed = "data/processed/knowledge_graph/relations.pkl.gz"
target = "data/processed/knowledge_graph/relations.pkl"

if not os.path.exists(target):

    print("开始解压...")

    with gzip.open(compressed, "rb") as f_in:
        with open(target, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    print("解压完成")

else:
    print("relations.pkl 已存在")
