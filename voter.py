

class Voter:
	def __init__(self, name:str, epic_id:str,
	             father_name:str, mother_name:str, 
	             father__epic_id="", mother_epic_id="",
	             spouse_name="", spouse_epic_id=""):
		self.name = name
		self.epic_id = epic_id
		self.father_name = father_name
		self.mother_name = mother_name
		self.father__epic_id = father__epic_id
		self.mother_epic_id = mother_epic_id
		self.spouse_name = spouse_name
		self.spouse_epic_id = spouse_epic_id

	def is_present_in_2002_SIR(self) -> bool:
		from db import check_name_exists_in_2002_list
		return check_name_exists_in_2002_list(self.epic_id)

	def get_relatives_epic_ids(self) -> list:
		return list(filter(lambda x: x != '', [self.father__epic_id, self.mother_epic_id, self.spouse_epic_id]))

	def __repr__(self):
		return f"Voter(Epic={self.epic_id})"
