class canarydictionary:
	
	def searchword(self, palabra):
		
		canario = {
			'millo': 'maiz',
			'papa': 'patata',
			'baifo': 'cabra',
			'godo': 'miguel',
			'guagua': 'autobus',
			'noword': None		
		}
		
		return canario[palabra]