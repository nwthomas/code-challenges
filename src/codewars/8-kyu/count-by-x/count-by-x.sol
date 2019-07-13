pragma solidity ^0.4.19;

contract CountByX {
  int[] z;
    
  function countBy(int x, int n) public returns (int[]) {
    if (n > 0) {
      z.push(x);
      for (uint8 i = 1; i < n; i++) {
        z.push(z[uint8(i) - 1] + x);
      }
    }
    return z;
  }
}