import pathlib
import subprocess


def cmd2func(args):
    def func(inp):
        proc = subprocess.run(args, input=inp, text=True, capture_output=True)
        return proc.stdout, proc.stderr

    return func


def func2judge(sol):
    def func(inp, out):
        ans, _ = sol(inp)
        return ans == out, ans

    return func


def stress_tester(tests, solution, judge=None, catch_all=False):
    if judge is None:
        verdict, answer = False, ''
        catch_all = True

    for inp in tests:
        out, err = solution(inp)

        if judge:
            verdict, answer = judge(inp, out)

        if not verdict:
            print('Input')
            print(inp)

            print('Output')
            print(out)

            if err:
                print('Error')
                print(err)

            if answer:
                print('Answer')
                print(answer)

            print('-' * 80)

            if not catch_all:
                break


def test_gen():
    for i in range(10):
        yield str(i) + '\n'


def judge(inp, out):
    return out, ''


tests = test_gen()
solution = cmd2func(['python', 'A.py'])
# judge = func2judge(cmd2func(["python", "judge.py"]))

stress_tester(tests, solution)
