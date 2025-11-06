const { rob } = require('./houseRobberII');

describe('rob', () => {
    it('should return the maximum amount of money you can rob from a small row', () => {
        const result = rob([1, 1, 3, 3]);
        expect(result).toEqual(4);
    });

    it('should return the maximum amount of money you can rob from a larger row', () => {
        const result = rob([2, 9, 8, 3, 6, 5, 17, 4, 8, 9, 3, 1]);
        expect(result).toEqual(44);
    });

    it('should return 0 if the row is empty', () => {
        const result = rob([]);
        expect(result).toEqual(0);
    });
});