#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class ChoiceList(object):
    def __init__(self, choices):
        super(ChoiceList, self).__init__()
        self.choice_list = _make_choice_list(choices)
    
    def normalize(self, selection):
        for i in xrange(len(self.choice_list)):
            if selection in self.choice_list[i]:
                return self.choice_list[i][2]


def _make_choice_list(choices):
    indices = [str(i + 1) for i in xrange(len(choices))]
    return map((lambda curr_choice, index: [
        index,
        "({}) {}".format(index, curr_choice),
        curr_choice,
    ]), choices, indices)
