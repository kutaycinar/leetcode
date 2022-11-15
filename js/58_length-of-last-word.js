/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {

    counter = 0
    flag = false

    i = s.length - 1
    while (i >= 0) {

        // aZ
        if (s[i] !== " ") {
            counter++
            flag = true
        }
        // space
        else {
            if (flag)
                break
        }
        i--
    }

    return counter
};
