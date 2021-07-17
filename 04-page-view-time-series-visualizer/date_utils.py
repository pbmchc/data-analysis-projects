def format_date_boundaries(date_index, date_format):
    from_boundary = date_index[0].strftime(date_format)
    to_boundary = date_index[-1].strftime(date_format)

    return from_boundary, to_boundary
