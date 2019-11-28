const {
  LeastFrequentlyUsedCache,
  Node
} = require("./leastFrequentlyUsedCache.js");

function testUtilsNamespace() {
  function returnCacheValues(LFUCache) {
    const final = [];
    let currentNode = LFUCache._head;
    while (currentNode) {
      final.push(currentNode._value[1]);
      currentNode = currentNode._next;
    }
    return final;
  }
  function setHundredValues(LFUCache) {
    for (let i = 1; i <= 100; i++) {
      LFUCache.set(`thing${i}`, i);
    }
  }
  return [returnCacheValues, setHundredValues];
}

describe("LeastFrequentlyUsedCache()", () => {
  let LFUCache;
  const [returnCacheValues, setHundredValues] = testUtilsNamespace();

  beforeEach(() => {
    LFUCache = new LeastFrequentlyUsedCache(20);
  });

  describe("instantiates", () => {
    it("tests that an LFU Cache has been instantiated", () => {
      expect(LFUCache instanceof LeastFrequentlyUsedCache).toBeTruthy();
    });
  });

  describe("set", () => {
    it("adds keys and values to the LFU Cache", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      expect(LFUCache.length()).toBe(2);
      expect(Object.keys(LFUCache._cache)).toEqual(["thing1", "thing2"]);
      expect(LFUCache._head._value).toEqual(["thing2", 2]);
    });

    it("handles the same value being added multiple times", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      LFUCache.set("thing1", 1);
      expect(LFUCache.length()).toBe(2);
      expect(Object.keys(LFUCache._cache)).toEqual(["thing1", "thing2"]);
      expect(LFUCache._head._value).toEqual(["thing1", 1]);
      expect(LFUCache._tail._value).toEqual(["thing2", 2]);
    });

    it("links all of the Nodes in order", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      LFUCache.set("thing3", 3);
      LFUCache.set("thing4", 4);
      expect(returnCacheValues(LFUCache)).toEqual([4, 3, 2, 1]);
    });

    it("handles trying to add a key value pair twice with n === 1", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing1", 1);
      expect(LFUCache.length()).toBe(1);
      expect(LFUCache._head === LFUCache._tail).toBeTruthy();
    });

    it("deletes old nodes to not exceed max cache size", () => {
      setHundredValues(LFUCache);
      expect(Object.keys(LFUCache._cache).length).toBe(20);
      expect(LFUCache.length()).toBe(20);
    });
  });

  describe("get", () => {
    it("gets values from the cache by key name", () => {
      LFUCache.set("thing1", 1);
      LFUCache.set("thing2", 2);
      const value = LFUCache.get("thing1");
      expect(value).toEqual(["thing1", 1]);
    });

    it("gets the value when a lot of values have been added to the cache", () => {
      setHundredValues(LFUCache);
      expect(LFUCache.get("thing100")).toEqual(["thing100", 100]);
    });

    it("returns null if the value is not present in the cache", () => {
      LFUCache.set("thing1", 1);
      expect(LFUCache.get("notAValidValue")).toBeFalsy();
    });
  });

  describe("length", () => {
    it("returns the length of the cache", () => {
      expect(LFUCache.length()).toBeFalsy();
      LFUCache.set("test", "test");
      expect(LFUCache.length()).toBe(1);
      setHundredValues(LFUCache);
      expect(LFUCache.length()).toBe(20);
    });
  });
});
