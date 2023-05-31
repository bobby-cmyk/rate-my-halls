def posted_ago(dt, years):
  try:
      dt = dt.replace(year=dt.year-years)
  except ValueError:
      dt = dt.replace(year=dt.year-years, day=dt.day-1)
  return dt