/*
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
    def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N
doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..2,147,483,647].'
*/
var assert = require("assert");

function solution(n) {
  let maxGap = 0;
  const binary = n.toString(2);
  let zeroArray = binary.split("1");
  zeroArray.pop();

  for (element of zeroArray) {
    if (element.length > maxGap) {
      maxGap = element.length;
    }
  }
  return maxGap;
}

function testExecution(number, expected) {
  try {
    const result = solution(number);
    assert.equal(
      result,
      expected,
      `FAILED! For number ${number}: Expected ${expected}, but got ${result}.`
    );
  } catch (err) {
    console.log(err.message);
  }
}

testExecution(9, 2);
testExecution(529, 4);
testExecution(20, 1);
testExecution(15, 0);
testExecution(32, 0);
testExecution(1041, 5);
testExecution(561892, 3);
testExecution(74901729, 4);
testExecution(74901728, 3);
testExecution(1376796946, 5);
