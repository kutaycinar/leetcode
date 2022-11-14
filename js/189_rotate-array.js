/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {

    size = nums.length
    temp = [...nums]

    for (let i = 0; i < size; i++) {
        nums[(i + k) % size] = temp[i]
    }

};
