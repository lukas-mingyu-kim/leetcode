

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """


    def run(self):
        test_cases = {
            123: 321,
            -123: -321,
            120: 21
        }

        for input, expected_output in test_cases.items():
            output = self.reverse(input)
            if output != expected_output:
                print(f'input: {input}, output: {output}, expected output: {expected_output}')

        print('PASSED ALL TESTS')
