/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */

//  a b b c b c c c

var characterReplacement = function (s, k) {
  let l = 0;
  let r = 0;
  let max = 0;
  let res = 1;
  const hashMap = new Map();

  while (r <= s.length - 1) {
    hashMap[s[r]] = hashMap[s[r]] + 1;
    console.log(`hashMap[${s[r]}] = ${hashMap[s[r]]}`);
    max = Math.max(...Object.values(hashMap));
    while (!(r - l + 1 - max <= k)) {
      hashMap[s[l]] = hashMap.get(s[l]) - 1;
      max = Math.max(...Object.values(hashMap));
      l++;
    }
    res = Math.max(res, r - l + 1);
    r++;
  }
  return res;
};

const res = characterReplacement("ABAB", 2);
console.log(res);
