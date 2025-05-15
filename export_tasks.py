# export_tasks.py
from pathlib import Path
from evalplus.data import get_human_eval_plus   # 或 get_mbpp_plus

out_dir = Path("tasks/humaneval")
for tid, prob in get_human_eval_plus().items():
    out_path = out_dir / f"{tid}.py"            # 可能含多级子目录
    out_path.parent.mkdir(parents=True, exist_ok=True)  # 关键：递归建目录
    out_path.write_text(prob["prompt"])
