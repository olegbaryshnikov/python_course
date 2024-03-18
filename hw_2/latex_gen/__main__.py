from latex_gen.utils import get_latex_table, get_latex_img, latex_doc_wraper
from typing import List, Any
import click
import os


def get_table(rows: int, cols: int) -> List[List[Any]]:
    return [[i + j * cols for i in range(cols)] for j in range(rows)]


def save_file(text: str, path: str) -> None:
    with open(path, "w+") as f:
        f.write(text)


@click.command(name="gen", short_help="Gen Latex file with table and img")
@click.option("--img_path", "-i", required=True, type=str, help="Path to img")
@click.option("--save_dir", "-s", required=True, type=str, help="Path to output dir")
def gen_latex_table_img(
    img_path: str = "hw_2/Lenna.png",
    save_dir: str = os.path.join(".", "hw_2", "artifacts"),
):

    latex_table = get_latex_table(get_table(10, 5))
    latex_img = get_latex_img(os.path.basename(img_path))

    latex_doc = latex_doc_wraper(
        latex_table + "\n" + latex_img, os.path.dirname(img_path)
    )
    save_file(latex_doc, os.path.join(save_dir, "latex.tex"))


if __name__ == "__main__":
    gen_latex_table_img()
