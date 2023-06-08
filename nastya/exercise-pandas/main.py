import pandas as pd
from typing import Final, List

TEXT_TABLE_URL: Final[str] = \
    "https://raw.githubusercontent.com/mathling-programming/practice2022/main/exercise-pandas/text.csv"
VOCAB_TABLE_URL: Final[str] = \
    "https://raw.githubusercontent.com/mathling-programming/practice2022/main/exercise-pandas/vocab.csv"

SEPARATOR: Final[str] = ","
WORDNO_COLUMN: Final[str] = "WORDNO"
WORD_COLUMN: Final[str] = "WORD"
POS_COLUMN: Final[str] = "POS"
GROUP_HEADER: Final[str] = "POS"

UNIQUE_HEADERS: Final[List[str]] = [WORD_COLUMN, POS_COLUMN]


def download_table(url: str) -> pd.DataFrame:
    return pd.read_csv(url, sep=SEPARATOR)


def join_tables_by_header(table1: pd.DataFrame, table2: pd.DataFrame, header: str) -> pd.DataFrame:
    return table1.merge(table2, on=header)


def delete_duplicates(table: pd.DataFrame, headers: list[str]) -> pd.DataFrame:
    return table.drop_duplicates(subset=headers)


def count_word_length(table: pd.DataFrame, header: str) -> pd.DataFrame:
    return table[header].apply(lambda x: len(x))


if __name__ == "__main__":
    text_table: pd.DataFrame = download_table(TEXT_TABLE_URL)
    vocab_table: pd.DataFrame = download_table(VOCAB_TABLE_URL)

    joined_table: pd.DataFrame = join_tables_by_header(text_table, vocab_table, WORD_COLUMN)
    joined_table = delete_duplicates(joined_table, UNIQUE_HEADERS)
    joined_table[WORD_COLUMN + "_LENGTH"] = count_word_length(joined_table, WORD_COLUMN)

    groups = joined_table.drop(columns=[WORD_COLUMN, WORDNO_COLUMN]).groupby(GROUP_HEADER)
    grouped_table: pd.DataFrame = pd.DataFrame(columns=[GROUP_HEADER, "MEAN"])
    for group in groups:
        rolled_table = group[1].drop(columns=POS_COLUMN).rolling(window=5, min_periods=1).mean()
        rolled_value = sum(rolled_table.values) / len(rolled_table.values)

        grouped_table.loc[len(grouped_table)] = [group[0], rolled_value[0]]

    grouped_table.to_html("grouped_table.html")
    plt = grouped_table.plot.bar(x=GROUP_HEADER, y="MEAN")
    plt.get_figure().savefig("grouped_table.png", dpi=500, bbox_inches='tight', pad_inches=0.5, transparent=True,
                             facecolor='w', edgecolor='w', orientation='portrait')
