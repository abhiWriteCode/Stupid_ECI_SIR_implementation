from voter import Voter


ECI_2002_SIR_DB = {
	# EPIC_ID: NAME,
	'101': 'Vikas',
	'102': 'Pari',
	'103': 'Pushpa',
	'104': 'Harish',
	'105': 'Soma',
}
ECI_2026_SIR_DB = {
	# EPIC_ID: NAME,
	'101': 'Vikas',
	'103': 'Pushpa',
	'106': 'Aman',
	'107': 'Amok',
	'786': 'Abdul'
}

data_entry = {
    # Epic ID: {metadata}
    '101': {
        'name': 'Vikas', 'epic_id': '101',
        'father_name': 'Ranjan', 'mother_name': 'Pari',
        'father__epic_id': '', 'mother_epic_id': '102',
        'spouse_name': 'Pushpa', 'spouse_epic_id': '103'
    },
    '102': {
        'name': 'Pari', 'epic_id': '102',
        'father_name': '', 'mother_name': '',
        'father__epic_id': '', 'mother_epic_id': '',
        'spouse_name': 'Ranjan', 'spouse_epic_id': ''
    },
    '103': {
        'name': 'Pushpa', 'epic_id': '103',
        'father_name': 'Harish', 'mother_name': 'Soma',
        'father__epic_id': '104', 'mother_epic_id': '105',
        'spouse_name': 'Vikas', 'spouse_epic_id': '101'
    },
    '104': {
        'name': 'Harish', 'epic_id': '104',
        'father_name': '', 'mother_name': '',
        'father__epic_id': '', 'mother_epic_id': '',
        'spouse_name': 'Soma', 'spouse_epic_id': '105'
    },
    '105': {
        'name': 'Soma', 'epic_id': '105',
        'father_name': '', 'mother_name': '',
        'father__epic_id': '', 'mother_epic_id': '',
        'spouse_name': 'Harish', 'spouse_epic_id': '104'
    },
    '106': {
        'name': 'Aman', 'epic_id': '106',
        'father_name': 'Vikas', 'mother_name': 'Pushpa',
        'father__epic_id': '101', 'mother_epic_id': '103',
        'spouse_name': '', 'spouse_epic_id': ''
    },
    '107': {
        'name': 'Amok', 'epic_id': '107',
        'father_name': 'Vikas', 'mother_name': 'Pushpa',
        'father__epic_id': '101', 'mother_epic_id': '103',
        'spouse_name': '', 'spouse_epic_id': ''
    },
    '786': {
        'name': 'Abdul', 'epic_id': '786',
        'father_name': 'Md.', 'mother_name': 'Aisha',
        'father__epic_id': '9/11', 'mother_epic_id': '26/11',
        'spouse_name': 'Jihad', 'spouse_epic_id': '72hoors'
    },
}


def get_data_from_DB(epic_ids: list[int]) -> dict[int: Voter]:  # hard coded data 
	voters = {epic_id: Voter(**data_entry[epic_id]) for epic_id in epic_ids if epic_id in data_entry}
	return voters

def check_name_exists_in_2002_list(epic_id: str) -> bool:
	return epic_id in ECI_2002_SIR_DB
