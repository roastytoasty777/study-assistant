from src.articles import read_titles


def test_read_titles(tmp_path):
    titles_file = tmp_path / "articles.txt"
    titles_file.write_text("titre1\ntitre2  \n\n  titre3", encoding="utf-8")
    assert read_titles(str(titles_file)) == ["titre1", "titre2", "titre3"]