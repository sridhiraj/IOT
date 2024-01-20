user_input = ''

LED_LIST = [[17, 'OUT'],[27, 'OUT'],[22, 'OUT'],[26, 'IN']]

				
def test(LED):
	print(LED[0], 'GPIO.OUT' if LED[1] == 'OUT' else 'GPIO.IN')

for LED in LED_LIST:
	test(LED);
	

