const {
  LeastFrequentlyUsedCache,
  Node
} = require("./leastFrequentlyUsedCache.js");

function returnCacheValues(LFUCache) {
  const final = [];
  let currentNode = LFUCache._head;
  while (currentNode) {
    final.push(currentNode._value[1]);
    currentNode = currentNode._next;
  }
  return final;
}

describe("LeastFrequentlyUsedCache()", () => {
  let LFUCache;

  beforeEach(() => {
    LFUCache = new LeastFrequentlyUsedCache(20);
  });

  describe("instantiates", () => {
    it("tests that an LFU Cache has been instantiated", () => {
      expect(LFUCache instanceof LeastFrequentlyUsedCache).toBeTruthy();
    });
  });

  describe("set", () => {
    it("should add keys and values to the LFU Cache", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      expect(LFUCache.length()).toBe(2);
      expect(Object.keys(LFUCache._cache)).toEqual(["thing1", "thing2"]);
      expect(LFUCache._head._value).toEqual(["thing2", 2]);
    });

    it("should handle the same value being added multiple times", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      LFUCache.set("thing1", 1);
      expect(LFUCache.length()).toBe(2);
      expect(Object.keys(LFUCache._cache)).toEqual(["thing1", "thing2"]);
      expect(LFUCache._head._value).toEqual(["thing1", 1]);
      expect(LFUCache._tail._value).toEqual(["thing2", 2]);
    });

    it("should successfully link all of the Nodes in order", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      LFUCache.set("thing3", 3);
      LFUCache.set("thing4", 4);
      expect(returnCacheValues(LFUCache)).toEqual([4, 3, 2, 1]);
    });
  });

  describe("get", () => {
    it("should get values from the cache by key name", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      const value = LFUCache.get("thing1");
      expect(value).toEqual(["thing1", 1]);
    });
  });
});
