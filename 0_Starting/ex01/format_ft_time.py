import time
import datetime as dt

t = time.time()
d = dt.datetime.now().strftime("%b %d %Y")

fmt_date = f"{d}"
fmt_sec = f"{t:,.4f}"
sci_sec = f"{t:.2e}"

print(f"""Seconds since January 1, 1970: {fmt_sec} or {sci_sec} in scientific notation
{fmt_date}""")
