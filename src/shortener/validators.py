from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
	url_validator = URLValidator()
	value_1_invalid = False
	value_2_invalid = False

	try: #validate input 
		url_validator(value)
	except: #if url not valid, set value_1_invalid to true
		value_1_invalid = True

	value_2_url = "http://" + value

	try: #validate value_2_url
		url_validator(value_2_url)
	except: #if still invalid, set value_2_invalid to true
		value_2_invalid = True

	if value_1_invalid and value_2_invalid: #if both are True
		raise ValidationError("Invalid input")

	return value

def validate_dot_com(value):
	if not ".com" in value:
		raise ValidationError("no .com, invalid input")
	return value