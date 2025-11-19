## Stupid ECI S.I.R. mapping using `bidirectional graph` data structure


### Output

```
Node(Voter(Epic=101)): [Voter(Epic=102), Voter(Epic=103), Voter(Epic=106), Voter(Epic=107)]
Node(Voter(Epic=102)): [Voter(Epic=101)]
Node(Voter(Epic=103)): [Voter(Epic=104), Voter(Epic=105), Voter(Epic=101), Voter(Epic=106), Voter(Epic=107)]
Node(Voter(Epic=104)): [Voter(Epic=105), Voter(Epic=103)]
Node(Voter(Epic=105)): [Voter(Epic=104), Voter(Epic=103)]
Node(Voter(Epic=106)): [Voter(Epic=101), Voter(Epic=103)]
Node(Voter(Epic=107)): [Voter(Epic=101), Voter(Epic=103)]
```
