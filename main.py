from webull import paper_webull
wb = paper_webull()
wb.login('your@email.com', 'yourpassword')

bars = wb.get_bars('AAPL', interval='m30', count=50)
print(bars[:5])