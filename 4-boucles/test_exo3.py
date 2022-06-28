from exo3 import moyenne_liste


def test_moyenne_liste():
    assert 6/3==moyenne_liste([1,2,3])
    assert 15/5==moyenne_liste([1,2,3,4,5])