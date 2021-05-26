from ProofOfStake import ProofOfStake
from Lot import Lot

def test_lotHashin()->None:
    lot = Lot('bob', 1, 'lastHash')
    assert lot.lotHash() == 'c682ef770875f2304a8b2617029926e147f252a1dede34f8805d59a89fdc5b83'
