import sys

rates = {"USD": 0.81, "EUR": 1.22}

def parse_input(text):
	if not text:
		return None, None, None

	amount = float(text.split()[0])
	currency = text.split()[1].upper()
	converted_current = "USD" if currency == "EUR" else "EUR"
	to_be_paid = round(amount*rates[currency], 2)
	cents = int(str(to_be_paid).split(".")[1])

	return int(to_be_paid), cents, converted_current


def output(amount, cents, currency):
	if not amount and not cents and not currency:
		return "You did mistake!"
	if cents == 0:
		return "%d %s" %(amount, currency)
	else:
		return "%d %s and %d cents" % (amount, currency, cents)

if __name__ == "__main__":
	data = parse_input(sys.argv[1])
	print(output(*data))
