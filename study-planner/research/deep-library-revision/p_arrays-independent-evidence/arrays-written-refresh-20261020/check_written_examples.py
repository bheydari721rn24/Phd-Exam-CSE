import json
from pathlib import Path

ROOT = Path(__file__).parent
RESEARCH = Path(__file__).resolve().parents[4] / 'research'
checks = []

def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append({'name': name, 'actual': actual, 'expected': expected})

def normalize(value):
    return json.loads(json.dumps(value))

# Actual authored Python certificate programs, each in a fresh namespace.
for question in json.loads((RESEARCH / 'p_arrays-questions.json').read_text(encoding='utf-8')):
    certificate = question['certificate']
    if certificate['kind'] == 'python':
        program, expected = certificate['data']
        namespace = {}
        exec(compile(program, question['id'], 'exec'), namespace)
        check(question['id'], normalize(namespace['result']), expected)

# Independently constructed boundary cases for the written-source reconciliation.
def source_divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def proper_divisors(n):
    assert n >= 1
    return [x for x in range(1, n) if n % x == 0]

check('source_divisors_1_bug', source_divisors(1), [1])
check('proper_divisors_1', proper_divisors(1), [])
check('source_perfects_includes_1', [n for n in range(1, 1000) if sum(source_divisors(n)) == n], [1, 6, 28, 496])
check('correct_perfects_excludes_1', [n for n in range(1, 1000) if sum(proper_divisors(n)) == n], [6, 28, 496])

row = [3]
a = [row]
b = [x for x in a]
check('comprehension_distinct_outer', a is b, False)
check('comprehension_can_share_inner', a[0] is b[0], True)
b[0].append(8)
check('shared_inner_mutation', a, [[3, 8]])
t = (a[0],)
t[0].append(10)
check('tuple_referenced_object_mutable', a, [[3, 8, 10]])

for length in range(10):
    sequence = list(range(length))
    for spec in [slice(None, None, -1), slice(None, -1, -1), slice(-25, 25, 3), slice(8, -20, -2)]:
        indices = list(range(*spec.indices(length)))
        check('slice_indices_%s_%s' % (length, spec), sequence[spec], [sequence[i] for i in indices])

check('unicode_codepoints', len('Aé'), 2)
check('unicode_utf8_bytes', len('Aé'.encode('utf-8')), 3)
check('decomposed_character_codepoints', len('e\u0301'), 2)

# List membership compares an element, string membership checks a substring.
check('substring_membership', 'bc' in 'abcd', True)
check('list_element_membership', ['b', 'c'] in list('abcd'), False)

result = {'status': 'passed', 'checks': len(checks), 'entries': checks,
          'scope': 'Actual Python certificate programs plus independently authored boundary cases. No compiled C or C++ execution is claimed.'}
(ROOT / 'python-checks.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps({'status': 'passed', 'checks': len(checks)}))
