from unittest import TestCase, mock
from paa191t2.branch_and_bound.binary import serialize_key, get_bound, solve_formula, binary_bb


class TestBinary(TestCase):

    def test_if_serialize_is_correct(self):
        t_dict = dict()
        t_dict["9"] = 3
        t_dict["1"] = 12
        t_dict["2"] = 15
        s_dict = serialize_key(t_dict)
        self.assertEqual(s_dict, "[('1', 12), ('2', 15), ('9', 3)]")

    def test_if_getting_bound(self):
        instances = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["1", "2"],
            "5": ["1", "3"]
        }

        partition = {
            "1": True,
            "2": True,
            "3": True,
            "4": True,
            "5": True
        }

        weights = {
            "1": 2.0,
            "2": -1.0,
            "3": 4.0,
            "4": -2.5,
            "5": 1.5
        }

        self.assertEqual(get_bound(instances, partition, weights), 7.5)

    def test_if_getting_lower_bounding_if_variable_unset(self):
        instances = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["1", "2"],
            "5": ["1", "3"]
        }

        partition = {
            "1": True,
            "2": True,
            "3": False,
            "4": True,
            "5": True
        }

        weights = {
            "1": 2.0,
            "2": -1.0,
            "3": 4.0,
            "4": -2.5,
            "5": 1.5
        }

        self.assertEqual(get_bound(instances, partition, weights), 2.0)

    def test_if_solving_formula(self):
        instances = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["1", "2"],
            "5": ["1", "3"]
        }

        partition = {
            "1": True,
            "2": True,
            "3": True,
            "4": True,
            "5": True
        }

        weights = {
            "1": 2.0,
            "2": -1.0,
            "3": 4.0,
            "4": -2.5,
            "5": 1.5
        }

        self.assertEqual(solve_formula(instances, partition, weights), 4.0)

    def test_if_solving_formula_with_false(self):
        instances = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["1", "2"],
            "5": ["1", "3"]
        }

        partition = {
            "1": True,
            "2": True,
            "3": False,
            "4": True,
            "5": True
        }

        weights = {
            "1": 2.0,
            "2": -1.0,
            "3": 4.0,
            "4": -2.5,
            "5": 1.5
        }

        self.assertEqual(solve_formula(instances, partition, weights), -1.5)

    def test_running_sample(self):

        start_node_list = [1, 2, 3]

        instances = {
            "1": ["1"],
            "2": ["2"],
            "3": ["3"],
            "4": ["1", "2"],
            "5": ["1", "3"]
        }

        weights = {
            "1": 2.0,
            "2": -1.0,
            "3": 4.0,
            "4": -2.5,
            "5": 1.5
        }

        self.assertEqual(binary_bb(start_node_list, instances, weights), 7.5)