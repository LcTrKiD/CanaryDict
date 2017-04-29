class canarydictionary:
	
	def searchword(self, palabra):
		
		canario = {
			'millo': 'maiz',
			'papa': 'patata',
			'baifo': 'cabra',
			'godo': 'miguel',
			'noword': None		
		}
		
		return canario[palabra]