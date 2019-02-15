# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import unittest

from qiskit.aqua.utils import get_entangler_map, validate_entangler_map
from test.common import QiskitAquaTestCase


class TestEngtanlerMap(QiskitAquaTestCase):

    def test_map_type_linear(self):
        ref_map = [[0, 1], [1, 2], [2, 3]]
        entangler_map = get_entangler_map('linear', 4)

        for (ref_src, ref_targ), (exp_src, exp_targ) in zip(ref_map, entangler_map):
            self.assertEqual(ref_src, exp_src)
            self.assertEqual(ref_targ, exp_targ)

    def test_map_type_full(self):
        ref_map = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        entangler_map = get_entangler_map('full', 4)

        for (ref_src, ref_targ), (exp_src, exp_targ) in zip(ref_map, entangler_map):
            self.assertEqual(ref_src, exp_src)
            self.assertEqual(ref_targ, exp_targ)

    def test_validate_entangler_map(self):
        valid_map = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        self.assertTrue(validate_entangler_map(valid_map, 4))

        valid_map_2 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [3, 2]]
        self.assertTrue(validate_entangler_map(valid_map_2, 4, True))

        invalid_map = [[0, 4], [4, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        with self.assertRaises(ValueError):
            validate_entangler_map(invalid_map, 4)

        invalid_map_2 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [3, 2]]
        with self.assertRaises(ValueError):
            validate_entangler_map(invalid_map_2, 4)

        wrong_type_map = {0: [1, 2, 3], 1: [2, 3]}
        with self.assertRaises(TypeError):
            validate_entangler_map(wrong_type_map, 4)

        wrong_type_map_2 = [(0, 1), (0, 2), (0, 3)]
        with self.assertRaises(TypeError):
            validate_entangler_map(wrong_type_map_2, 4)

if __name__ == '__main__':
    unittest.main()
