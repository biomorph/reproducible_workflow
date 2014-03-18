from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

# a test function returns nothing and it is self contained, tests if outputs are correct
# assert statement evaluates a statement and raises an error if it is false, if not it just moves on, assert is seen by pytest and it knows how to handle errors

def test_owl_is_correct():
    owlrec, owlmean = get_sightings(filename, 'Owl')
   # if you don't have a message after assert if it gives an error it will tell you what actual owltest calculated is in the error
    assert owlrec == 2, 'Number of records for owl is wrong'
    assert owlmean == 17, 'Mean sightings for owl is wrong'

def test_muskox_is_correct():
    oxrec, oxmean = get_sightings(filename, 'Muskox')
    assert oxrec == 2,'Number of records for Muskox is wrong'
    assert oxmean == 25.5, 'Mean sightings for Muskox is wrong'

def test_animal_not_present():
    animrec, animmean = get_sightings(filename, 'NotPresent')
    assert animrec == 0, 'Animal missing should return zero records'
    assert animmean == 0, 'Animal missing should return zero mean'

def test_mispelled_owl_is_correct():
    owlrec, owlmean = get_sightings(filename, 'owl')
   # if you don't have a message after assert if it gives an error it will tell you what actual owltest calculated is in the error
    assert owlrec == 2, 'Number of records for owl is wrong'
    assert owlmean == 17, 'Mean sightings for owl is wrong'


