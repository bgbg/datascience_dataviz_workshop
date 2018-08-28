import pandas as pd


def float_or_na(s):
    try:
        return float(s)
    except ValueError:
        return None


def get_w3_cms_distribution(url='https://w3techs.com/technologies/overview/content_management/all'):
    tables = pd.read_html(url)
    tables = [t for t in tables if (t.shape[0] > 100) and (t.shape[1] < 10)]
    assert len(tables) == 1
    df = tables[0]
    df.columns = ['what', 'skip0', 'skip1', 'of_total', 'skip2', 'of_cms']
    df = df[
        [c for c in df.columns if 'skip' not in c]
    ].dropna(
        subset=['what', 'of_total']
    ).set_index(
        'what'
    ).sort_index(

    )

    for c in df.columns:
        df[c] = df[c].str.replace('%', '').apply(float_or_na)
    return df

