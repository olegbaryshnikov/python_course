import os
from typing import List, Any


def _get_row(row: List[Any]) -> str:
    return "  " + " & ".join([str(el) for el in row])


def _get_content(table: List[List[Any]]) -> str:
    rows = [_get_row(row) for row in table]
    return "  \\hline\n" + " \\\\ \\hline\n".join(rows) + " \\\\ \\hline\n"


def _table_wrapper(content: str, col_num: int) -> str:
    columns_format = "|" + "|".join(["c"] * col_num) + "|"
    start = "\\begin{tabular}{" + columns_format + "}\n"
    end = "\\end{tabular}\n"
    return start + content + end


def get_latex_table(table: List[List[Any]]) -> str:
    """
    Function to get table in latex compatible format
    """
    assert len(table) > 0 and len(table[0]) > 0, "table should not be empty"
    return _table_wrapper(_get_content(table), len(table[0]))


def get_latex_img(img_path: str) -> str:
    """
    Function to get image in latex compatible format
    """
    return "\\includegraphics{" + img_path + "}"


def latex_doc_wraper(content: str, cwd_path: str = "") -> str:
    """
    Latex document wrapper for latex compatible content
    """
    header = (
        "\\documentclass[12pt]{article}\n"
        + "\\usepackage{graphicx}\n"
        + "\\graphicspath{{"
        + cwd_path.replace("/", "\\")
        + "}}\n"
        + "\n"
    )
    return header + "\\begin{document}\n" + f"{content}\n" + "\\end{document}\n"
