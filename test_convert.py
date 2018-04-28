import unittest
from convert import parse_input, output


class ConvertorParseTest(unittest.TestCase):
	def test_no_argument_passed(self):
		data = parse_input("")
		self.assertEquals(data, (None, None, None))

	def test_100eur_to_usd(self):
		(amount, cents, currency) = parse_input("100 EUR")
		self.assertEquals(amount, 122)
		self.assertEquals(cents, 0)
		self.assertEquals(currency, "USD")

	def test_100usd_to_eur(self):
		(amount, cents, currency) = parse_input("100 USD")
		self.assertEquals(amount, 81)
		self.assertEquals(cents, 0)
		self.assertEquals(currency, "EUR")

	def test_99usd_to_eur(self):
		(amount, cents, currency) = parse_input("99 USD")
		self.assertEquals(amount, 80)
		self.assertEquals(cents, 19)
		self.assertEquals(currency, "EUR")

	def test_100usd_capital_letters(self):
		(amount, cents, currency) = parse_input("99 eur")
		self.assertEquals(amount, 120)
		self.assertEquals(cents, 78)
		self.assertEquals(currency, "USD")

	@unittest.skip("no functionality yet")
	def more_then_100_centes(self):
		pass


class ConvertorOutputTest(unittest.TestCase):
	def test_passed_arguments_have_cents(self):
		self.assertEquals(output(100, 0, "USD"), "100 USD")

	def test_passed_arguemnts_have_no_centes(self):
		self.assertEquals(output(89, 50, "EUR"), "89 EUR and 50 cents")
