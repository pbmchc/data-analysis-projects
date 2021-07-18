import datetime


def format_date_boundaries(date_index, date_format):
    from_boundary = date_index[0].strftime(date_format)
    to_boundary = date_index[-1].strftime(date_format)

    return from_boundary, to_boundary


def get_months_order():
    return [_get_month_name(month_number) for month_number in range(1, 13)]


def _get_month_name(month_number, month_name_format='%B'):
    return datetime.datetime.strptime(str(month_number), '%m').strftime(month_name_format)
