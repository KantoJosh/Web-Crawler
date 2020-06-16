# Web Crawler

In order to run the search engine:

	1) Run milestone1.py to create initial indexers from given json files
	2) Run organize.py to create a separate indexer (In alphabet) that contains {"token":{docID:tf}}
	3) Run tf_score.py to calculate tf-idf score and creating tf_score_indexer by extracting tf and other information from separate indexers
	4) Run create_partial.py to create a bookmark for search.py
	5) Run search_GUI.py to run search engine GUI (Need to copy the link from "Running on http:..." and paste it on web browser) and search a query
