import P1_game as GAME

TIMES = 20
TRIALTIMES = 1000
PROB_H = 0.5


Trial = GAME.trial(TRIALTIMES, TIMES, PROB_H)

print('The expected value is', Trial.get_ave_expected_cost())
