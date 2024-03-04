import click
import os
import sys
from typing import List, Optional


@click.command(name="nl", short_help="Numerate and print lines of text")
@click.argument("file", required=False, type=click.Path())
def cli_num_lines(file: Optional[str] = None) -> str:
    if file is not None:
        with open(file, "r") as f:
            lines = f.readlines()

        # dynamic format for len(lines)>=100000
        num_format = max(6, len(str(len(lines))))
        numerated_lines = [
            f"{i+1:{num_format}d}  {line}" for i, line in enumerate(lines)
        ]

        out = "".join(numerated_lines)

        print(out)
    else:
        numerated_lines = []
        for i, line in enumerate(sys.stdin):
            numerated_line = f"{i+1:6d}  {line}"
            numerated_lines.append(numerated_line)

            # should be printed after current line
            print(numerated_line, end="")

        out = "".join(numerated_lines)

    return out


@click.command(name="tail", short_help="Print the last 10 lines of files/stdin")
@click.argument("files", required=False, nargs=-1, type=click.Path())
def cli_tail(files: List[str] = []) -> str:
    if len(files) > 0:
        output_lines = []
        for file in files:
            header = ""
            lines = []

            # print file names if number of files > 0
            if len(files) > 0:
                header = f"==> {file} <==\n"

            with open(file, "r") as f:
                lines += f.readlines()

            # join all file lines by "" to join every file by "\n" separator later
            output_lines.append("".join([header] + lines[-10:]))
        out = "\n".join(output_lines)
    else:
        # read last 10 (17?) lines from stdin
        output_lines = sys.stdin.readlines()
        # output_lines = [line for line in sys.stdin][-10:]
        out = "".join(output_lines[-10:])

    print(out)

    return out


@click.command(name="wc", short_help="Print stats about files/stdin")
@click.argument("files", required=False, nargs=-1, type=click.Path())
def cli_wc(files: List[str] = []) -> str:
    if len(files) > 0:
        stats = []
        sum_stats = {"file": "total", "newlines": 0, "words": 0, "bytes": 0}

        for file in files:
            with open(file, "r") as f:
                lines = f.readlines()

            # count stats
            # wc don't count the last newline in this mode
            num_newlines = sum(1 for line in lines for w in line if w=="\n")
            num_words = sum(1 for line in lines for _ in line.split())
            num_bytes = (
                sum(len(line.encode("utf-8")) for line in lines)
                + len("\n".encode("utf-8")) * num_newlines
            )

            stats.append(
                {
                    "file": file,
                    "newlines": num_newlines,
                    "words": num_words,
                    "bytes": num_bytes,
                }
            )
            sum_stats["newlines"] += num_newlines
            sum_stats["words"] += num_words
            sum_stats["bytes"] += num_bytes

        # always dynamic format
        newlines_format = len(str(sum_stats["newlines"])) + 1
        words_format = len(str(sum_stats["words"])) + 1
        bytes_format = len(str(sum_stats["bytes"]))

        if len(files) > 1:
            # append sum_stats to all stats as "total"
            stats.append(sum_stats)

        output_lines = [
            f"{file_stats['newlines']:{newlines_format}d} {file_stats['words']:{words_format}d} "
            f"{file_stats['bytes']:{bytes_format}d} {file_stats['file']}"
            for file_stats in stats
        ]
        out = "\n".join(output_lines)
    else:
        lines = sys.stdin.readlines()
        # count stats
        num_newlines = sum(1 for line in lines for w in line if w=="\n")
        num_words = sum(1 for line in lines for _ in line.split())
        # wc skip newlines as bytes in this mode
        num_bytes = sum(len(line.encode("utf-8")) for line in lines)
        out = f"{num_newlines:7d} {num_words:7d} {num_bytes:7d}"

    print(out)
    return out


@click.group()
def cli():
    pass


cli.add_command(cli_num_lines)
cli.add_command(cli_tail)
cli.add_command(cli_wc)

if __name__ == "__main__":
    cli()
