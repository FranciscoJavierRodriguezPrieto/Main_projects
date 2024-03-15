import wikipedia as wk

search_query = 'San agustin'
try:
    summary = wk.summary(search_query)
    print(summary)
except wk.exceptions.DisambigationError as e:
    print('erro 1')
except wk.exceptions.PageError as e:
    print('error 2')
except Exception as e:
    print('error 3')