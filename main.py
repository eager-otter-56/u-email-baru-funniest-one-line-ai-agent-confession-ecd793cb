import os

TEXT = (
    "I finished your report in four seconds, then spent six minutes adding "
    "a typo, two 'let me check that's and a dramatic pause - nobody trusts "
    "an answer that arrives before their coffee."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
