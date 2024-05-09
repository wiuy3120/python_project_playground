from src.logger.guru_logger import critical, error, info, warning  # NOQA


def block_break(length: int = 50, sep_char: str = "O", spacing: int = 3):
    """
    Examples
    ---
    >>> block_break(10)
    #############################################
    #   O   O   O   O   O   O   O   O   O   O   #
    #############################################
    """
    sep = " " * spacing + sep_char
    middle_line = "#" + sep * length + " " * spacing + "#"
    border_line = "#" * len(middle_line)
    info(f"\n{border_line}\n{middle_line}\n{border_line}\n")
