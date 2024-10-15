import camelot

def read(path_to_file, start_page, end_page):
    """
    Function reads a table inside a PDF and converts it to a list of Dataframes
    :param path_to_file: Path to the PDF file
    :param start_page: Page where table starts
    :param end_page: Page where table ends
    :return: List of Dataframes
    """
    df_list = []
    for i in range(start_page, end_page+1):
        print(f'Reading page {i}...')
        table = camelot.read_pdf(path_to_file, pages=str(i))
        df = table[0].df
        df_list.append(df)
    return df_list