from exo5 import inverse_ordre

def test_inverse_ordre():
    liste=[0,1,2,3,4,5,6]
    assert inverse_ordre(liste)==[6,5,4,3,2,1,0]
    liste=[0,1,2,3,4,5,6,7]
    assert inverse_ordre(liste)==[7,6,5,4,3,2,1,0]

