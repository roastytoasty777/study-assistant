def read_titles(path: str) -> list[str]:
    with open(path, encoding="utf-8") as file:
        lines = file.read().splitlines()
    titles = []
    for line in lines:
        if line.strip():
            titles.append(line.strip())
    return titles