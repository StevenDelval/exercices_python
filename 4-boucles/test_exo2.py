from exo2 import somme_liste

def test_somme_liste():
    assert 1+2+3==somme_liste([1,2,3])
    assert 1+2+3==somme_liste([0,1,2,0,3])
    assert 1+2+3+10+20==somme_liste([20,1,2,10,3])
    assert 1+2+3+10+22==somme_liste([20,1,2,10,3,2])
