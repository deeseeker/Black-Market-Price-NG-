from newsapi import NewsApiClient



newsapi = NewsApiClient(api_key='7cbf747bbc6d4442b99ca7b5f91d0018')

# /v2/everything
all_articles = newsapi.get_everything(q='black market fuel prices in Nigeria',
                                      from_param='2022-08-15',
                                      to='2022-09-15',
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=5,
                                      country='ng',
                                      page=1)
print(all_articles['sources'])
