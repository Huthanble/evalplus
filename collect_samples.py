# collect_samples.py
import json, pathlib
from evalplus.data import get_human_eval_plus, write_jsonl

root = pathlib.Path("tasks/humaneval")
samples = []
for tid in get_human_eval_plus():
    code = (root / f"{tid}.py").read_text()
    samples.append({"task_id": tid, "solution": code})  # solution=完整文件
write_jsonl("my_plugin_samples.jsonl", samples)
