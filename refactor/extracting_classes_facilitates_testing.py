# extracting_classes_facilitates_testing.py

from after_refactor_extract_objs_when2eat_certain_food import OystersGood, TomatoesGood
import warnings


test = OystersGood('November')
assert test
assert test.r
assert not test.ary

test = OystersGood('July')
assert not test
assert not test.r
assert not test.ary

warnings.warn('Helpful warning here.')