from voter import Voter
from graph import Node
from db import get_data_from_DB


check_voter_ids = ['101', '102', '103', '104', '105', '106', '107', '541', '786']
voters = get_data_from_DB(check_voter_ids)
graph_nodes = {epic_id: Node(voters[epic_id]) for epic_id in voters.keys()}


def estb_voter_relations():
    for epic_id in graph_nodes.keys():
        node = graph_nodes[epic_id]

        for relative_voter in node.relatives:  # updating the relative's relative
            if node.voter not in graph_nodes[relative_voter.epic_id].relatives:
                graph_nodes[relative_voter.epic_id].relatives.append(node.voter)


estb_voter_relations()


def get_valid_voters() -> list[Node]:
    return [node for node in graph_nodes.values() if node.check_valid_voter_or_not()]

print(*get_valid_voters(), sep='\n')

