from voter import Voter
from db import get_data_from_DB


class Node:
    def __init__(self, voter: Voter):
        self.voter = voter
        relative_epic_ids = voter.get_relatives_epic_ids()
        voters = get_data_from_DB(relative_epic_ids)
        self.relatives = [voters[epic_id] for epic_id in relative_epic_ids if voters.get(epic_id) is not None]
        self.valid_voter: bool = False

    def check_valid_voter_or_not(self) -> bool:
        if self.voter.is_present_in_2002_SIR():
            self.valid_voter = True
        if any([True if relative_voter.is_present_in_2002_SIR() else False for relative_voter in self.relatives]):
            self.valid_voter = True
        return self.valid_voter

    def __repr__(self):
        return f"Node({self.voter}): {self.relatives}"
