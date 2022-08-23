from requests import get


class Cryptonator:
	def __init__(self):
		self.api = "https://api.cryptonator.com/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_currencies(self):
		return get(
			f"{self.api}/currencies",
			headers=self.headers).json()

	def get_simple_ticker(self, currency_code: str):
		return get(
			f"{self.api}/ticker/{currency_code}",
			headers=self.headers).json()

	def get_complete_ticker(self, currency_code: str):
		return get(
			f"{self.api}/full/{currency_code}",
			headers=self.headers).json()	
