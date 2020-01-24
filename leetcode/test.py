from typing import List, Dict


class Test(object):
    def __init__(self, func: callable, test_data: List[Dict], single_param=False):
        self.execute_func = func
        self.test_data = test_data
        self.single_param = single_param

    def test(self):
        for case in self.test_data:
            if self.single_param:
                r = self.execute_func(case["input"])
            else:
                r = self.execute_func(*case["input"])
            if case["output"] == r:
                print("OK")
            else:
                print("FAIL")
                print("case: {}, result: {}".format(case, r))
