'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = 'test1.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################


def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    problem = {}
    nb_livres, nb_jours = [int(x) for x in input().split(' ')]
    problem['nb_livres'] = nb_livres
    problem['nb_jours'] = nb_jours
    problem['jours'] = []
    
    for i_jour in range(nb_jours):
        # charger les données du jour et les mettre dans la liste problem['jours']
        nb_clients = int(input())
        jour = {
            'nb_clients': nb_clients,
            'reservations': []
        }
        for i_client in range(nb_clients):
            i_livre, duree = [int(x) for x in input().split(' ')]
            reservation = {
                'i_livre': i_livre,
                'duree': duree
            }
            jour['reservations'].append(reservation)
        problem['jours'].append(jour)   
        
    
    return problem

def solve(problem):

    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__': #pas forcement nécessaire
    problem = parse_input()
    result = solve(problem)
    output(result)