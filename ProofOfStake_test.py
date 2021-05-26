from ProofOfStake import ProofOfStake


#if __name__ == '__main__':

def test_proofOfStake_update() -> None:    
    PoS = ProofOfStake()
    PoS.update('Alice', 10)
    assert PoS.getStake('Alice') == 10
    PoS.update('Alice', 100)
    assert PoS.getStake('Alice') == 110

def test_proofOfStake_getStake() -> None:
    PoS = ProofOfStake()
    assert PoS.getStake('Jake') == None