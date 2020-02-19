#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Ever thing else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):


    my_score = 0
    some_score = 0

    if len(dice) == 0:
        return my_score

    ROLL_TO_POINTS = {
            1: 100,
            2: 0,
            3: 0,
            4: 0,
            5: 50,
            6: 0
        }
    SET_ROLL_TO_POINTS = {
            1: 1000,
            2: 2*100,
            3: 3*100,
            4: 4*100,
            5: 5*100,
            6: 6*100
          }


    int_count= 1

    def up_score(score, i, count):

      if count == 3 and i == 1:
        some_score = SET_ROLL_TO_POINTS[i] + score
      elif count == 3 and i == 5:
        some_score = 500 + score
      elif count >= 3:
        some_score = SET_ROLL_TO_POINTS[i]+ score
      else:
        some_score = (ROLL_TO_POINTS[i] * count) + score
      return some_score

    for i in range(0,len(dice)):
        if i < (len(dice)-1):
            if  dice[i] == dice[i+1]:
                if int_count == 3:
                    # sum = my_score
                    my_score =  up_score(my_score,dice[i],int_count)
                    int_count = 1
                    continue

                int_count+= 1
                # continue
            elif dice[i] != dice[i+1]:
                # sum = my_score
                my_score =  up_score(my_score,dice[i],int_count)
                int_count= 1
                # continue
        else:
            # sum = my_score
            my_score =  up_score(my_score,dice[i],int_count)



    return my_score








class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2,5,2,2,2]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))
