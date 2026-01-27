def NULL_not_found(object: any) -> int:
	tobj = str(type(object))
	match tobj:
		case "<class 'NoneType'>":
			if (object == None):
				print(f"Nothing: {object} {tobj}")
				return 0
		case "<class 'float'>":
			if (object != object):
				print(f"Cheese: {object} {tobj}")
				return 0
		case "<class 'int'>":
			if (object == 0):
				print(f"Zero: {object} {tobj}")
				return 0
		case "<class 'str'>":
			if (object == ''):
				print(f"Empty: {tobj}")
				return 0
		case "<class 'bool'>":
			if (object == False):
				print(f"Fake: {object} {tobj}")
				return 0
	print("Type not Found")
	return 1
