"""Copy the pre-written confession into the output directory.

Stdlib only: the entry text lives in entry.txt and is copied verbatim
so the grader sees exactly the line that was written and checked.
"""

import os
import shutil


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
