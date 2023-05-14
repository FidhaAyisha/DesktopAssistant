import pywhatkit
import Assistant
import wikipedia
from wikipedia import wikihow, search_wikihow

def GoogleSearch(term):
    query = term.replace('Edith','')
    query = query.replace('what is','')
    query = query.replace('how to','')
    query = query.replace('what is','')
    query = query.replace(' ','')
    query = query.replace('what do you mean by','')
    writeab = str(query)
    Query = str(term)
    if 'how to ' in Query:
        max_results = 1
        how_to_function = search_wikihow(query=Query, max_results=max_results)
        assert len(how_to_function) == 1
        how_to_function[0].print()
        Assistant.output(how_to_function[0].summary)

    else:
        pywhatkit.search(Query)
        search = wikipedia.summary('Query',2)
        Assistant.output(f"According to your search:{search}")

GoogleSearch("what is photosynthesis")