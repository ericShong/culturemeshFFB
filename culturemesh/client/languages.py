#
# CultureMesh Languages API 
#

####################### GET methods #######################

def get_language(client, langId):
	"""
	:param client: the CultureMesh API client
	:param langId: the id of the language to fetch

	Returns a language JSON.
	"""
	raise NotImplementedError

def language_autocomplete(client, input_text):
	"""
	:param client: the CultureMesh API client
	:param input_text: partial input text to a query field

	Returns a list of language JSONs
	in order of relevance.
	"""
	raise NotImplementedError