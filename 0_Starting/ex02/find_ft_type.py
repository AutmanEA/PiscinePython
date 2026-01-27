def all_thing_is_obj(object: any) -> int :
	tobj = str(type(object))
	match tobj:
		case "<class 'list'>":
			print(f"List : {tobj}")
		case "<class 'tuple'>":
			print(f"Tuple : {tobj}")
		case "<class 'set'>":
			print(f"Set : {tobj}")
		case "<class 'dict'>":
			print(f"Dict : {tobj}")
		case "<class 'str'>":
			print(f"{object} is in the kitchen : {tobj}")
		case _:
			print("Type not found")
	return 42
