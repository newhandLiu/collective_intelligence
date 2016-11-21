# coding=utf8

# A dictionary of movie critics and their ratings of a small set of movies
from math import sqrt

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                  'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
                     'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5,
                     'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0,
                     'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0,
                      'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}
}



def sim_distance(prefs, person1, person2):
    """ Calculate the Euclidean disance for person1 and person2
    """
    squares = [pow(prefs[person1][item] - prefs[person2][item], 2)
               for item in prefs[person1] if item in prefs[person2]]
    if len(squares) == 0:
        return 0
    return 1 / (1 + sum(squares))


def sim_pearson(prefs, p1, p2):
    """ Calculate the Pearson correlation coefficient for p1 and p2

    :param prefs:
    :param p1:
    :param p2:
    :return:
    """
    si = {item: 1 for item in prefs[p1] if item in prefs[p2]}
    n = len(si)
    if n == 0:
        return 0

    sum1 = sum(prefs[p1][it] for it in si.keys())
    sum2 = sum(prefs[p2][it] for it in si.keys())

    sum1_sq = sum(pow(prefs[p1][it], 2) for it in si.keys())
    sum2_sq = sum(pow(prefs[p2][it], 2) for it in si.keys())

    products_of_sum = sum([prefs[p1][it] * prefs[p2][it] for it in si.keys()])

    # calculate peason score
    num = products_of_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    else:
        r = num / den
        return r


def get_top_matches(prefs, person, n=5, similarity=sim_pearson):
    """
    Return the best matches for person from the prefs dictionary.
    :param prefs:
    :param person:
    :param n:
    :param similarity:
    :return:
    """
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores = sorted(scores, key=lambda tup: tup[0], reverse=True)
    return scores[:n]

def print_iter(iter):
    for item in iter:
        print item

if __name__ == '__main__':
    # print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
    # print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
    print '=======sim_pearson==========='
    print_iter(get_top_matches(critics, 'Toby', similarity=sim_pearson))
    print '=======sim_distance==========='
    print_iter(get_top_matches(critics, 'Toby', similarity=sim_distance))