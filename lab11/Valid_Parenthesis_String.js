var checkValidString = function (s) {
  let low = 0;
  let high = 0;

  for (const char of s) {
    if (char === "(") {
      low++;
      high++;
    } else if (char === ")") {
      low = Math.max(low - 1, 0);
      high--;
    } else if (char === "*") {
      low = Math.max(low - 1, 0);
      high++;
    }

    if (high < 0) {
      return false;
    }
  }

  return low === 0;
};

console.log(checkValidString("()")); // Output: true
console.log(checkValidString("(*)")); // Output: true
console.log(checkValidString("(*))")); // Output: true
